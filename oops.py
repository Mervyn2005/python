class cars:
    def __init__(self,name,modal,transmission,dtype):
        self.name = name
        self.modal = modal
        self.transmission = transmission
        self.dtype = dtype
    def __str__(self):
        return f'''I like a car called {self.name}, particularly a modal called {self.modal}.
It has {self.transmission} and it drives as {self.dtype}'''
BMW = cars("BMW","M5","Automatic","AWD")
Suzuki = cars("Suzuki","Swift","Manual","FWD")
Ford = cars("Ford","Mustang","Automatic","RWD")
print(BMW)
print(Suzuki)
print(Ford)
print(BMW.name)
print(BMW.transmission)
b='hi'
a=input()
print(a)