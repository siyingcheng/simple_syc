#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @License  :   ©Copyright 2021-2021, Simple-syc    
# @Author   :   SiYingCheng
# @Contact  :   siyingcheng@126.com
# @DateTime :   2021/1/10 21:42
# @Project  :   simples
import os

from flask import Flask

from config import config

app = Flask('simples')
app.config.from_object(config[os.getenv('FLASK_CONFIG', 'development')])


if __name__ == '__main__':
    