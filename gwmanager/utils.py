#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from glob import glob
from subprocess import check_output, CalledProcessError


def get_usb_devices():
    """
    Lista dispositivos USB conectados

    :return:
    """
    sdb_devices = map(os.path.realpath, glob('/sys/block/sd*'))
    usb_devices = (dev for dev in sdb_devices
        if 'usb' in dev.split('/')[5])
    return dict((os.path.basename(dev), dev) for dev in usb_devices)


def get_mount_points(devices=None):
    """
    Lista pontos de montagem

    :param devices:
    :return: Lista de tuplas

        [('/dev/sdb1', '/media/bisa/BACKUP')]
    """
    devices = devices or get_usb_devices() # if devices are None: get_usb_devices
    output = check_output(['mount']).splitlines()
    is_usb = lambda path: any(dev in path for dev in devices)
    usb_info = (line for line in output if is_usb(line.split()[0]))
    return [(info.split()[0], info.split()[2]) for info in usb_info]
