#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/1/19 0:38
# @Project  :   simples
import enum

from werkzeug.security import generate_password_hash, check_password_hash

from simples.extensions import db


class RoleEnum(enum.Enum):
    admin = '管理员'
    publisher = '发布者'
    commenter = '评论者'


class Users(db.Model):
    __talbename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    nickname = db.Column(db.String(32), nullable=True)  # 昵称
    password_hash = db.Column(db.String(256))
    email = db.Column(db.String(128))
    about = db.Column(db.String(128), nullable=True)  # 个人说明
    avatar = db.Column(db.String(256), nullable=True)  # 个人头像地址f

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return self.username

    def __repr__(self):
        return '<Users {}>'.format(self.username)


if __name__ == '__main__':
    print('<Users {}>'.format('owen'))
