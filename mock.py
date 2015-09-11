__author__ = 'test_fing'
class fin_logger(object):

    def log_state(self,data):
        print data


class Resources(object):
    def __init__(self):
        self.credits = 0
        self.gold = 0

class player(object):
    def __init__(self):
        inventoryPlanes=[]

    def saveResources(self):
        print "res saved"