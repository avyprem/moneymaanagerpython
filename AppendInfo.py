# tkinter tutorial https://www.pythontutorial.net/tkinter/tkinter-hello-world/
import csv
import tkinter as tk
import datetime
root = tk.Tk()
root.title('moneymanager')
root.resizable(100,100)
root.geometry(600,300,300)

root.mainloop()

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
   
       
   with open("accountdata.txt","a+") as file:
        file.write(f"First Name: {first_name}\n")
        file.write(f"Last Name: {last_name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Monthly Income: {income}\n")
        file.write("-----------------------------\n")
         
 except ValueError:
    confirmation_label.config(text='not confirmed')

