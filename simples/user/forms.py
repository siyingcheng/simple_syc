#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/2/16 21:09
# @Project  :   simples
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length

from simples.settings import INVITE_CODE


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=32)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=256)])
    repassword = PasswordField('RePassword', validators=[DataRequired()])
    email = EmailField('Email', validators=[Email()])
    code = StringField('Invite Code', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_repassword(self, field):
        if self.password != field.data:
            raise ValueError('两次密码不一致')

    def validate_code(self, field):
        if field.data != INVITE_CODE:
            raise ValueError('邀请码错误')
