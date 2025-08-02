class  Starboy:
    __name1 = 'arav'
    def __init__(self, name,age,address):
        self.__name = name
        self.age = age
        self.address = address
    def hi(self):
        print('welcome to class')
        print(f'name:{self.__name}\n age :{self.age}\n address :{self.address}')
        
    
obj = Starboy('arav',25,'ktm')
# obj.hi()
print(obj._Starboy__name)