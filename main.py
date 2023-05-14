from gevent.server import StreamServer
from gevent.pool import Pool


class Server(object):
    def __init__(
        self, host: str = "127.0.0.1", port: int = 16379, max_clients: int = 64
    ) -> None:
        self._pool = Pool(max_clients)
        self._server = StreamServer((host, port), self.connection_handler, spawn=self._pool)

    def connection_handler(self, socket, address):
        socket_file = socket.makefile('rwb')
        print(socket_file.readline())

    def run(self):
        self._server.serve_forever()


if __name__ == "__main__":
    Server().run()
