class Student:
    def __init__(self, sid, sname, sgrade): #these variable belongs to this constructor, to make them a class variable so they are
                                        # accessible everywhere
                                        # variable use self key word
        self.sid=sid
        self.sname=sname
        self.sgrade=sgrade
    def displaystu(self): #this method is just for printing
        print(self.sid, self.sname, self.sgrade)