class Example():
    def __init__(self):
        self.__pList = []
    def addPerson(self,name,number):
        self.__pList.append(Person(name,number))
    def findPerson(self, **kwargs):
        return next(self.__iterPerson(**kwargs))
    def allPersons(self, **kwargs):
        return list(self.__iterPerson(**kwargs))
    def __iterPerson(self, **kwargs):
        return (person for person in self.__pList if person.match(**kwargs))

class Person():
    def __init__(self,name,number):
        self.nom = name
        self.num = number
    def __repr__(self):
        return "Person('%s', %d)" % (self.nom, self.num) 
    def match(self, **kwargs):
        return all(getattr(self, key) == val for (key, val) in kwargs.items())
    
a = Example()
a.addPerson('dave',123)
a.addPerson('mike',345)
a.addPerson('dave',678)

temp = a.findPerson(num=345)
all = a.allPersons()

print(temp)