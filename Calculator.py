from tkinter import *

#_____________________Global Variables__________________#

first_value = None
second_value = None
operator = None
text = ["", "Error", "Cannot Divide by Zero", "Please enter your calculation", 'Requires a number first!']
button_bg = '#FDFDFD'
button_fg = 'black'


#_________________________Functions_____________________#

def validate(nums):
    if nums in ("", "-", ".", "-.") or nums in text:
        return True
    try:
        float(nums)
        return True
    except ValueError:
        return False


def placeholder(event=None):
    if entry.get() in text:
        clear()


def number(nums):
    placeholder()
    nums = int(nums)
    entry.insert(END, nums)


def no_decimal(nums):
    nums = str(nums)
    end = len(nums)
    if end >= 3:
        if nums[end - 2] == "." and nums[end - 1] == "0":
            return int(nums[0:end - 2])
    return float(nums)


def negative():
    placeholder()
    if len(entry.get()) == 0 or entry.get()[0] != '-':
        entry.insert(0, '-')
    else:
        entry.delete(0, 1)


def root():
    try:
        placeholder()
        global operator, first_value
        first_value = float(entry.get())
        clear()
        operator = '√'
    except ValueError:
        print('Requires a number first')

def square():
    try:
        placeholder()
        global operator, first_value
        first_value = float(entry.get())
        clear()
        operator = '^'
    except ValueError:
        print('Requires a number first')


def add():
    try:
        placeholder()
        global operator, first_value
        first_value = float(entry.get())
        clear()
        operator = '+'
    except ValueError:
        print('Requires a number first')


def sub():
    try:
        placeholder()
        global operator, first_value
        first_value = float(entry.get())
        clear()
        operator = '-'
    except ValueError:
        print('Requires a number first')


def mul():
    try:
        placeholder()
        global operator, first_value
        first_value = float(entry.get())
        clear()
        operator = '*'
    except ValueError:
        print('Requires a number first')

def div():
    try:
        placeholder()
        global operator, first_value
        first_value = float(entry.get())
        clear()
        operator = '/'
    except ValueError:
        print('Requires a number first')


def equal():
    try:
        global first_value, second_value, operator
        second_value = float(entry.get())
        match operator:
            case '^':
                first_value = pow(float(first_value), float(second_value))
                second_value = None
                clear()
                entry.insert(END, no_decimal(first_value))
                operator = None
            case '√':
                first_value = pow(float(second_value), float(1 / first_value))
                second_value = None
                clear()
                entry.insert(END, no_decimal(first_value))
                operator = None
            case '+':
                first_value = float(first_value + second_value)
                second_value = None
                clear()
                entry.insert(END, no_decimal(first_value))
                operator = None
            case '-':
                first_value = float(first_value - second_value)
                second_value = None
                clear()
                entry.insert(END, no_decimal(first_value))
                operator = None
            case '*':
                first_value = float(first_value * second_value)
                second_value = None
                clear()
                entry.insert(END, no_decimal(first_value))
                operator = None
            case '/':
                first_value = float(first_value / second_value)
                second_value = None
                clear()
                entry.insert(END, no_decimal(first_value))
                operator = None

    except ValueError:
        clear()
        entry.insert(0, "Error")
        print("Error")
    except ZeroDivisionError:
        clear()
        entry.insert(0, "Cannot Divide by Zero")
        print("Cannot Divide by Zero")
    except E:
        clear()
        entry.insert(0, "Unknown Error")
        print("Unknown Error")


def clear():
    entry.delete(0, END)


def delete():
    x = len(entry.get()) - 1
    entry.delete(x)


#__________________________ GUI_________________________#

window = Tk()

window.title('Calculator')
window.geometry('300x350')

frame = Frame(window)
frame.pack(fill=BOTH, expand=True)

entry = Entry(frame, font=('Arial', 14), bg='black', fg='white')
entry.pack(side=TOP, fill=BOTH, expand=True, ipady=10)

#-------------------------------First Frame----------------------------------------

frame = Frame(window)
frame.pack(fill=BOTH, expand=True)

# Width turned to 1 to ensure same size regardless of text size
button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, text='Clear', width=1,
                command=lambda: entry.delete(0, END))
button.pack(side=LEFT, fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, text='Delete', width=1, command=delete)
button.pack(side=LEFT, fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, text=str("(-)"), width=1, command=negative)
button.pack(side=LEFT, fill=BOTH, expand=True)

#----------------------------------Second Frame--------------------------------

frame = Frame(window)
frame.pack(fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, width=1, text="^", command=square)
button.pack(side=LEFT, fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, width=1, text="√", command=root)
button.pack(side=LEFT, fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, width=1, text='+', command=add)
button.pack(side=LEFT, fill=BOTH, expand=True)

#----------------------------------Third Frame--------------------------------

frame = Frame(window)
frame.pack(fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, width=1, text='-', command=sub)
button.pack(side=LEFT, fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, width=1, text='*', command=mul)
button.pack(side=LEFT, fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, width=1, text='/', command=div)
button.pack(side=LEFT, fill=BOTH, expand=True)

#------------------------------------Fourth Frame------------------------------


for i in range(1, 10):
    if (i - 1) % 3 == 0:
        frame = Frame(window)
        frame.pack(fill=BOTH, expand=True)
    button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg,
                    command=lambda num=i: number(num), text=str(i))
    button.pack(side=LEFT, fill=BOTH, expand=True)

#------------------------------------Fifth Frame------------------------------

frame = Frame(window)
frame.pack(fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, text='.', width=1,
                command=lambda: entry.insert(END, '.'))
button.pack(side=LEFT, fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg,
                command=lambda num=0: entry.insert(END, float(num)), width=1, text=str(0))
button.pack(side=LEFT, fill=BOTH, expand=True)

button = Button(frame, font=('Arial', 14), bg=button_bg, fg=button_fg, text='Equal', width=1, command=equal)
button.pack(side=LEFT, fill=BOTH, expand=True)

#----------------------------------End of GUI------------------------------------------
place = "Please enter your calculation"
entry.insert(0, place)

# Key Validation to ensure no character are typed
validates = (window.register(validate), '%P')
entry.config(validate='key', validatecommand=validates)

# Remove placeholder or error messages when number or operation are typed
entry.bind('<FocusIn>', placeholder)
entry.bind('<Button>', placeholder)

window.mainloop()
