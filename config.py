#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 10:45
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : config.py
# @Software: PyCharm
# @Desc    :
import os

basedir = os.path.abspath(os.path.dirname(__file__))
# 基类
class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flask]'
    FLASKY_MAIL_SENDER = 'Flask Admin'
    FLASKY_ADMIN = 'dimples'

    @staticmethod
    def init_app(app):
        pass

# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True

    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:111111@127.0.0.1:3306/world'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:shouhuang123!@#@106.14.205.157:3306/nutem'
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_RECYCLE = 1800
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {
    'default': DevelopmentConfig,
}