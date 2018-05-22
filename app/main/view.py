#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 14:33
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : view.py
# @Software: PyCharm
# @Desc    :
from flask import render_template, session, redirect, url_for, current_app, request
from .. import db
from ..models import NutemProject, AlchemyEncoder
from . import main
import json

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

