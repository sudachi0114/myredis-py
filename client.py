from gevent import socket

class Client(object):
    def __init__(self, host: str = "127.0.0.1", port: int = 16379) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((host, port))
        self._fh = self._socket.makefile("rwb")

    def execute(self, *args):
        command = " ".join(args).encode("utf-8")
        print(command)
        self._fh.write(command)
        self._fh.flush()

    def set(self, key, value):
        return self.execute("SET", key, value)

    def get(self, key):
        return self.execute("GET", key)
