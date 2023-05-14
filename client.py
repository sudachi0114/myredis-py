class Client(object):
    def __init__(self) -> None:
        pass

    def execute(self, *args):
        print(args)

    def set(self, key, value):
        return self.execute("SET", key, value)

    def get(self, key):
        return self.execute("GET", key)
