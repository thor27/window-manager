#!/usr/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import os
import configparser
import logging
import logging.config

environment = 'development'


def load_config():
    """
    Carrega configuração
    :return:
    """
    config = configparser.ConfigParser()
    here = os.path.abspath(os.path.dirname(__file__))
    config_file = os.path.join(here, '../' + environment + '.ini')
    config.read(config_file)

    # Logging
    logging.config.fileConfig(config_file)

    return config
