from flask import Flask
from views import views

app = Flask (__name__)

# THe route has been set up in the views.py instead.
#
# @app.route("/")
# def home():
#     return "This is the home page"
#

app.register_blueprint(views, url_prefix='/views/lala')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

