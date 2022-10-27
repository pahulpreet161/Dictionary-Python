
from tkinter import *
import csv
from tkinter.messagebox import *
class addword:

    def newword(self):

        if self.txt1.get()=="" or self.txt2.get()=="":
            showinfo("","Please Fill word and meaning")
        else:
            wr=open("dictionary.csv","a")
            obj=csv.writer(wr)
            p=[self.txt1.get(),self.txt2.get()]
            obj.writerow(p)
            wr.close()
            showinfo("","Word Added Successfully")


    def __init__(self):
        self.root=Tk()
        self.lb1=Label(self.root,text="Enter Word")
        self.lb2=Label(self.root,text="Enter Meaning")

        self.txt1=Entry(self.root)
        self.txt2=Entry(self.root)

        self.bt1=Button(self.root,text="Add Word",command=self.newword)

        self.lb1.grid(row=0,column=0)
        self.txt1.grid(row=0,column=1)

        self.lb2.grid(row=1,column=0)
        self.txt2.grid(row=1,column=1)

        self.bt1.grid(row=2,column=1)

        self.root.mainloop()
#---------------------------------------------
addword()
