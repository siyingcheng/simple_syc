#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/1/19 0:38
# @Project  :   simples
import enum

from simples.extensions import db


class RoleEnum(enum.Enum):
    admin = '管理员'
    publisher = '发布者'
    commenter = '评论者'


class Users(db.Model):
    __talbename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    nickname = db.Column(db.String(32), nullable=True)  # 昵称
    password_hash = db.Column(db.String(256))
    about = db.Column(db.String(128), nullable=True)  # 个人说明
    avatar = db.Column(db.String(256), nullable=True)  # 个人头像地址
    role = db.Column(db.Enum(RoleEnum), default=RoleEnum.commenter)

    def __str__(self):
        return self.username

    def __repr__(self):
        return '<Users {}>'.format(self.username)


if __name__ == '__main__':
    print('<Users {}>'.format('owen'))
