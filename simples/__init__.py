#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/1/17 23:42
# @Project  :   simples
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from simples.extensions import db
from simples.settings import config

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def register_logging(app):
    """
    注册日志
    :param app:
    :return:
    """
    pass


def register_extensions(app):
    """
    注册扩展
    :param app:
    :return:
    """
    db.init_app(app)


def register_blueprints(app):
    """
    注册蓝图
    :param app:
    :return:
    """
    pass


def register_commands(app):
    """
    注册命令
    :param app:
    :return:
    """
    pass


def register_errors(app):
    """
    错误处理
    :param app:
    :return:
    """
    pass


def register_shell_context(app):
    """
    自定义shell命令
    :param app:
    :return:
    """
    @app.context_processor
    def make_shell_context():
        return dict(db=db)


def register_template_context(app):
    """
    模板上下文
    :param app:
    :return:
    """
    pass


def register_request_handles(app):
    """
    请求处理
    :param app:
    :return:
    """
    pass


def create_app(config_name):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('simples')
    app.config.from_object(config[config_name])

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errors(app)
    register_shell_context(app)
    register_template_context(app)
    register_request_handles(app)
    return app