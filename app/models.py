#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 10:53
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : models.py
# @Software: PyCharm
# @Desc    :
from app import db
import datetime
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x not in ['metadata', 'query', 'query_class']]:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, datetime.datetime):
                        data = data.strftime("%Y%m%d%H%M%S")
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)
class NutemProject(db.Model):
    """Represents Proected users."""
    '''Table: nutem_project
    Columns:
    id varchar(32) PK 
    createTime datetime 
    deleted bit(1) 
    lastEditTime datetime 
    lastEditor varchar(255) 
    uniqueId varchar(255) 
    buildTime varchar(20) 
    compactStatus varchar(40) 
    customerName varchar(100) 
    feeAmount varchar(20) 
    finalCustomerName varchar(100) 
    operateTime varchar(20) 
    projectStatus varchar(255) 
    sn varchar(50) 
    summary varchar(250) 
    teamwork varchar(200) 
    techName varchar(50) 
    title varchar(100) 
    titleEn varchar(100) 
    manager_id varchar(32) 
    multi_project_id varchar(32) 
    monitor varchar(32) 
    coding varchar(20) 
    workflowStatus varchar(255) 
    qulityFiles longtext 
    taskFile varchar(255)'''
    # Set the name for table
    __tablename__ = 'nutem_project'
    id = db.Column(db.String(32), primary_key=True, unique=True)
    createTime = db.Column(db.DateTime())
    deleted = db.Column(db.Boolean())
    lastEditTime = db.Column(db.DateTime())
    lastEditor = db.Column(db.String(255))
    uniqueId = db.Column(db.String(255))
    buildTime = db.Column(db.String(20))
    compactStatus = db.Column(db.String(40))
    customerName = db.Column(db.String(100))
    feeAmount = db.Column(db.String(20))
    finalCustomerName = db.Column(db.String(100))
    operateTime = db.Column(db.String(20))
    projectStatus = db.Column(db.String(255))
    sn = db.Column(db.String(50))
    summary = db.Column(db.String(250))
    teamwork = db.Column(db.String(200))
    techName = db.Column(db.String(50))
    title = db.Column(db.String(100))
    titleEn = db.Column(db.String(20))
    manager_id = db.Column(db.String(32))
    multi_project_id = db.Column(db.String(32))
    monitor = db.Column(db.String(32))
    coding = db.Column(db.String(20))
    workflowStatus = db.Column(db.String(255))
    qulityFiles = db.Column(db.Text())
    taskFile = db.Column(db.String(255))

    def __init__(self, id, createTime, deleted, lastEditTime, lastEditor, uniqueId, buildTime, compactStatus, customerName, feeAmount, finalCustomerName, operateTime, projectStatus\
                 , sn, summary, teamwork, techName, title, titleEn, manager_id, multi_project_id, monitor, coding, workflowStatus, qulityFiles, taskFile):
        self.id = id
        self.createTime = createTime
        self.deleted = deleted
        self.lastEditTime = lastEditTime
        self.lastEditor = lastEditor
        self.uniqueId = uniqueId
        self.buildTime = buildTime
        self.compactStatus = compactStatus
        self.customerName = customerName
        self.feeAmount = feeAmount
        self.finalCustomerName = finalCustomerName
        self.operateTime = operateTime
        self.projectStatus = projectStatus
        self.sn = sn
        self.summary = summary
        self.teamwork = teamwork
        self.techName = techName
        self.title = title
        self.titleEn = titleEn
        self.manager_id = manager_id
        self.multi_project_id = multi_project_id
        self.monitor = monitor
        self.coding = coding
        self.workflowStatus = workflowStatus
        self.qulityFiles = qulityFiles
        self.taskFile = taskFile

    def __repr__(self):
        #__repr__ 当打印User对象时显示的数据。
        return "<Model NutemProject `{}`>".format(self.id)

    # def as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}
