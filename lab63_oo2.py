class Myclass:
    pass

print(type(Myclass),Myclass.__class__,Myclass.__class__.__bases__)

i1 = Myclass()

print(type(i1),i1.__class__,i1.__class__ == Myclass)