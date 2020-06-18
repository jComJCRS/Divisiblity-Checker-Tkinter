try:
    import Tkinter as tk
except:
    import tkinter as tk
import time

rownum = 100

def disptext(text):
    global rownum
    Text = tk.Label(dc, text=text, font=("Montserrat", 10), bg='yellow', fg = 'blue')
    Text.grid(row=rownum, column=0, sticky="W")
    rownum = rownum - 1

def ButtonCode1():

    numlist = []
    result1 = "Divisible by "
    Value1 = CheckBox.get()
    try:
        Value1 = int(Value1)
    except:
        disptext("Not a numeral\n")
    for i in range(1, Value1 + 1):
        if Value1 % i == 0:
            numlist.append(i)
            result1 = result1 + str(i) + ","
    result1 = result1 + "."


    if len(numlist) > 2:
        prime = str(Value1) + " is a Composite Number\n"
    else:
        prime = str(Value1) + " is a Prime Number\n"
    CheckBox.delete(0, Value1+1)

    CheckButton.configure(text="Check")

    disptext(prime)
    disptext(result1)





dc = tk.Tk()
dc.configure(bg = 'yellow')
dc.geometry('1280x500')
dc.title("Divisiblity Checker")
icon = tk.PhotoImage(file = "icon.png")
dc.iconphoto(False, icon)
CheckBox = tk.Entry(dc, width = 110, bg = "yellow", fg = "blue", font = "Montserrat")
CheckBox.grid(row = 0, column = 0)
CheckButton = tk.Button(dc, text = "Check", font = ("Montserrat Extrabold", 9), bg = "blue", fg = "yellow", padx = 10, pady = 0.5, command = ButtonCode1)
CheckButton.grid(row = 0, column = 1)

dc.mainloop()


