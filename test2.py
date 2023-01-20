from tkinter import *
class Mine:
   def __init__(self,master):
       framev=Frame(master)
       framev.grid(row=0,column=0)
if __name__=="__main__":
   root=Tk()
   root.geometry("500x500")
   root.wm_title("I want to change the color of THIS area")
   m=Mine(root)
   root.overrideredirect(True)
   root.mainloop()