# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import logging
import os.path
import shutil
import utils

log = logging.getLogger()


class Mirror(object):
    """
    Métodos para fazer mirror do banco
    """
    def __init__(self):
        """
        Método construtor
        """

    def copy(self, origin, filename):
        """
        Copy from origin to mirror

        :param origin: Origin file
        :param filename: Mirror file name
        :return:
        """
        usb_disks = utils.get_mount_points()
        if len(usb_disks) == 0:
            log.debug("MIRROR - No disk partitions found!")
            return False

        # Considera somente a primeira partição
        mirror_path = os.path.join(usb_disks[0][1], filename)

        # Sempre substitui a versão antiga
        shutil.copyfile(origin, mirror_path)

        log.debug("MIRROR - File %s copied to %s", origin, mirror_path)

        return True
