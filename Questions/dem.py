class Doselect:
    def new(self):
        self.init(self)
        print("Doselct's new() Invoked")
    def init(self):
        print("Doselct's init() Invoked")

class Derived_Doselect(Doselect):
    def new(self):
        print("Derived_Doselect's new() Invoked")
    def init(self):
        print("Derived_Doselect's init() Invoked")

def main():
    obj1=Derived_Doselect()
    obj2=Doselect()
main()

# print('\'.join(['x','y','z']))
# d={
#     'foo':100,
#     'foo':200,
#     'foo':300
# }
a,b,c=(1,2,3,4,5,6,7,8,9)[1::3]
print(b)