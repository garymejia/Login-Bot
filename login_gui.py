import tkinter as tk
from tkinter import ttk
from tkinter import * 

backgroundColor = "#333333"
entryWidthSize = 5

class Time_Widgets(tk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.master = master
    def group_time_widgets(self):
        self.in_entry = tk.Entry(self.master, width = entryWidthSize)
        self.colon_label = tk.Label(self.master, text=":", bg=backgroundColor, fg="white")
        self.out_entry = tk.Entry(self.master, width= entryWidthSize)
        self.in_entry.grid(row=0, column= 1, sticky=W, pady =3)
        self.colon_label.grid(row = 0, column = 2, sticky=W, pady = 3)
        self.out_entry.grid(row=0, column= 3, sticky=W, pady = 3)

class Login_Gui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.pack()
        self.create_widgets()

    def create_widgets(self):
        """self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello\n"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
"""
        #Initialization of Widgetes
        """self.mon_in_entry = tk.Entry(self.master, width = entryWidthSize)
        self.mon_out_entry = tk.Entry(self.master, width = entryWidthSize)
        """
        
        self.mon_label = tk.Label(self.master, text="Monday", bg="grey", fg="white")
        frame1 = tk.Frame(self.master, height = 100, width=100,bg=backgroundColor, borderwidth = 2)
        frame1.grid(row =0, column = 1, sticky = W, pady = 1)
        group = Time_Widgets(master = frame1)
        group.group_time_widgets()


        self.tues_label = tk.Label(self.master, text="Tuesday", bg="grey", fg="white")

        self.wed_label = tk.Label(self.master,text = "Wednesday", bg = "grey", fg="white")
        
        self.thur_label = tk.Label(self.master,text = "Thursday", bg = "grey", fg="white")

        self.fri_label = tk.Label(self.master,text = "Friday", bg = "grey", fg="white")
        
        self.sat_label = tk.Label(self.master,text = "Saturday", bg = "grey", fg="white")

        #organization of widgets into grid layout        
        #pady are spaces in the horizontal vertex 
        self.mon_label.grid(row = 0, column=0, sticky=W, pady=3)
       
        self.tues_label.grid(row=1, column= 0, sticky=W, pady = 3)
        
        self.wed_label.grid(row=2, column= 0, sticky=W, pady = 3)
       
        self.thur_label.grid(row=3, column= 0, sticky=W, pady = 3)
       
        self.fri_label.grid(row=4, column= 0, sticky=W, pady = 3)
       
        self.sat_label.grid(row=5, column= 0, sticky=W, pady = 3)
       
        """frame1 = tk.Frame(self.master, height = 100, width=100,bg="WHITE", borderwidth = 2)
        frame1.grid(row = 7, column = 0, sticky = W, pady = 1)
        group = Time_Widgets(master = frame1)
        group.group_time_widgets()
        """
        self.quit = tk.Button(self.master, text = "QUIT", fg = "red", command=self.master.destroy)
        self.quit.grid(row = 6, column=0, sticky=W, pady=2)
        

if __name__ == "__main__":   
    root = tk.Tk()
    root.geometry("500x500")
    root.configure(background = backgroundColor)
    Login_Gui(master=root).grid(sticky="nsew")
    #root.grid_rowconfigure(0, weight=1)
    #root.grid_columnconfigure(0 ,weight=1)
    #app = Login_Gui(master=root)
    root.mainloop()