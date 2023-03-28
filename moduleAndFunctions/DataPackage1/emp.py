class Employee:
    def __init__(self, eid, ename, sal): #these variable belongs to this constructor, to make them a class variable so they are
                                        # accessible everywhere
                                        # variable use self key word
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def displayemp(self): #this method is just for printing
        print(self.eid, self.ename, self.sal)