from flask import Flask
import os
# from os import getenv

import logging
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite_script.db'

    # logging.basicConfig(filename='record.log', level=logging.DEBUG,
                    # format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

    # import blueprints
from .views.admin import admin
from .views.students import student
from .views.courses import course
from .views.colleges import college

    # register blueprints
app.register_blueprint(admin)
app.register_blueprint(student)
app.register_blueprint(course)
app.register_blueprint(college)
app.secret_key = os.getenv('SECRET_KEY')

# def create_app() -> object:
    # app = Flask(__name__)
    # app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite_script.db'

    # # logging.basicConfig(filename='record.log', level=logging.DEBUG,
    #                 # format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

    # # import blueprints
    # from .views.admin import admin
    # from .views.students import student
    # from .views.courses import course
    # from .views.colleges import college

    # # register blueprints
    # app.register_blueprint(admin)
    # app.register_blueprint(student)
    # app.register_blueprint(course)
    # app.register_blueprint(college)

    # return app
