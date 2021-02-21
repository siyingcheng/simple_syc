#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/2/16 21:09
# @Project  :   simples
import re

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from simples.settings import INVITE_CODE


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=32)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=256)])
    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=32)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=256)])
    repassword = PasswordField('RePassword', validators=[DataRequired()])
    email = EmailField('Email', validators=[Email()])
    code = StringField('Invite Code', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_username(self, field):
        if not re.match('^[a-zA-Z0-9_]{6,32}$', field.data):
            flash('请输入6到32位的大小写字母、数字或者下划线的组合')
            raise ValidationError('请输入6到32位的大小写字母、数字或者下划线的组合')

    def validate_password(self, field):
        if not re.match(r'^[a-zA-Z0-9`~!@#$%^&*()-_=+\\|\[\]{}:;\'\"?/.>,<]{8,256}$', field.data):
            flash('请输入8到256位的密码，必须包含大小、写字母、数字或者特殊符号的至少两种组合')
            raise ValidationError('请输入8到256位的密码，必须包含大小、写字母、数字或者特殊符号的至少两种组合')
        match_count = 0
        if re.search(r'[0-9]', field.data):
            match_count += 1
        if re.search(r'[a-z]', field.data):
            match_count += 1
        if re.search(r'[A-Z]', field.data):
            match_count += 1
        if re.search(r'[`~!@#$%^&*()-_=+\\|\[\]{}:;\'\"?/.>,<]', field.data):
            match_count += 1
        if match_count < 2:
            flash('请输入8到256位的密码，必须包含大小、写字母、数字或者特殊符号的至少两种组合')
            raise ValidationError('请输入8到256位的密码，必须包含大小、写字母、数字或者特殊符号的至少两种组合')

    def validate_repassword(self, field):
        if self.password.data != field.data:
            flash('两次密码不一致')
            raise ValidationError('两次密码不一致')

    def validate_code(self, field):
        if field.data != INVITE_CODE:
            flash('邀请码错误')
            raise ValidationError('邀请码错误')
