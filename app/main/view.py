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
@main.route('/project/v1.0/', methods=['GET'])
def project():
    if request.args.get('id'):
        project = NutemProject.query.filter_by(id=request.args.get('id')).first()
        results = json.dumps(project, cls=AlchemyEncoder)
    else:
        projects = NutemProject.query.all()
        results = json.dumps(projects, cls=AlchemyEncoder)
    return results

@main.route('/eth')
def index():
    print request.args.get('id')
    print request.args.get('sum')
    return 'fdfdf'
    # form = NameForm()
    #
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.name.data).first()
    #     if user is None:
    #         user = User(username=form.name.data)
    #         db.session.add(user)
    #         session['known'] = False
    #         if current_app.config['FLASKY_ADMIN']:
    #             send_email(current_app.config['FLASKY_ADMIN'], 'New User',
    #                        'mail/new_user', user=user)
    #     else:
    #         session['known'] = True
    #     session['name'] = form.name.data
    #     return redirect(url_for('.index'))
    # return render_template('index.html',form=form, name=session.get('name'),known=session.get('known', False))