import tkinter as tk
from tkinter import ttk
from tkinter import * 

backgroundColor = "#333333"
entryWidthSize = 5

class Time_Widgets(tk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.edit = None

    def group_time_widgets(self):
        self.in_entry = tk.Entry(self.master, width = entryWidthSize)
        self.colon_label = tk.Label(self.master, text=" - ", bg=backgroundColor, fg="white")
        self.out_entry = tk.Entry(self.master, width= entryWidthSize)
        self.in_entry.config(state = 'disabled')
        self.out_entry.config(state = 'disabled')
        self.in_entry.grid(row=0, column= 1, sticky=W, pady =3)
        self.colon_label.grid(row = 0, column = 2, sticky=W, pady = 3)
        self.out_entry.grid(row=0, column= 3, sticky=W, pady = 3)

class Login_Gui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.edit = tk.Button()
        self.create_widgets()

#def done(self):
    #return

    """def disable_children(self, parent):
        for child in parent.winfo_children():
            #wtype = child.winfo_class()
            child.configure(state = 'disable')
    """
    def edit_schedule(self):
        for child in self.master.winfo_children():
                wtype = child.winfo_class()
                if isinstance(child, tk.Frame):
                    for subchild in child.winfo_children():
                        if isinstance(subchild, tk.Entry):
                            subchild.config(state = 'normal')

        #disable_children(self.master)

    """
    time widgets created.
    Label for days of the week as long as entry boxes for shift times    
    """
    def create_widgets(self):
        self.mon_label = tk.Label(self.master, text="Monday", bg="grey", fg="white")
        mon_frame = tk.Frame(self.master, height = 100, width=100,bg=backgroundColor, borderwidth = 2)
        mon_frame.grid(row =0, column = 1, sticky = W, pady = 1)
        group = Time_Widgets(master = mon_frame)
        group.group_time_widgets()

        self.tues_label = tk.Label(self.master, text="Tuesday", bg="grey", fg="white")
        tues_frame = tk.Frame(self.master, height = 100, width=100,bg=backgroundColor, borderwidth = 2)
        tues_frame.grid(row =1, column = 1, sticky = W, pady = 1)
        group = Time_Widgets(master = tues_frame)
        group.group_time_widgets()

        self.wed_label = tk.Label(self.master,text = "Wednesday", bg = "grey", fg="white")
        wed_frame = tk.Frame(self.master, height = 100, width=100,bg=backgroundColor, borderwidth = 2)
        wed_frame.grid(row =2, column = 1, sticky = W, pady = 1)
        group = Time_Widgets(master = wed_frame)
        group.group_time_widgets()

        self.thur_label = tk.Label(self.master,text = "Thursday", bg = "grey", fg="white")
        thurs_frame = tk.Frame(self.master, height = 100, width=100,bg=backgroundColor, borderwidth = 2)
        thurs_frame.grid(row =3, column = 1, sticky = W, pady = 1)
        group = Time_Widgets(master = thurs_frame)
        group.group_time_widgets()

        self.fri_label = tk.Label(self.master,text = "Friday", bg = "grey", fg="white")
        fri_frame = tk.Frame(self.master, height = 100, width=100,bg=backgroundColor, borderwidth = 2)
        fri_frame.grid(row =4, column = 1, sticky = W, pady = 1)
        group = Time_Widgets(master = fri_frame)
        group.group_time_widgets()

        self.sat_label = tk.Label(self.master,text = "Saturday", bg = "grey", fg="white")
        sat_frame = tk.Frame(self.master, height = 100, width=100,bg=backgroundColor, borderwidth = 2)
        sat_frame.grid(row =5, column = 1, sticky = W, pady = 1)
        group = Time_Widgets(master = sat_frame)
        group.group_time_widgets()


        #position day labels on grid 
        self.mon_label.grid(row = 0, column=0, sticky=W, pady=3)  
        self.tues_label.grid(row=1, column= 0, sticky=W, pady = 3)
        self.wed_label.grid(row=2, column= 0, sticky=W, pady = 3)
        self.thur_label.grid(row=3, column= 0, sticky=W, pady = 3)
        self.fri_label.grid(row=4, column= 0, sticky=W, pady = 3)
        self.sat_label.grid(row=5, column= 0, sticky=W, pady = 3)
    

        #Edit and Quit buttons 
        self.edit = tk.Button(self.master, text = "EDIT", fg = "red", command = self.edit_schedule)
        
        self.edit.grid (row = 6, column = 0, sticky = W, pady = 2)
        self.quit = tk.Button(self.master, text = "QUIT", fg = "red", command=self.master.destroy)
        self.quit.grid(row = 6, column=1, sticky=W, pady=2)



if __name__ == "__main__":   
    root = tk.Tk()
    root.geometry("500x500")
    root.configure(background = backgroundColor)
    Login_Gui(master=root).grid(sticky="nsew")
    #root.grid_rowconfigure(0, weight=1)
    #root.grid_columnconfigure(0 ,weight=1)
    #app = Login_Gui(master=root)
    root.mainloop()