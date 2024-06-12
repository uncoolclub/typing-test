from utils.manager_json import create_file


class User:
    _instance = None

    def __new__(cls, nickname=None):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.nickname = nickname
        return cls._instance

    def __init__(self, nickname=None):
        pass

    def set_nickname(self, nickname):
        self.nickname = nickname
        create_file(nickname)

    def get_nickname(self):
        return self.nickname

