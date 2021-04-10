import flask
import views
import cfgs

app = flask.Flask(__name__)
app.register_blueprint(views.views_blueprint)


def main():
    app.run(host=cfgs.HOST,
            port=cfgs.PORT,
            debug=cfgs.DEBUG)

if __name__ == "__main__":
    main()