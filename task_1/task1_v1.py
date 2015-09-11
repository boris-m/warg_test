

class Account(object):
    id = 0
    def __new__(cls):
        Account.id += 1
        return object.__new__(cls)
    def __init__(self):
        pass


class Vechicle(Account):
    def __init__(self):
        pass


class Player(Account):
    def __init__(self):
        object_id_collector = self.id

class Bot(Account):
    def __init__(self):
        object_id_collector = self.id

class Tank(Vechicle):
    def __init__(self):
        object_id_collector = self.id

if __name__ == '__main__':
    print Player().id, Player().id, Tank().id, Bot().id, Player().id