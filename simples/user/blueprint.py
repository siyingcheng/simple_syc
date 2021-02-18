#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/2/14 21:21
# @Project  :   simples

from flask import Blueprint, render_template, url_for

from simples.user.forms import UserForm

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def index():
    return render_template('user/index.html')


@user_bp.route('/login')
def login():
    return render_template('user/login.html')


@user_bp.route('/register')
def register():
    form = UserForm()
    return render_template('user/register.html', form=form)