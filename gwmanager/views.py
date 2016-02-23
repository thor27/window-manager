# -*- coding: utf-8 -*-
import tornado.web
import json
import logging
import threading
from screen import Screen

logger = logging.getLogger()


class JsonHandler(tornado.web.RequestHandler):
    """
    Request handler where requests and responses speak JSON.
    Source: https://gist.github.com/mminer/5464753
    """
    def prepare(self):
        """
        Incorporate request JSON into arguments dictionary.
        """
        if self.request.body:
            try:
                self.json_data = json.loads(self.request.body.decode('utf-8'))
            except ValueError as e:
                logger.debug(e)
                message = 'Unable to parse JSON.'
                self.send_error(400, message=message)  # Bad Request

        # Set up response dictionary.
        self.response = dict()

    def set_default_headers(self):
        """
        Default headers for JSON
        """
        self.set_header('Content-Type', 'application/json')

    def write_error(self, status_code, **kwargs):
        """
        Write error to connection

        :param status_code: HTTP code error
        :param kwargs:
        :return:
        """
        if 'message' not in kwargs:
            if status_code == 405:
                kwargs['message'] = 'Invalid HTTP method.'
            else:
                kwargs['message'] = 'Unknown error.'

        self.response = kwargs
        self.write_json()

    def write_json(self):
        """
        Write JSON to output
        :return:
        """
        output = json.dumps(self.response)
        self.write(output)


class ScreenHandler(JsonHandler):
    """
    Handle requests
    """
    def prepare(self):
        """
        Prepare incoming request for handler
        """
        self.lock = False
        self.screen = Screen()
        super(ScreenHandler, self).prepare()

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        # 1 - Find operation
        try:
            operation = self.json_data['operation']
            name = self.json_data['name']
        except Exception as e:
            logger.debug("MASTER VIEW - Error\n%s", e)
            self.write_error(500, message=e)
            self.finish()

        # 2 - Execute operation
        method = getattr(self, operation)
        result = method(name)

    def focus(self, name):
        """
        Focus on screen

        :param name: Screen name
        """
        t = threading.Thread(
            target=self.screen.lock,
            args=(name,)
        )
        t.daemon = True
        t.start()

        self.response = {}
        self.write_json()
        self.finish()

    def release(self, name):
        """
        Release screen focus
        """
        self.screen.release()

        self.response = {}
        self.write_json()
        self.finish()


class KeyboardHandler(JsonHandler):
    """
    Handle requests
    """
    def prepare(self):
        """
        Prepare incoming request for handler
        """
        super(KeyboardHandler, self).prepare()

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        # 1 - Find operation
        try:
            operation = self.json_data['operation']
        except Exception as e:
            logger.debug("MASTER VIEW - Error\n%s", e)
            self.write_error(500, message=e)
            self.finish()

        # 2 - Execute operation
        method = getattr(self, operation)
        result = method()

        # Just return JSON
        self.response = {}
        self.write_json()
        self.finish()

    def lock(self):
        """
        Lock keyboard
        """

    def unlock(self):
        """
        Unlock Keyboard
        """
