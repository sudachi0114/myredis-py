from gevent.server import StreamServer
from gevent.pool import Pool


class Server(object):
    def __init__(
        self, host: str = "127.0.0.1", port: int = 16379, max_clients: int = 64
    ) -> None:
        self._pool = Pool(max_clients)
        self._server = StreamServer(
            (host, port), self.connection_handler, spawn=self._pool
        )

        self._kv = {}
        self._commands = self.get_commands()

    def connection_handler(self, socket, address):
        socket_file = socket.makefile("rwb")
        raw_request = socket_file.readline().rstrip(b'\r\n')
        print(raw_request)
        request = raw_request.decode('utf-8')
        response = self.get_response(request)
        print(response)

    def get_commands(self):
        return {
            "GET": self.get,
            "SET": self.set
        }

    def get_response(self, request):
        # TODO: validation
        request = request.split()
        print(request)
        command = request[0].upper()
        print(command)
        return self._commands[command](*request[1:])

    def set(self, key, value):
        self._kv[key] = value
        return 1

    def get(self, key):
        return self._kv.get(key)

    def run(self):
        self._server.serve_forever()


if __name__ == "__main__":
    Server().run()
