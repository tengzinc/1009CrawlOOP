# others
import numpy as np
# tkinter
from tkinter.ttk import Treeview
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox, ttk
from tkinter import *
from tkinter import simpledialog
# matplotlib
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# User Defined Modules
from Database import Database
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler
from socialMediaObjectCreator import socialMedia


class GUI:
    def __init__(self, db, reddit, twitter):
        self.graph = socialMedia
        self.myFont = ('Arial', 15, 'bold')
        self.myFont1 = ('broadway', 15, 'bold')
        self.db = db
        self.redditObject = socialMedia(self.db, "reddit")
        self.twitterObject = socialMedia(self.db, "twitter")
        self.reddit = reddit
        self.twitter = twitter
        self.root = Tk(className=' Crawler Data for Reddit & Twitter')
        self.root.geometry("800x500")
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.w = Label(self.frame,
                       text="Welcome to the Crawler Data GUI",
                       font="50")
        self.w['font'] = self.myFont1
        self.w.pack(side=tk.TOP)

        self.button0 = tk.Button(self.frame,
                                 text="Search",
                                 fg="black",
                                 command=self.search)
        self.button0['font'] = self.myFont
        self.button0.pack(side=tk.TOP,
                          padx=5,
                          pady=5)

        self.wrapper1 = LabelFrame(self.root, text="Crawl Data")
        self.wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
        self.trv = ttk.Treeview(self.wrapper1,
                                columns=(1, 2, 3, 4, 5, 6),
                                show="headings",
                                height="20")
        self.trv.pack()
        self.trv.heading(1, text="ID")
        self.trv.heading(2, text="type")
        self.trv.heading(3, text="user")
        self.trv.heading(4, text="text")
        self.trv.heading(5, text="likes")
        self.trv.heading(6, text="dates & times")

        self.button1 = tk.Button(self.frame,
                                 text="Exit",
                                 fg="red",
                                 command=quit)
        self.button1['font'] = self.myFont
        self.button1.pack(side=tk.BOTTOM,
                          padx=5,
                          pady=5)

        self.button2 = tk.Button(self.frame,
                                 text="Plot",
                                 fg="black",
                                 command=self.plotting)
        self.button2['font'] = self.myFont
        self.button2.pack(side=tk.BOTTOM,
                          padx=5,
                          pady=5)

        self.button3 = tk.Button(self.frame,
                                 text="Crawl Data",
                                 fg="black",
                                 command=self.crawldata)
        self.button3['font'] = self.myFont
        self.button3.pack(side=tk.BOTTOM,
                          padx=5,
                          pady=5)

    # Refresh function: To refresh the table
    def refresh(self):
        for i in self.trv.get_children():
            self.trv.delete(i)
        # print("table")

    # Update function: To update table after the search function
    def update(self, rows):
        for i in rows:
            self.trv.insert('', 'end', values=i)

    # Search function: To search the keyword
    def search(self):
        e = simpledialog.askstring(title="Data Crawled",
                                   prompt="What do you want to search?:")
        self.refresh()
        x = self.db.search(e)
        self.update(x)

    # window function: To open new window when plotting the graph
    # def window():
    #   newWindow = Toplevel(root)
    #   newWindow.title("Graph")
    #   newWindow.geometry("300x300")

    # plotting function: To plot the graph
    def tplotting(self):
        objects = ('scam', 'drug', 'violence', 'sexOffence')
        y_pos = np.arange(len(objects))
        performance = [self.redditObject.getCrimeScore()]
        plt.barh(y_pos, performance, align='center', alpha=0.7)
        plt.yticks(y_pos, objects)
        plt.ylabel('Category')
        plt.xlabel('Frequency')
        plt.title('Keyword Category in the News')

        plt.show()

        print("Plot")
    
    # plotting function: To plot the graph
    def plotting(self):
        key = list(self.redditObject.getCrimeScore().keys())
        value = list(self.redditObject.getCrimeScore().values())
        plt.bar(range(len(self.redditObject.getCrimeScore())),value,tick_label=key)
        plt.xlabel('Category')
        plt.ylabel('Frequency')
        plt.title('Keyword Category in the News')

        plt.show()

        print("Plot")

    # crawldata function: To start the crawling of data from the website
    def crawldata(self):
        self.db.createTable()
        self.reddit.crawl(self.db)
        self.twitter.crawl(self.db)
        self.redditObject = socialMedia(self.db, "reddit")
        self.twitterObject = socialMedia(self.db, "twitter")
        messagebox.showinfo("Popup", "Crawl Done")