class Emp():
    pass


class Enginner(Emp):
    pass


class PM(Emp):
    pass


class HR(Emp):
    pass


EmpClasses = [Emp, Enginner, HR]
emp1 = Emp()
enginner1 = Enginner()
pm1 = PM()
hr1 = HR()
staffs = [(emp1, "emlpyee1"),
          (enginner1, "engineer1"),
          (pm1, "project manager1"),
          (hr1, "human resource1")]

for staff, name in staffs:
    for c in EmpClasses:
        isA = isinstance(staff, c)
        msg1 = 'is a' if isA else 'is not a'
        print(name, msg1, c.__name__)

print("***" * 30)
for c1 in EmpClasses:
    for c2 in EmpClasses:
        isSubclass = issubclass(c1, c2)
        message = '{0} a subclass of'.format('is' if isSubclass else 'is not')
        print(c1.__name__, message, c2.__class__)
