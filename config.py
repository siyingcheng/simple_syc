#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/1/11 0:25
# @Project  :   simples

import pathlib, os

basedir = pathlib.Path()


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'This is a secret key string.')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir.joinpath("data-dev.sqlite")


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///' + basedir.joinpath("data.sqlite"))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

if __name__ == '__main__':
    pass
