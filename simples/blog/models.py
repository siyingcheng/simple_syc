#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/1/20 0:05
# @Project  :   simples
from datetime import datetime, timezone, timedelta

from simples.extensions import db


posts_labels = db.Table('posts_labels',
                        db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
                        db.Column('label_id', db.Integer, db.ForeignKey('label.id'), primary_key=True)
                        )


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    posts = db.relationship('Post', lazy='select', backref=db.backref('categories', lazy='joined'))


class Label(db.Model):
    __tablename__ = 'labels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    posts = db.relationship('Post', secondary=posts_labels, lazy='subquery',
                            backref=db.backref('labels', lazy=True))


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.relationship('User', lazy='select', backref=db.backref('posts', lazy='joined'))
    title = db.Column(db.String(64))
    abstract = db.Column(db.String(256), nullable=True)  # 摘要
    body = db.Column(db.Text)
    ctime = db.Column(db.DateTime, default=datetime.now(tz=timezone(timedelta(hours=8), name='Aisa/Shanghai')))
    mtime = db.Column(db.DateTime, default=ctime)
    comments = db.relationship('Comment', lazy='select', backref=db.backref('posts', lazy='joined'))


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author = db.relationship('User', lazy='select', backref=db.backref('comments', lazy='joined'))
    body = db.Column(db.Text)
    ctime = db.Column(db.DateTime, default=datetime.now(tz=timezone(timedelta(hours=8), name='Aisa/Shanghai')))
    mtime = db.Column(db.DateTime, default=ctime)
    replied_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    replied = db.relationship('Comment', back_populates='replies', remote_side=[id])
    replies = db.relationship('Comment', back_populates='replied', cascade='all')
