import sys  # needed for epsilon in Newton function

class FindRoots:
    def __init__(self, polyArray, a, b, degree):
        self.polyArray = polyArray
        self.a = a
        self.b = b
        self.degree = degree      # 3x^3 + 2X^2 -2x + 1 = 0  --> degree 3 == length -1


    def evalFx(self, x):
        #3x^3 + 2x^2 - 2x + 1

        #solve for x^some power:
        result = 0
        print(str(x))
        i = 0
        for index in range(len(self.polyArray) - (self.degree+1), len(self.polyArray)):
            xTerm = 1
            for power in range(0, self.degree - i):        # e.g. power = 3 --> x*x*x   or power = 2 --> x*x 3 --> 0
                xTerm = xTerm * x                                   # 3-->1,  2--> 1, 1--> 1, 0
            i = i + 1
            print("xTerm = " + str(xTerm))
            result = result + self.polyArray[index]*xTerm
            print("result: " + str(result))
        print("Final result = " + str(result))

    def execute(self):
        currC = 0
        for count in range(10000):
            fa = self.evalFx(self.a)
            fb = self.evalFx(self.b)
            currC = (((self.a)*fb)) - (((self.b)*fa)) / (fb - fa)
            fc = self.evalFx(currC)
            if fa*fc < 0:
                self.b = currC
            elif (fa*fc) > 0:
                self.a = currC
            else:
                break

        return currC


