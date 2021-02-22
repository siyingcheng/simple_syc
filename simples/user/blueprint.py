#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/2/14 21:21
# @Project  :   simples

from flask import Blueprint, render_template, url_for, redirect, flash, g, session

from simples import db
from simples.user.forms import UserForm, LoginForm
from simples.user.models import Users

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def index():
    return render_template('user/index.html', title='SiYingcheng个人博客')


@user_bp.route('/logout')
def logout():
    session.pop('username')
    flash('用户已登出!')
    return redirect(url_for('user.index'))


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('user.index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data.get('username')
        password = form.data.get('password')
        user = Users.query.filter_by(username=username).first()
        if user and user.check_password(password):
            flash('欢饮 {}!'.format(user.nickname), category='info')
            session['username'] = username
            return redirect(url_for('user.index'))
        flash('用户名密码错误', category='error')
    return render_template('user/login.html', form=form, title='登录')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        username = form.data.get('username')
        if Users.query.filter_by(username=username):
            flash('该用户已注册：' + username, category='error')
            return redirect(url_for('user.register'))
        password = form.data.get('password')
        email = form.data.get('email')
        user = Users()
        user.username = username
        user.nickname = username
        user.set_password(password)
        user.email = email
        db.session.add(user)
        db.session.commit()
        flash('注册成功: ' + username, category='info')
        return redirect(url_for('user.login'))
    return render_template('user/register.html', form=form, title='注册')
