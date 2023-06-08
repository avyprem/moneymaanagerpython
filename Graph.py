import matplotlib.pyplot as plt

plt.figure(figsize=(7,7))

labels = ['Charan', 'Avy', 'Qadeer','Wilfrid', 'Jonathon']
values = ['1', '2', '3','4', '5']
#explode = [0,0,0,0,0]
colors = ['c', 'b', 'g', 'r', 'y']

plt.pie(values, labels=labels, autopct="%.1f%%", colors=colors)



plt.show()
