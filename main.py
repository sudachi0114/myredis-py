from gevent.server import StreamServer
from gevent.pool import Pool


class Server(object):
    def __init__(
        self, host: str = "127.0.0.1", port: int = 16379, max_clients: int = 64
    ) -> None:
        self._pool = Pool(max_clients)
        self._server = StreamServer((host, port), self.handle, spawn=self._pool)

    def handle(self, socket, address):
        print("new connection!")

    def run(self):
        self._server.serve_forever()


if __name__ == "__main__":
    Server().run()
