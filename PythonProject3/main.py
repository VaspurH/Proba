from tkinter import  *
from tkinter import  ttk
import calculator_login as c

oper = ''
first = 0
second = 0
result = 0


def calc():
    second = float(entry.get())
    if oper == '+':
        result = c.add(first, second)
    elif oper == '-':
        result = c.subtract(first, second)
    elif oper == '*':
        result = c.multiply(first, second)
    elif oper == '/':
        result = c.divide(first, second)
    elif oper == '**':
        result = c.square(first)                 #добавлено функцию square(x)
    entry.delete(0, END)
    entry.insert(0, str(result))


def calculate_square():
    num = float(entry.get())
    result = c.square(num)
    entry.delete(0, END)
    entry.insert(0, str(result))

def enter_number(number):
    entry.insert(END, number)

def clear_entry():
     entry.delete(0, END)


def set_operation(operetion):
    global first
    global oper
    first = float(entry.get())
    oper = operetion
    entry.delete(0, END)


def validate_entry():
    e = entry.get()
    txt = ''.join(b for b in e if b  in "0123456789.-")
    if e != txt:
        entry.delete(0, END)
        entry.insert(0, txt)

window = Tk()
window.title("Калькулятор")

entry = ttk.Entry()
entry.grid(row=0, column=0, columnspan=4, sticky='ew')
entry.bind('<KeyRelease>', lambda event: validate_entry())

ttk.Button(text="1", command=lambda: enter_number('1')).grid(row=1, column=0)
ttk.Button(text="2", command=lambda: enter_number('2')).grid(row=1, column=1)
ttk.Button(text="3", command=lambda: enter_number('3')).grid(row=1, column=2)
ttk.Button(text="4", command=lambda: enter_number('4')).grid(row=2, column=0)
ttk.Button(text="5", command=lambda: enter_number('5')).grid(row=2, column=1)
ttk.Button(text="6", command=lambda: enter_number('6')).grid(row=2, column=2)
ttk.Button(text="7", command=lambda: enter_number('7')).grid(row=3, column=0)
ttk.Button(text="8", command=lambda: enter_number('8')).grid(row=3, column=1)
ttk.Button(text="9", command=lambda: enter_number('9')).grid(row=3, column=2)
ttk.Button(text="0", command=lambda: enter_number('0')).grid(row=4, column=0)

ttk.Button(text="C", command=clear_entry).grid(row=4, column=1)
ttk.Button(text="=", command=calc).grid(row=4, column=2)

ttk.Button(text="+", command=lambda: set_operation('+')).grid(row=1, column=3)
ttk.Button(text="-", command=lambda: set_operation('-')).grid(row=2, column=3)
ttk.Button(text="*", command=lambda: set_operation('*')).grid(row=3, column=3)
ttk.Button(text="/", command=lambda: set_operation('/')).grid(row=4, column=3)

window.mainloop()
