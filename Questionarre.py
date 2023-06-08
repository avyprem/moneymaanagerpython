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

def empty_check():
  try:
    if confirmation_label['text'] != 'confirmed':
      tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Confirm Your Monthly Income After Taxes.')
    #elif confirmation_label['text'] == 'confirmed':
    elif int(age_spinbox.get()) < 18 or int(age_spinbox.get()) > 110:
      tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Enter A Valid Age.')
    elif len(age_spinbox.get()) > 3:
        tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Enter A Valid Age.')
    elif first_name_entry.get() and last_name_entry.get() != "":
      next_frame(frame2)
    else:
      tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Fill All Required Fields')
  except ValueError:
    tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Enter A Valid Age.')

  
def field_check():
  try:
    if float(Q1_entry.get()) == '':
      tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Enter All Required Fields!')
    elif float(Q2_entry.get()) == '':
      tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Enter All Required Fields!')
    elif float(Q3_entry.get()) == '':
      tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Enter All Required Fields!')
    elif float(Q4_entry.get()) == '':
      tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Enter All Required Fields!')
    elif float(Q5_entry.get()) == '':
      tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Enter All Required Fields!')
    elif float(Q6_entry.get()) == '':
      tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Enter All Required Fields!')
    else:
      next_frame(frame3)
  except ValueError:
    tkinter.messagebox.showwarning(title = '!WARNING!', message = 'Please Do Not Use Any Letters or Special Characters!')

def data():
  data = [Q1_entry.get(), Q2_entry.get(), Q2_entry.get(), Q3_entry.get(), Q4_entry.get(), Q5_entry.get(), Q6_entry.get(), Q7_entry.get(), Q8_entry.get(), Q9_entry.get(), Q10_entry.get(), Q11_entry.get(), Q12_entry.get()]
  print(data)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              ^^^                  FUNCTIONS                 ^^^                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

window = tkinter.Tk()
window.geometry("620x735")
window.resizable(0,0)
window.title("Wealth Garden")



#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              vvv                FRAME SWITCH                vvv                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

frame1 = tkinter.Frame(window)
frame2 = tkinter.Frame(window)
frame3 = tkinter.Frame(window)



for frame in(frame1,frame2,frame3):
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

first_name_label = tkinter.Label(user_info_frame, text="First Name *")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name *")
last_name_label.grid(row=0, column=1)
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

age_label = tkinter.Label(user_info_frame, text="Age *")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=0, column=2)
age_spinbox.grid(row=1, column=2)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Frame for income input & confirmation
income = tkinter.LabelFrame(frame1, text="Monthly Income")
income.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Label within the frame, emphasizing the entry box purpose
income_label = tkinter.Label(income, text= "Monthly Income After Taxes  (do not include: $) *")
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
    
  

next_btn = tkinter.Button(next_page, text='Next >',command=lambda:empty_check())
next_btn.grid(row=0, column=0, padx=5,pady=5)


welcome = tkinter.LabelFrame(frame2, text="Wealth Garden")
welcome.grid(row= 0, column=0, padx=20, pady=10)
font_obj = tkFont.Font(family='Calibri', size=10)
msg = tkinter.Label(welcome, font=font_obj, text="Welcome name to Wealth Garden, The best \nplace to organize, and start to grow your wealth, \nlike a garden. The first steps is to fill out this \nshort quiz and get your organized data to start \nspending wisely")
msg.grid(row=0, column=0, padx = 121)

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
Q1_entry = tkinter.Entry(Expenses)

Q1_label.grid(row=1, column=0, padx=91, pady=10)
Q1_entry.grid(row=2, column=0,pady=15)

# Question 2 ...............................................................................

Q2_label = tkinter.Label(Expenses, text="(2) How Much Do You Spend on ALL your current Insurances plans?\n(Dental Insurance, Life Insurance, Auto Insurance, etc.)",)
Q2_entry = tkinter.Entry(Expenses)

Q2_label.grid(row=3, column=0, padx=79)
Q2_entry.grid(row=4, column=0,pady=15)

# Question 3 ...............................................................................

Q3_label = tkinter.Label(Expenses, text="(3) How Much Do You Spend on Communications?\n(WiFi, Internet, Phone Services)",)
Q3_entry = tkinter.Entry(Expenses)

Q3_label.grid(row=5, column=0)
Q3_entry.grid(row=6, column=0,pady=15)

# Question 4 ...............................................................................

Q4_label = tkinter.Label(Expenses, text="(4) How Much Do You Spend on Car Payments?\n(Repairs, Gas, Car Installments)",)
Q4_entry = tkinter.Entry(Expenses)

Q4_label.grid(row=7, column=0)
Q4_entry.grid(row=8, column=0,pady=15)

# Question 5 ...............................................................................

Q5_label = tkinter.Label(Expenses, text="(5) How Much Do You Spend on Education?\n(OSAP, University, College)",)
Q5_entry = tkinter.Entry(Expenses)

Q5_label.grid(row=9, column=0)
Q5_entry.grid(row=10, column=0,pady=15)

# Question 6 ...............................................................................

Q6_label = tkinter.Label(Expenses, text="(6) How Much Debt Do You Currently Have?",)
Q6_entry = tkinter.Entry(Expenses)
next_btn2 = tkinter.Button(frame2, text='Next >',command=lambda:field_check())


Q6_label.grid(row=11, column=0)
Q6_entry.grid(row=12, column=0,pady=15)
next_btn2.grid(row=2, column=0)



# Question 7 ...............................................................................

Saving = tkinter.LabelFrame(frame3, text="Saving (2):")
Q7_list = ["5%" , "15%" , "20%" , "25%"]
Q7_label = tkinter.Label(Saving, text="(7) How Much Would You Like To Start, Or Are Already Currently Saving?")
Q7_entry = ttk.Combobox(Saving, values = Q7_list)

Saving.grid(row= 1, column=0, padx=20, pady=10)
Q7_label.grid(row=1, column=0, padx=33, pady=10)
Q7_entry.grid(row=2, column=0,pady=15)

# Question 8 ...............................................................................

Q8_label = tkinter.Label(Saving, text="(8) How Much Would You Like To Start, Or Are Already Currently Investing? (Higher Incomes)")
Q8_entry = tkinter.Entry(Saving)

Q8_label.grid(row=3, column=0, padx=2)
Q8_entry.grid(row=4, column=0,pady=15)

# Question 9 ...............................................................................

personal = tkinter.LabelFrame(frame3, text="Personal Expenses (3):")

Q9_label = tkinter.Label(personal, text="(9) How Much Do You Spend on Clothing?")
Q9_entry = tkinter.Entry(personal)

personal.grid(row= 2, column=0, padx=10, pady=10)
Q9_label.grid(row=1, column=0, padx=33, pady=10)
Q9_entry.grid(row=2, column=0,pady=15)

# Question 10 ...............................................................................

Q10_label = tkinter.Label(personal, text="(10) How Much Do You Spend on Personal Care? (Haircuts, Cosmetics, Skin Care, Travel)")
Q10_entry = tkinter.Entry(personal)


Q10_label.grid(row=3, column=0, padx=16, pady=11)
Q10_entry.grid(row=4, column=0,pady=15)

# Question 11 ...............................................................................

Q11_label = tkinter.Label(personal, text="(11) How Much Do You Spend on Groceries?")
Q11_entry = tkinter.Entry(personal)


Q11_label.grid(row=5, column=0, padx=18, pady=10)
Q11_entry.grid(row=6, column=0,pady=15)

# Question 12 ...............................................................................

other = tkinter.LabelFrame(frame3, text="Other Expenses (1):")
Q12_label = tkinter.Label(other, text="(11) How Much Do You Spend on Pets? (Veterinarian Clinic Visits, Food)")
Q12_entry = tkinter.Entry(other)
submit_btn = tkinter.Button(frame3, text='Submit & View Data',command=lambda:data())


other.grid(row= 3, column=0, padx=10, pady=10)
submit_btn.grid(row=4)
Q12_label.grid(row=1, column=0, padx=68, pady=10)
Q12_entry.grid(row=2, column=0,pady=15)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=              ^^^                  QUESTIONS                 ^^^                    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


for widget in income.winfo_children():
    widget.grid_configure(padx=10, pady=5)

 
window.mainloop()
