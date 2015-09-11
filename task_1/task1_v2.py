

class Account(object):
    count = 0.0

    def __getattr__(self, attr):
        Account.count += 0.5
        return int(Account.count)

Vechicle=Account


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