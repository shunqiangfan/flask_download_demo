import flask
import find_file
import cfgs
import os



views_blueprint = flask.Blueprint('views', __name__, url_prefix='')


@views_blueprint.route('/', methods=['GET'])
def index_get():
    return flask.render_template(
        'index.html')


@views_blueprint.route('/download', methods=['GET'])
def download_get():
    return flask.render_template(
        'download.html',
        dirctory_contents=find_file.find_files_by_dirctory(cfgs.DIRCTORY_PATH))

@views_blueprint.route('/download/<path:name>', methods=['GET'])
def download_file_get(name):
    if(os.path.isdir(cfgs.DIRCTORY_PATH+'/'+name)):
        return flask.render_template(
            'download.html',
            dirctory_contents=find_file.find_files_by_dirctory(cfgs.DIRCTORY_PATH+'/'+name,name+'/'))
    elif(os.path.isfile(cfgs.DIRCTORY_PATH+'/'+name)):
        file_path=find_file.get_file_path(name)
        file_name=find_file.get_file_name(name)
        print(file_path)
        print(file_name)
        return flask.send_from_directory(cfgs.DIRCTORY_PATH+'/'+file_path, file_name, as_attachment=True)
    else:
        return "Error file!"
