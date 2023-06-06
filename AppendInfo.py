# tkinter tutorial https://www.pythontutorial.net/tkinter/tkinter-hello-world/
import csv
import tkinter as tk

root = tk.Tk()
root.title('moneymanager')
root.resizable(100,100)
root.geometry(600,300,300)

root.mainloop()

def saveaccountdata():
   with open("account.txt", "a") as file:
        file.write(f"First Name: {first_name}\n")
        file.write(f"Last Name: {last_name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Monthly Income: {income}\n")
        file.write("-----------------------------\n")

