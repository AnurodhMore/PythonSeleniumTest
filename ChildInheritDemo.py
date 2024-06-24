from OOPSDemo import Calculator


class  ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 10, 20)  #calling parent constructor

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = ChildImpl()
print(obj.getCompleteData())