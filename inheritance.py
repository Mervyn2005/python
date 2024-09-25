# 1.Single Inheritance

class thala:
    def __init__(self,tname):
        self.thala=tname
# class superstar:
#     def __init__(self,sname):
#         self.superstar=sname
class thalapathy(thala):
    def __init__(self,tname,thname):
        self.thname=thname
        super().__init__(tname)
    def __str__(self):
        return f"Iam Mervyn big fan of {self.thala}!!"
obj=thalapathy("thala","thalapathy")
print(obj)
print("-"*30)

# 2.Multipule Inheritance

# class Thalapathy(thala,superstar):
#     def __init__(self,tname,sname,thname):
#         self.Thname=Thname
#         thala.__init__(self,tname)
#         superstar.__init__(self,sname)
#     def __str__(self):
#         return f"Iam a {self.Thname} and I am a big fan of {self.thala} and {self.superstar}!!"
# obj=thalapathy("thala","superstar","thalapathy")
# print(obj)
# print("-"*30)

# 3 Multilevel Inheritance
class dhanush(thalapathy):
    def __init__(self,tname,thname,dname):
        self.dname=dname
        # thala.__init__(self,tname)
        thalapathy.__init__(self,tname,thname)
    def __str__(self):
        return f"I am {self.dname} and I am a big fan of {self.tname} and {self.thname}!!"
obj=dhanush("Thala","Thalapathy","Dhanush")
print(obj)