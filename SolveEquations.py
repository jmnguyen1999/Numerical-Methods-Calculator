#    file: SolveEquations.cpp
#    class: SolveEquations
#    Purpose:
#        This class can solve any system of equations given their coefficients and the number of equations there are. This class
#        serves as one of the functions on the Numerical Methods calculator
#
class SolveEquations:
    #constructor: given all the coefficients, and the # of equations
    def __init__(self, fullMatrix, numOfEq):
        self.fullMatrix = fullMatrix
        self.numOfEq = numOfEq
        self.numOfVar = numOfEq  # # of variables to solve == # of equations there are
        self.coeffMatrix = [[0 for cols in range(self.numOfEq)] for rows in range(self.numOfVar)]
        self.b = [0 for i in range(self.numOfEq)]
        self.L = [0 for i in range(self.numOfEq)]
        self.S = [0 for i in range(self.numOfEq)]
        self.solutions = [0 for i in range(self.numOfEq)]
        for num in range(len(self.L)):
            self.L[num] = num + 1
        self.initialS()

    #Solves the system of equations!, executes the steps in correct order:
    def execute(self):
        #NOTE: k = iteration #
        #1.) Forward Elimination: Loop does n-1 iterations, n = # of equations
        for k in range(1, self.numOfEq):
            # 1.) Do the scaled ratios, and find which index of L lies the pivot eq.
            pivotEqIndex = self.doRatios(k)

            # 2.) Update L to switch the pivot eq. to correct spot (correct spot = index k-1)
            valueToSwitch = self.L[k - 1]
            self.L[k - 1] = self.L[pivotEqIndex]
            self.L[pivotEqIndex] = valueToSwitch

            # 3.) Do an iteration and print matrix after
            self.iteration(k)

        #2.) Back substitution:
        # 1.) Copy b and coeffMatrix from fullMatrix for back sub use
        for i in range(len(self.b)):
            self.b[i] = self.fullMatrix[i][self.numOfVar]
        for row in range(self.numOfEq):
            for col in range(self.numOfVar):
                self.coeffMatrix[row][col] = self.fullMatrix[row][col]

        #3.) Get solutions
        self.backSub()
        return self.solutions



    # initializes S[], finds the max element (in abs. value) in each row of matrix
    def initialS(self):
        for row in range(self.numOfEq):
            max = 0
            for col in range(self.numOfVar):      # purposely doesn't include the b values
                elem = abs(self.fullMatrix[row][col])

                if elem > max:
                    max = elem
            self.S[row] = max


    # calculates, compares, and prints ratios of a given iteration. Uses global L[], S[], and fullMatrix[]. Returns the index of #             L[] whose equation has the scaled highest ratio.
    def doRatios(self, k):
        ratios = [0 for i in range(len(self.L))]
        currRatio = None
        # 1.) Only finds ratios for the kth equation and on in L[]  (bc equations before that should have already been iterated)
        for index in range(k - 1, len(self.L)):
            eqIndex = self.L[index] - 1
            row = eqIndex
            coeff = self.fullMatrix[row][k - 1]

            currRatio = abs(coeff / self.S[eqIndex])
            ratios[index] = currRatio

        #2.) Find max ratio and save the index of where to find it, identical logic to initalS()
        maxRatio = 0
        indexOfMax = -1
        for index in range(len(ratios)):
            currRatio = ratios[index]
            if currRatio > maxRatio:
                maxRatio = currRatio
                indexOfMax = index

        return indexOfMax


    # Does one iteration given an iter #, uses global L[], fullMatrix[][], numOfVar. Compares coeffs of the pivot equation
    # with the following equations (listed in L[]), find the factor to zero out the correct coeff, factorizes it, then adds.
    # Saves the new coeffs into fullMatrix
    def iteration(self, k):
        # 1.) Obtain pivot row, and pivot's first coeff ( == coeff to compare to all others)
        pivotRow = self.L[k - 1] - 1  # L[k-1] = pivot equation --> l[k-1] - 1 == index of eq we want
        colToZero = k - 1
        pivotCoeff = self.fullMatrix[pivotRow][colToZero]

        # 2.) Loop starts with equation AFTER the pivot eq --> index = k
        for index in range(k, len(self.L)):
            otherEqRow = self.L[index] - 1
            otherCoeff = self.fullMatrix[otherEqRow][colToZero]
            factor = -1 * (otherCoeff / pivotCoeff)

            # 3.) Multiple each term in pivot row/eq , add to corresponding term, then store new coeff
            for col in range(k - 1, self.numOfVar + 1):
                otherTerm = self.fullMatrix[otherEqRow][col]
                pivotTerm = factor * (self.fullMatrix[pivotRow][col])
                newOtherTerm = pivotTerm + otherTerm

                self.fullMatrix[otherEqRow][col] = newOtherTerm


    # uses global L[], coeffMatrix[][], b[], and numOfEq. Method solves for unknown variables backwards given order from L[], store/initalizes global solutions[] in to array and returns it
    def backSub(self):

        # 1.) solutions[] to fill and return it, solvedFor[] to know whether or not has been solved already
        solvedFor = [False for i in range(self.numOfEq)]

        # Loop backwards from last equation stated in L[], in each eq loop from last coeff to first
        # Idea: If solved the variable where coeff is at --> substitute it and move to right side of eq
        #         Otherwise --> variable can be solved for --> divides coeff over to the right to solve variable
        for index in range(len(self.L) - 1, -1, -1):
            eqNumIndex = self.L[index] - 1

            for col in range(self.numOfEq - 1, -1, -1):
                solvedAlready = solvedFor[col]
                coeff = self.coeffMatrix[eqNumIndex][col]

                # if haven't solved it, solve it!
                if not (solvedAlready):
                    self.b[eqNumIndex] = self.b[eqNumIndex] / coeff
                    self.solutions[col] = self.b[eqNumIndex]
                    solvedFor[col] = True
                    break
                # Otherwise: needs to substitute the known variable and move to right side
                else:
                    solvedVar = self.solutions[col]
                    substitute = solvedVar * coeff

                # if Term is positive, need to add its negative, vice versa
                    self.b[eqNumIndex] = (self.b[eqNumIndex] + -1 * substitute)


