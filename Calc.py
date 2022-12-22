## Chinmay D. 12/20/2022 Hg5590
from tkinter import *
# Imports tkinter into the program
x = ""
# declares the expression variable
def tap(i):
# Creates and names a function for action upon clicking buttons
    global x
    x = x + str(i)
    calculate.set(x)
# Sets up a variable and updates the expression then concatenates string 
def solver():
# Creates and names function which evaluates the expression problem
    try: 
        global x
        final = str(eval(x)) 
        calculate.set(final)
        x = ""
    except:
        calculate.set(" error ")
        x = ""
# Sets up empty string to initialize expression variable
def clear():
# Creates and names function to delete and clear search memory inputs or outputs
    global x
    x = ""
    calculate.set("")
if __name__ == "__main__":
    box = Tk()
    box.configure(background="blue")
    box.title("Calculator")
# Names the calculator graphical user interface 
    box.geometry("300x250")
# Creates and configures the main application window 
    calculate = StringVar()
    math = Entry(box, textvariable=calculate)
# Sets up a way to enter string input and recieve output
    math.grid(columnspan=4, ipadx=90)
# Configures the column and row sizes
    equal = Button(box, text=' = ', fg='black', bg='yellow',
                command=solver, height=2, width=5)
    equal.grid(row=4, column=3)
    clear = Button(box, text='Clear', fg='black', bg='yellow',
                command=clear, height=2, width=5)
    clear.grid(row=2, column='3')
    decimal= Button(box, text='.', fg='black', bg='yellow',
                    command=lambda: tap('.'), height=2, width=5)
    decimal.grid(row=3, column=3) 
# Creates and configures buttons for clearing/solving/inserting decimal in expression 
    concentate = Button(box, text=' + ', fg='black', bg='yellow',
                command=lambda: tap("+"), height=2, width=5)
    concentate.grid(row=6, column=0)
    minus = Button(box, text=' - ', fg='black', bg='yellow',
                command=lambda: tap("-"), height=2, width=5)
    minus.grid(row=6, column=1)
    multiply = Button(box, text=' * ', fg='black', bg='yellow',
                    command=lambda: tap("*"), height=2, width=5)
    multiply.grid(row=6, column=2)
    divide = Button(box, text=' / ', fg='black', bg='yellow',
                    command=lambda: tap("/"), height=2, width=5)
    divide.grid(row=6, column=3)
# Creates and configures buttons to add/subtract/multiply/divide the expression
    one = Button(box, text=' 1 ', fg='black', bg='yellow',
                    command=lambda: tap(1), height=2, width=5)
    one.grid(row=2, column=0) 
    two = Button(box, text=' 2 ', fg='black', bg='yellow',
                    command=lambda: tap(2), height=2, width=5)
    two.grid(row=2, column=1)
    three = Button(box, text=' 3 ', fg='black', bg='yellow',
                    command=lambda: tap(3), height=2, width=5)
    three.grid(row=2, column=2)
    four = Button(box, text=' 4 ', fg='black', bg='yellow',
                    command=lambda: tap(4), height=2, width=5)
    four.grid(row=3, column=0)
    five = Button(box, text=' 5 ', fg='black', bg='yellow',
                    command=lambda: tap(5), height=2, width=5)
    five.grid(row=3, column=1)
    six = Button(box, text=' 6 ', fg='black', bg='yellow',
                    command=lambda: tap(6), height=2, width=5)
    six.grid(row=3, column=2)
    seven = Button(box, text=' 7 ', fg='black', bg='yellow',
                    command=lambda: tap(7), height=2, width=5)
    seven.grid(row=4, column=0)
    eight = Button(box, text=' 8 ', fg='black', bg='yellow',
                    command=lambda: tap(8), height=2, width=5)
    eight.grid(row=4, column=1)
    nine = Button(box, text=' 9 ', fg='black', bg='yellow',
                    command=lambda: tap(9), height=2, width=5)
    nine.grid(row=4, column=2)
    zero = Button(box, text=' 0 ', fg='black', bg='yellow',
                    command=lambda: tap(0), height=2, width=5)
    zero.grid(row=5, column=1)
# Creates and configures a button for the numbers 0,1,2,3,4,5,6,7,8 & 9
    box.mainloop()
# Packs and loops elements of window and boots up GUI tkinter calculator
# CSC 1500, Section 902, Final Exam