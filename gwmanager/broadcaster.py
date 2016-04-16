from sockjs.tornado import SockJSRouter, SockJSConnection
import logging

logger = logging.getLogger()

class BroadcastConnection(SockJSConnection):
    clients = set()

    def on_open(self, info):
        self.clients.add(self)

    def on_message(self, msg):
        logger.debug('Number of clients: {0} Message: {1}'.format(str(len(self.clients)), msg))
        self.broadcast(self.clients, msg)

    def on_close(self):
        self.clients.remove(self)

BroadcastRouter = SockJSRouter(BroadcastConnection, '/broadcast')
urls = BroadcastRouter.urls
