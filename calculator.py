import tkinter
from tkinter import *
tk = tkinter.Tk()
#click the numbers and operators in the calculator
def click(numbers):
    global operator
    operator = operator + str(numbers)
    input.set(operator)
#clears the screen
def clear():
    global operator
    operator= ""
    input.set("")
#shows the result
def equal():
    global operator
    result = str(eval(operator))
    input.set(result)
    operator = ""
tk.title("Calculator")
operator = ""
input = StringVar()
display = Entry(tk,textvariable = input, bd = 20, insertwidth = 5, justify = "right").grid(columnspan = 4)
bt15 = Button(tk, bd= 3, padx = 16,  text = "(", width = 1, height = 2, command = lambda:click("(")).grid(column = 0, row = 1)
bt16 = Button(tk, bd= 3, padx = 16,  text = ")", width = 1, height = 2, command = lambda:click(")")).grid(column = 1, row = 1)
bt17 = Button(tk, bd= 3, padx = 16,  text = "%", width = 1, height = 2, command = lambda: click("%")).grid(column = 2, row = 1)
bt18 = Button(tk, bd= 3, padx = 16,  text = "C", width = 1, height = 2, command = lambda:clear()).grid(column = 3, row = 1)
bt1 = Button(tk, bd= 3, padx = 16,  text = "7", width = 1, height = 2, command = lambda:click(7)).grid(column = 0, row = 2)
bt2 = Button(tk, bd= 3, padx = 16,  text = "8", width = 1, height = 2,command = lambda:click(8)).grid(column = 1, row = 2)
bt3 = Button(tk, bd= 3, padx = 16,  text = "9", width = 1, height = 2, command = lambda:click(9)).grid(column = 2, row = 2)
bt1 = Button(tk, bd= 3, padx = 16,  text = "/", width = 1, height = 2, command = lambda:click("/")).grid(column = 3, row = 2)
bt4 = Button(tk, bd= 3, padx = 16,  text = "6", width = 1, height = 2, command = lambda:click(6)).grid(column = 0, row = 3)
bt5 = Button(tk, bd= 3, padx = 16,  text = "5", width = 1, height = 2, command = lambda:click(5)).grid(column = 1, row = 3)
bt6 = Button(tk, bd= 3, padx = 16,  text = "4", width = 1, height = 2, command = lambda:click(4)).grid(column = 2, row = 3)
bt1 = Button(tk, bd= 3, padx = 16,  text = "*", width = 1, height = 2, command = lambda:click("*")).grid(column = 3, row = 3)
bt7 = Button(tk, bd= 3, padx = 16,  text = "3", width = 1, height = 2, command = lambda:click(3)).grid(column = 0, row = 4)
bt8 = Button(tk, bd= 3, padx = 16,  text = "2", width = 1, height = 2, command = lambda:click(2)).grid(column = 1, row = 4)
bt9 = Button(tk, bd= 3, padx = 16,  text = "1", width = 1, height = 2, command = lambda:click(1)).grid(column = 2, row = 4)
bt10 = Button(tk, bd= 3, padx = 16,  text = "-", width = 1, height = 2, command = lambda:click("-")).grid(column = 3, row = 4)
bt11 = Button(tk, bd= 3, padx = 16,  text = "0", width = 1, height = 2, command = lambda:click(0)).grid(column = 0, row = 5)
bt12 = Button(tk, bd= 3, padx = 16,  text = ".", width = 1, height = 2, command = lambda:click(".")).grid(column = 1, row = 5)
bt13 = Button(tk, bd= 3, padx = 16,  text = "=", width = 1, height = 2, command = lambda:equal()).grid(column = 2, row = 5)
bt14 = Button(tk, bd= 3, padx = 16,  text = "+", width = 1, height = 2, command = lambda:click("+")).grid(column = 3, row = 5)
tk.mainloop()