#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/2/14 21:21
# @Project  :   simples

from flask import Blueprint, render_template, url_for, redirect, get_flashed_messages

from simples import db
from simples.user.forms import UserForm
from simples.user.models import Users

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def index():
    return render_template('user/index.html')


@user_bp.route('/login')
def login():
    return render_template('user/login.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        username = form.data.get('username')
        password = form.data.get('password')
        email = form.data.get('email')
        user = Users()
        user.username = username
        user.set_password(password)
        user.email = email
        db.session.add(user)
        db.session.commit()
        print('添加成功：' + username)
        return redirect(url_for('user.index'))
    else:
        print('校验失败')
        for msg in get_flashed_messages():
            print('error->' + msg)
    return render_template('user/register.html', form=form)
