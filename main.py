import requests
from tkinter import *
from tkinter import ttk
import random


class Used:
    def __init__(self):
        self.used_numbers = requests.get('https://www.pais.co.il/lotto/lotto_resultsDownload.aspx')
        self.used_list = []

    def simplify(self):
        temp = self.used_numbers.content.decode('iso-8859-1').replace("\n", "").split("\r")
        for i in temp[1:-1]:
            self.used_list.append([int(x) for x in i.split(",")[2:8]])


used_nums = Used()
used_nums.simplify()


def generate(num, numlist):
    lottery = []
    trv.delete(*trv.get_children())
    for n in range(num):
        while True:
            temp= random.sample(range(1, 37), 6)
            temp.sort()
            temp.append(random.randint(1,7))
            if temp not in numlist:
                lottery.append(temp)
                break
    for lotto in lottery:
        trv.insert('',END,values=lotto)



window = Tk()
window.title("Lottery Numbers Generator")
window.geometry("800x600")

f_right = Frame(window, background="#FFF0C1", bd=1, relief=SUNKEN)
f_left = Frame(window, background="#D2E2FB", bd=1, relief=SUNKEN)
f_inside_left = Frame(f_left, relief=SUNKEN)
f_inside_left.pack(pady=10, padx=10, fill=X)
f_right.grid(row=0, column=1, sticky=NSEW)
f_left.grid(row=0, column=0, sticky=NSEW)

window.grid_rowconfigure(0, weight=2)
window.grid_columnconfigure(0, weight=4)
window.grid_columnconfigure(1, weight=1)

label = LabelFrame(f_right, text="number of rows", labelanchor='ne')
label.pack(padx=5, pady=40)
row_options = ttk.Combobox(label, state="readonly",
                           values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14])
row_options.current(0)
row_options.pack(pady=10, padx=10)
row_options.configure(justify='right')
scrollbar = Scrollbar(f_inside_left)
scrollbar.pack(side=RIGHT, fill=Y)
columns = ("1", "2", "3", "4", "5", "6", "7")
trv = ttk.Treeview(f_inside_left, columns=columns, yscrollcommand=scrollbar.set, show='headings')
trv.heading("1", text="1")
trv.heading("2", text="2")
trv.heading("3", text="3")
trv.heading("4", text="4")
trv.heading("5", text="5")
trv.heading("6", text="6")
trv.heading("7", text="powerball")
trv.column("1", width=30, minwidth=0, stretch=YES,anchor=CENTER)
trv.column("2", width=30, minwidth=0, stretch=YES,anchor=CENTER)
trv.column("3", width=30, minwidth=0, stretch=YES,anchor=CENTER)
trv.column("4", width=30, minwidth=0, stretch=YES,anchor=CENTER)
trv.column("5", width=30, minwidth=0, stretch=YES,anchor=CENTER)
trv.column("6", width=30, minwidth=0, stretch=YES,anchor=CENTER)
trv.column("7", width=30, minwidth=0, stretch=YES,anchor=CENTER)
trv.pack(fill=X)
scrollbar.configure(command=trv.yview)

generate_button = Button(f_right, text="Generate Numbers",
                         command=lambda: generate(int(row_options.get()), used_nums.used_list))
generate_button.pack(side=BOTTOM, pady=20, ipadx=10, ipady=10)
window.mainloop()
