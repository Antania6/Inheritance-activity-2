class person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printname(self):
        print(self.firstName,self.lastName)


class student(person):
    def __init__(self,firstName,lastName,year):
        super().__init__(firstName,lastName)
        self.graduationyear = year


obj=student("mark","henry",2021)
obj.printname()
print(obj.graduationyear)