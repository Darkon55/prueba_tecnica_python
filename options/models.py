import uuid


class Endpoint:

    def __init__(self, username, password, url):
        self.username = username
        self.password =  password
        self.url =  url
    
    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['username', 'password', 'url']