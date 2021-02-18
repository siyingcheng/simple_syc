#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/1/17 23:47
# @Project  :   simples

import os
import sys
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent

STATIC_FOLDER = str(BASE_DIR.joinpath('static'))

TEMPLATE_FOLDER = str(BASE_DIR.joinpath('templates'))

INVITE_CODE = os.getenv('INVITE_CODE', 'invite code dev')


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CRSF_ENABLE = False
    SQLALCHEMY_DATABASE_URL = prefix + ':memory:'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

if __name__ == '__main__':
    print(BASE_DIR)
