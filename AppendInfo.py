#note code does not fully function without the questionnaire code added!
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messageboxtutorial https://www.pythontutorial.net/tkinter/tkinter-hello-world/
import csv
import datetime
#Uses current real time information to open up a new .txt file
current_time = datetime.datetime.now()
account = f"account_#{current_time.strftime('%Y%m%d%S')}.txt"

def number():
   
    # Check if income contains letters or symbols, only accepts numbers (1,2,3, etc (also accepts decimals))
    try:
        float(monthly_income.get())
        confirmation_label.config(text='confirmed')
        confirm_btn['state'] = 'disabled'
        monthly_income['state'] = 'disabled'
        
        # saves user information to a text file
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        age = age_spinbox.get()
        income = monthly_income.get()

#Opens the real time .txt file and writes data to file
   with open(account,"w") as csv:
        csv.write(f"First Name: {first_name}\n")
        csv.write(f"Last Name: {last_name}\n")
        csv.write(f"Age: {age}\n")
        csv.write(f"Monthly Income: {income}\n")
        csv.write("-----------------------------\n")
         
 except ValueError:
    tkinter.messagebox.showwarning(title = '!WARNING!', message = 'We seemed to have detected a letter, or symbol in the text box. Please try again')
    confirmation_label.config(text='not confirmed')

