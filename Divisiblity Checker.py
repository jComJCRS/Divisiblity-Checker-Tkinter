try:
    import Tkinter as tk
except:
    import tkinter as tk
import time

rownum = 10000
expand = False

def disptext(text):
    global rownum
    Text = tk.Label(dc, text=text, font=("Calibri", 10))
    Text.grid(row=rownum, column=0, sticky="W")
    rownum = rownum - 1

def ButtonCode1():

    numlist = []
    result1 = "Divisible by "
    Value1 = CheckBox.get()
    try:
        Value1 = int(Value1)
        for i in range(1, Value1 + 1):
            if Value1 % i == 0:
                numlist.append(i)
                result1 = result1 + str(i) + ","
        result1 = result1 + "."

        if len(numlist) > 2:
            prime = str(Value1) + " is a Composite Number\n"
        else:
            prime = str(Value1) + " is a Prime Number\n"
        CheckBox.delete(0, Value1 + 1)

        disptext(prime)
        disptext(result1)

    except:
        disptext("Not a numeral")

def expand():
    CheckBox.configure(width=110)
def shortern():
    CheckBox.configure(width=40)



dc = tk.Tk()
dc.title("Divisiblity Checker")
dc.resizable(False, False)
icon = tk.PhotoImage(file="icon.png")
dc.iconphoto(False, icon)
CheckBox = tk.Entry(dc, width=40, font="Calibri")
CheckBox.grid(row=0, column=0)
CheckButton = tk.Button(dc, text="↳", font=("Calibri", 10), padx=10, pady=0.5, command=ButtonCode1)
CheckButton.grid(row=0, column=1)
Expand = tk.Button(dc, text="E", font=("Calibri", 10), command=expand)
Expand.grid(row=0, column=2)
Shortern = tk.Button(dc, text="S", font=("Calibri", 10), command=shortern)
Shortern.grid(row=0, column=3)
dc.mainloop()
