# -*- coding: utf-8 -*-
import logging
import tornado.web
import tornado.ioloop
from views import ScreenHandler, KeyboardHandler

logger = logging.getLogger()


class Robot(object):
    """
    Robot object
    """
    def __init__(self, port):
        """
        :param port: Start port
        """
        self.port = port

    def start(self):
        """
        Start tornado Web Server
        """
        # App settings
        settings = {
            "debug": True,
            "xsrf_cookies": False,
        }

        app = tornado.web.Application(
            [
                (r"/screen", ScreenHandler),
                (r"/keyboard", KeyboardHandler),
            ],
            **settings
        )

        # Start tornado
        logger.debug("Starting tornado on port %s..." % self.port)
        app.listen(self.port, address='')
        tornado.ioloop.IOLoop.current().start()

    def stop(self):
        """
        Stop tornado web server
        """
        ioloop = tornado.ioloop.IOLoop.instance()
        ioloop.add_callback(ioloop.stop)
        logger.debug("Exiting tornado...")
