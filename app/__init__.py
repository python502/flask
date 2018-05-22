#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 14:08
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
# @Desc    :

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()


# 工厂函数
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    #注册蓝本
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)
    # app.register_blueprint(main_blueprint, url_prefix = '/auth')
    return app

