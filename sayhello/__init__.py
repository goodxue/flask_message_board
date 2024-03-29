from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_object('sayhello.settings')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrio_blocks = True

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
from sayhello import views

# db.init_app(app)
# db.drop_all(app=app)
db.create_all(app=app)


