from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrio_blocks = True

db = SQLAlchemy(app)
db.init_app(app)
db.create_all(app=app)

bootstrap = Bootstrap(app)
moment = Moment(app)

from sayhello import views