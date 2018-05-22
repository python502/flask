#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 11:36
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : manage.py
# @Software: PyCharm
# @Desc    :
from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()