
#1
class Ex:
    pass
class Example1(Ex):

    name ='Royal'

    def __init__(self):
        company='Limited'
        self.name='New'
        self.company ='Pvt'

    @classmethod
    def class_display(cls):
        print(cls.name)

    def display(self,variable):
        if variable == 'name':
            print(self.name)
        elif variable == 'company':
            print(self.company)
            # print(batch)
        # print(f"{self.name} {self.company}")

ex=Example1()
# Example1.class_display()
# ex.class_display()
# ex.display(input("enter variable"))
print(ex.__dict__)
ex.batch='General'

print(ex.__dict__)
del ex.batch
print(ex.__dict__)
print(issubclass(Example1,Ex))