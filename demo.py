from tkinter.ttk import Treeview
from Database import Database
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefault 
import matplotlib.pyplot as plt
import seaborn as sns 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from TwitterCrawler import TwitterCrawler
from RedditCrawler import RedditCrawler
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox, ttk
from tkinter import *
from tkinter import simpledialog
import mysql.connector

i = 0
twcrawl = TwitterCrawler("OrRuKndlEY6Xx3sOEuWaW3dPx","hwXN4qFNrCSRTy3k8tZWJ5uqJREGI8gJVDhpJj7YZ5Gs3PLfbL","1368589570518831106-JNKPyMGTUgifprCjUJqFZoVa0NzOSx","Yqe9FSSawbubSLQdv7Skifbh02gVnmsXxRF3Xow2upl5U")
rdcrawl = RedditCrawler("Shopping_habits", "zSqCr7ZeezCMgQ", "-K97i2uEaVP9ae69IGGJ8HXp7Xz3LA")
db = Database("localhost","root","password","sqldatabase")
myFont = ('Arial', 15, 'bold')
myFont1 = ('broadway', 15, 'bold')


# Search function: To search the keyword
def search():
    e = simpledialog.askstring(title="Data Crawled",
                               prompt="What do you want to search?:")
    refresh()
    x = db.search(e)
    update(x)


# Refresh function: To refresh the table
def refresh():
    for i in trv.get_children():
        trv.delete(i)
    # print("table")


# Update function: To update table after the search function
def update(rows):
    for i in rows:
        trv.insert('', 'end', values=i)


# plotting function: To plot the graph
def window():
    newWindow = Toplevel(root)
    newWindow.title("Graph")
    newWindow.geometry("300x300")

# plotting function: To plot the graph
def plotting():
    window()
    house_prices = np.random.normal(2000, 2500, 5000)
    plt.hist(house_prices, 50)
    plt.title('Top words overall')
    plt.ylabel('word from tweet', fontsize=12)
    plt.xlabe
    s = plt.show()
    # print("Bar chart")


# crawldata function: To start the crawling of data from the website
def crawldata():
    db.truncatetable()
    twcrawl.crawl(db)
    rdcrawl.crawl(db)
    messagebox.showinfo("Popup", "Crawl Done")


root = Tk(className=' Crawler Data for Reddit & Twitter')
# root2 = Tk()
root.geometry("800x500")
myFont = font.Font(family='Arial', size=15, weight='bold')
myFont1 = font.Font(family='broadway', size=15, weight='bold')
frame = tk.Frame(root)
frame.pack()
#style = ttk.Style()

w = Label(frame,
          text="Welcome to the Crawler Data GUI",
          font="50")
w['font'] = myFont1
w.pack(side=tk.TOP)

button0 = tk.Button(frame,
                    text="Search",
                    fg="black",
                    command=search)
button0['font'] = myFont
button0.pack(side=tk.TOP,
             padx=5,
             pady=5)

wrapper1 = LabelFrame(root, text="Crawl Data")
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
trv = ttk.Treeview(wrapper1,
                   columns=(1, 2, 3, 4, 5, 6),
                   show="headings",
                   height="20")
trv.pack()
trv.heading(1, text="ID")
trv.heading(2, text="type")
trv.heading(3, text="user")
trv.heading(4, text="text")
trv.heading(5, text="likes")
trv.heading(6, text="dates & times")

button1 = tk.Button(frame,
                    text="Exit",
                    fg="red",
                    command=quit)
button1['font'] = myFont
button1.pack(side=tk.BOTTOM,
             padx=5,
             pady=5)

button2 = tk.Button(frame,
                    text="Plot",
                    fg="black",
                    command=plotting)
button2['font'] = myFont
button2.pack(side=tk.BOTTOM,
             padx=5,
             pady=5)

button3 = tk.Button(frame,
                    text="Crawl Data",
                    fg="black",
                    command=crawldata)
button3['font'] = myFont
button3.pack(side=tk.BOTTOM,
             padx=5,
             pady=5)

#window(plotting())
root.mainloop()
