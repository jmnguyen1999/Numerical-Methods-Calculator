from tkinter import *
from SolveEquations import SolveEquations
from Interpolation import Interpolation
from FindRoots import FindRoots
import sys

root = Tk()

root.title("Numerical Methods Calculator")

welcomeMessage = Label(root,
                       text="Welcome! Are you ready to solve some numerical methods? Please choose from the drop down menu above.")
welcomeMessage.grid(row=0, column=0, pady=20, columnspan=3)

XYEntries = []


def linear():
    top = Toplevel()
    top.title('Solve Linear Equation')
    instructions = Label(top,
                         text="Please enter the coefficients for each variable. If coefficient isn't entered it will be assumed to be 0.")
    instructions.grid(row=0, column=0)

    equation1x = Entry(top)
    equation1x.grid(row=1, column=0)
    xLabel1 = Label(top, text="x")
    xLabel1.grid(row=1, column=1)
    equation1y = Entry(top)
    equation1y.grid(row=1, column=2)
    yLabel1 = Label(top, text="y")
    yLabel1.grid(row=1, column=3)
    equation1z = Entry(top)
    equation1z.grid(row=1, column=4)
    zLabel1 = Label(top, text="z")
    zLabel1.grid(row=1, column=5)

    equation2x = Entry(top)
    equation2x.grid(row=2, column=0)
    xLabel2 = Label(top, text="x")
    xLabel2.grid(row=2, column=1)
    equation2y = Entry(top)
    equation2y.grid(row=2, column=2)
    yLabel2 = Label(top, text="y")
    yLabel2.grid(row=2, column=3)
    equation2z = Entry(top)
    equation2z.grid(row=2, column=4)
    zLabel2 = Label(top, text="z")
    zLabel2.grid(row=2, column=5)

    equation3x = Entry(top)
    equation3x.grid(row=3, column=0)
    xLabel3 = Label(top, text="x")
    xLabel3.grid(row=3, column=1)
    equation3y = Entry(top)
    equation3y.grid(row=3, column=2)
    yLabel3 = Label(top, text="y")
    yLabel3.grid(row=3, column=3)
    equation3z = Entry(top)
    equation3z.grid(row=3, column=4)
    zLabel3 = Label(top, text="z")
    zLabel3.grid(row=3, column=5)

    solveButton = Button(top, text="Solve", command=solveButton2)
    solveButton.grid(row=4, column=0, pady=5, columnspan=5)

    top.mainloop()


def polynomial():
    global leadCoeff, coeff2, coeff3, coeff4, coeff5, a, b, degree
    third = Toplevel()
    third.title('Solve Polynomial Roots')

    enterDegreeLabel = Label(third, text="Enter the degree of the polynomial up to 4: ")
    enterDegreeLabel.grid(row=0, column=0)
    degree = Entry(third)
    degree.grid(row=0, column=1)

    enterLabel = Label(third, text="Enter polynomial's coefficients: ", padx=20, pady=20)
    enterLabel.grid(row=1, column=0)

    leadCoeff = Entry(third)
    leadCoeff.grid(row=1, column=1)
    label4Degree = Label(third, text="x^4")
    label4Degree.grid(row=1, column=2, padx = 10)
    coeff2 = Entry(third)
    coeff2.grid(row=1, column=3)
    label3Degree = Label(third, text="x^3")
    label3Degree.grid(row=1, column=4, padx = 10)
    coeff3 = Entry(third)
    coeff3.grid(row=1, column=5, padx = 5)
    label2Degree = Label(third, text="x^2")
    label2Degree.grid(row=1, column=6, padx = 10)
    coeff4 = Entry(third)
    coeff4.grid(row=1, column=7, padx = 5)
    label1Degree = Label(third, text="x")
    label1Degree.grid(row=1, column=8, padx = 10)
    coeff5 = Entry(third)
    coeff5.grid(row=1, column=9, padx = 5)

    labelFirstPoint = Label(third, text="Enter the starting guess A: ")
    labelFirstPoint.grid(row=2, column=0, padx = 10)
    a = Entry(third)
    a.grid(row=2, column=1, padx = 5)
    labelFirstPoint = Label(third, text="Enter the starting guess B: ")
    labelFirstPoint.grid(row=3, column=0, padx=10)
    b = Entry(third)
    b.grid(row=3, column=1, padx=5)

    solveButton = Button(third, text="Find Roots", command=solveButton3)
    solveButton.grid(row=3, column=0, pady=20, columnspan=9)

    third.mainloop()


def solveButton3(*args):
    global leadCoeff, coeff2, coeff3, coeff4, coeff5, a, b, degree

    degree = int(degree.get())
    leadCoeff = int(leadCoeff.get())
    coeff2 = int(coeff2.get())
    coeff3 = int(coeff3.get())
    coeff4 = int(coeff4.get())
    coeff5 = int(coeff5.get())
    a = int(a.get())
    b = int(b.get())

    polyArray = []

    polyArray.append(leadCoeff)
    polyArray.append(coeff2)
    polyArray.append(coeff3)
    polyArray.append(coeff4)
    polyArray.append(coeff5)

    findRoots = FindRoots(polyArray, a, b, degree)
    root = findRoots.execute()
    print("The root of the function is: ")
    print(root)

def interpolation():
    global x1
    global x2
    global x3
    global y1
    global y2
    global y3
    global x4
    second = Toplevel()
    second.title('Solve Interpolation')
    instructions = Label(second,
                         text="Please fill in three (x,y) values, and give the x-value you wish to find the corresponding y-value for. Then click the solve button.")

    #All of these are just formatting the entry boxes
    xLabel = Label(second, text="x")
    xLabel.grid(row=1, column=0, columnspan=3)

    x1 = Entry(second)

    x1.grid(row=2, column=0, columnspan=3, pady=1)
    x2 = Entry(second)
    x2.grid(row=3, column=0, columnspan=3, pady=1)
    x3 = Entry(second)
    x3.grid(row=4, column=0, columnspan=3, pady=1)

    yLabel = Label(second, text="y")
    yLabel.grid(row=1, column=1, columnspan=3)

    y1 = Entry(second)
    y1.grid(row=2, column=1, columnspan=3, pady=1)
    y2 = Entry(second)
    y2.grid(row=3, column=1, columnspan=3, pady=1)
    y3 = Entry(second)
    y3.grid(row=4, column=1, columnspan=3, pady=1)

    ysolve = Label(second, text="Please enter the x value that you want the corresponding y value for.")
    ysolve.grid(row=5, column=0, pady=20, columnspan=3)
    x4 = Entry(second)
    x4.grid(row=6, column=0, columnspan=3, pady=1)

    myButton = Button(second, text="Solve", command=solveButton, fg="black")
    myButton.grid(row=7, column=0, pady=5, columnspan=3)

    clearButton = Button(second, text="Clear", fg="black", command=buttonClear)
    clearButton.grid(row=9, column=0, pady=5, columnspan=3)

    second.mainloop()


def buttonClear():
    x1.delete(0, END)
    x2.delete(0, END)
    x3.delete(0, END)
    y1.delete(0, END)
    y2.delete(0, END)
    y3.delete(0, END)
    x4.delete(0, END)


def solveButton(*args):
    global n
    global xs
    global ys
    global cs
    global result
    stringInput = x1.get()
    intAnswer = int(stringInput)
    stringInput2 = x2.get()
    intAnswer2 = int(stringInput2)
    stringInput3 = x3.get()
    intAnswer3 = int(stringInput3)
    stringInput4 = x4.get()
    intAnswer4 = int(stringInput4)
    stringInput5 = y1.get()
    intAnswer5 = int(stringInput5)
    stringInput6 = y2.get()
    intAnswer6 = int(stringInput6)
    stringInput7 = y3.get()
    intAnswer7 = int(stringInput7)
    n = 2
    xs = []
    ys = []
    cs = []
    xs.append(intAnswer)
    xs.append(intAnswer2)
    xs.append(intAnswer3)
    ys.append(intAnswer5)
    ys.append(intAnswer6)
    ys.append(intAnswer7)
  #  coeff(xs, ys, cs, n)

    #result = test.execute() #evalnewton(xs, cs, intAnswer4, n)
    i = Interpolation(xs, ys, cs, n, intAnswer4)
    result = i.execute()
    print(result)


menu = Menu(root)
root.config(menu=menu)

equationMenu = Menu(menu)
menu.add_cascade(label="Choose Numerical Method", menu=equationMenu)
equationMenu.add_command(label="Solve Linear Equations", command=linear)
equationMenu.add_command(label="Solve Interpolation", command=interpolation)
equationMenu.add_command(label="Solve Polynomial Roots", command=polynomial)

root.mainloop()