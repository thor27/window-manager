# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import os
import time


class Screen(object):
    """
    Tela
    """
    def __init__(self):
        """
        Método construtor
        """
        here = os.path.abspath(os.path.dirname(__file__))
        self.lockfile = os.path.join(here, '../.screen')

    def lock(self, name):
        """
        Lock screen focus

        :param name: Screen name
        """
        # Primeiro precisa liberar o lock
        if self.is_locked():
            self.release()
            time.sleep(1)

        # Agora cria um novo lock para o processo
        with open(self.lockfile, 'w+') as fd:
            fd.write("")
            fd.close()

        while True:
            if self.is_locked():
                os.system("wmctrl -R '{}'".format(name))
                time.sleep(1)
            else:
                break

    def is_locked(self):
        """
        Verifica se a tela está travada
        :return:
        """
        if os.path.exists(self.lockfile):
            return True
        else:
            return False

    def release(self):
        """
        Libera a trava do arquivo
        """
        if os.path.exists(self.lockfile):
            os.unlink(self.lockfile)
