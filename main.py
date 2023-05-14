from gevent.server import StreamServer

class Server(object):
    def __init__(self) -> None:
        self._server = StreamServer(("127.0.0.1", 16379), self.handle)

    def handle(self, socket, address):
        print("new connection!")

    def run(self):
        self._server.serve_forever()


if __name__ == "__main__":
    Server().run()
