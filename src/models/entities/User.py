from datetime import datetime

class User():

    def __init__(self, id, username, password, token, date) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.token = token
        self.date = date
    
    @classmethod
    def verify_expiration(self, date) -> None:
        if datetime.strptime(datetime.strftime(date, '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S') > datetime.now():
            return False
        else:
            return True