#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 14:32
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
# @Desc    :

from flask import Blueprint
project = Blueprint('project', __name__)
from . import view, error