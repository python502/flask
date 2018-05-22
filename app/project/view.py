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
from . import project
import json

@project.route('/', methods=['GET'])
def project():
    if request.args.get('id'):
        project = NutemProject.query.filter_by(id=request.args.get('id')).first()
        results = json.dumps(project, cls=AlchemyEncoder)
    else:
        projects = NutemProject.query.order_by(NutemProject.createTime.desc()).limit(6).all()
        results = json.dumps(projects, cls=AlchemyEncoder)
    return results
    return render_template('index.html',form=form, name=session.get('name'),known=session.get('known', False))