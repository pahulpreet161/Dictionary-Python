import csv
from tkinter import *
from tkinter.ttk import *
class mydictionary:

    def search(self):
        self.t1.delete(*self.t1.get_children())

        rd = open("dictionary.csv", "r")
        obj = csv.reader(rd)
        i = 0
        for r in obj:
            if r[0] in self.txt.get():
                p = [i + 1, r[0], r[1]]
                self.t1.insert("", index=i, values=p)
                i = i + 1

    def __init__(self):
        self.root=Tk()

        self.p1=PanedWindow(self.root)
        self.p2=PanedWindow(self.root)

        self.lb1=Label(self.p1,text="Enter Search word")
        self.txt=Entry(self.p1)
        self.bt1=Button(self.p1,text="Search",command=self.search)

        self.lb1.grid(row=0,column=0)
        self.txt.grid(row=0,column=1)
        self.bt1.grid(row=0,column=2)

        self.t1=Treeview(self.p2,columns=("srno","word","meaning"))
        self.t1.heading("srno",text="Serial Number")
        self.t1.heading("word",text="Word")
        self.t1.heading("meaning",text="Meaning")
        self.t1.pack()

        rd=open("dictionary.csv","r")
        obj=csv.reader(rd)
        i=0
        for r in obj:
            p=[i + 1, r[0] , r[1] ]
            self.t1.insert("",index=i,values=p)
            i=i + 1



        self.p1.pack()
        self.p2.pack()

        self.root.mainloop()

#---------------------------------------

mydictionary()