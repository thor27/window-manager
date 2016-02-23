# -*- coding: utf-8 -*-
import tornado.web
import json
import logging
import threading
import subprocess
import sys
import os.path

logger = logging.getLogger()


class Keyboard(object):
    """
    Classe do teclado
    """
    def __init__(self):
        """
        :return:
        """
        pass

    def lock(self, name):
        """
        Lock keyboard
        """
        # Just execute command to lock keyboard
        process = subprocess.Popen([
            os.path.dirname(sys.executable) + "/autonumlock",
            name,
            "5"
        ], close_fds=True)
