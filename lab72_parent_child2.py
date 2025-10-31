class Emp():
    gradeLevel = 6
    def startWork(self):
        pass
    def endWork(self):
        pass

class RD(Emp):
    def __init__(self):
        self.currentGrade = self.gradeLevel

    def startWork(self):
        print("[{}]start Work".format(self.currentGrade))

    def endWork(self):
        print("end work")

r1= RD()
r1.startWork()
r1.endWork()