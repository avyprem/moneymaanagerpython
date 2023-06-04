import tkinter
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
import os

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              vvv                  FUNCTIONS                 vvv                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

def number():
    # Check if income contains letters or symbols, only accepts numbers (1,2,3, etc (also accepts decimals))
    try:
        float(monthly_income.get())
        confirmation_label.config(text='confirmed')
        confirm_btn['state'] = 'disabled'
        monthly_income['state'] = 'disabled'
    except ValueError:
        tkinter.messagebox.showwarning(title = '!WARNING!', message = 'We seemed to have detected a letter, or symbol in the text box. Please try again')
        confirmation_label.config(text='not confirmed')

def next_frame(frame):
    # Changes frames
    frame.tkraise()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              ^^^                  FUNCTIONS                 ^^^                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

window = tkinter.Tk()
window.geometry("487x318")
window.resizable(0,0)
window.title("Wealth Garden")

#scroll_bar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview) 

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              vvv                FRAME SWITCH                vvv                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

frame1 = tkinter.Frame(window)
frame2 = tkinter.Frame(window)


for frame in(frame1,frame2):
    frame.grid(row=0,column=0,sticky='nsew')
next_frame(frame1)
# Saving User Info
user_info_frame =tkinter.LabelFrame(frame1, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              ^^^                FRAME SWITCH                ^^^                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              vvv           FRONT PAGE INFORMATION           vvv                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=0, column=2)
age_spinbox.grid(row=1, column=2)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Frame for income input & confirmation
income = tkinter.LabelFrame(frame1, text="Monthly Income")
income.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Label within the frame, emphasizing the entry box purpose
income_label = tkinter.Label(income, text= "Monthly Income After Taxes  (do not include: $)")
income_label.grid(row=0,column=0)

# Entry box to input income
monthly_income = tkinter.Entry(income)
monthly_income.grid(row=1,column=0)

# Button to confirm income
confirm_btn = tkinter.Button(income, text='Confirm Income', command=number)
confirm_btn.grid(row=1,column=1)

# Confirmation Label
confirmation_label = tkinter.Label(income,text='not confirmed')
confirmation_label.grid(row=2,column=1)

next_page = tkinter.LabelFrame(frame1, text="Next")
next_page.grid(row= 2, column=0, sticky="news", padx=20, pady=10)

next_btn = tkinter.Button(next_page, text='Next >',command=lambda:next_frame(frame2),)
next_btn.grid(row=0, column=0, padx=5,pady=5)

welcome = tkinter.LabelFrame(frame2, text="Wealth Garden")
welcome.grid(row= 0, column=0, padx=20, pady=10)
font_obj = tkFont.Font(family='Calibri', size=10)
msg = tkinter.Label(welcome, font=font_obj, text="Welcome, name, to Wealth Garden, The best \nplace to organize, and start to grow your wealth, \nlike a garden. The first steps is to fill out this \nshort quiz and get your organized data to start \nspending wisely")
msg.grid(row=0, column=0, padx = 84)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              ^^^           FRONT PAGE INFORMATION           ^^^                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              vvv                  QUESTIONS                 vvv                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

# Question 1 ...............................................................................

Expenses = tkinter.LabelFrame(frame2, text="Expenses (6):")
Expenses.grid(row= 1, column=0, padx=20, pady=10)
help_note = tkinter.Label(Expenses, text="(input '0' if at any point a question is not applicable to you.)")
help_note.grid(row=0, column=0)

Q1_label = tkinter.Label(Expenses, text="(1) How Much Do You Spend on Mortgage/Rent?",)
Q1_label.grid(row=1, column=0, padx=91, pady=10)
Q1_entry = tkinter.Entry(Expenses)
Q1_entry.grid(row=2, column=0,pady=15)

# Question 2 ...............................................................................

Q2_label = tkinter.Label(Expenses, text="(2) How Much Do You Spend on ALL your current Insurances plans?\n(Dental Insurance, Life Insurance, Auto Insurance, etc.)",)
Q2_label.grid(row=3, column=0)
Q2_entry = tkinter.Entry(Expenses)
Q2_entry.grid(row=4, column=0,pady=15)

# Question 3 ...............................................................................

Q3_label = tkinter.Label(Expenses, text="(3) How Much Do You Spend on Communications?\n(WiFi, Internet, Phone Services)",)
Q3_label.grid(row=5, column=0)
Q3_entry = tkinter.Entry(Expenses)
Q3_entry.grid(row=6, column=0,pady=15)

# Question 4 ...............................................................................

Q4_label = tkinter.Label(Expenses, text="(4) How Much Do You Spend on Car Payments?\n(Repairs, Gas, Car Installments)",)
Q4_label.grid(row=7, column=0)
Q4_entry = tkinter.Entry(Expenses)
Q4_entry.grid(row=8, column=0,pady=15)

# Question 5 ...............................................................................

Q5_label = tkinter.Label(Expenses, text="(5) How Much Do You Spend on Education?\n(OSAP, University, College)",)
Q5_label.grid(row=9, column=0)
Q5_entry = tkinter.Entry(Expenses)
Q5_entry.grid(row=10, column=0,pady=15)

# Question 6 ...............................................................................

Q6_label = tkinter.Label(Expenses, text="(6) How Much Debt Do You Currently Have?",)
Q6_label.grid(row=11, column=0)
Q6_entry = tkinter.Entry(Expenses)
Q6_entry.grid(row=12, column=0,pady=15)

# Question 7 ...............................................................................

Saving = tkinter.LabelFrame(frame2, text="Saving (2):")
Saving.grid(row= 2, column=0, padx=20, pady=10)

Q7_label = tkinter.Label(Saving, text="(7) How Much Would You Like To Start, Or Are Already Currently Saving?",)
Q7_label.grid(row=1, column=0, padx=33, pady=10)

Q7_list = ["5%" , "15%" , "20%" , "25%"]
Q7_entry = ttk.Combobox(Saving, values = Q7_list)
Q7_entry.grid(row=2, column=0,pady=15)

# Question 8 ...............................................................................

Q8_label = tkinter.Label(Saving, text="(8) How Much Would You Like To Start, Or Are Already Currently Investing?",)
Q8_label.grid(row=3, column=0)
Q8_entry = tkinter.Entry(Saving)
Q8_entry.grid(row=4, column=0,pady=15)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              ^^^                  QUESTIONS                 ^^^                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

for widget in income.winfo_children():
    widget.grid_configure(padx=10, pady=5)

 
window.mainloop()
