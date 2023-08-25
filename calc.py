import tkinter
from tkinter import*

root = Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#1761b")

label_result = Label(root,width=25,height=2,text="",)
