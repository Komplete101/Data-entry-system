import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from tkinter import *


class Loginpage(tk.Frame):
    def __init__(self, p, c):
        tk.Frame.__init__(self, p)

        border = tk.LabelFrame(self, text="Login", bg="#FFFFFF", bd=10, font=("Helvetica", 15))
        border.pack(fill="both", expand="yes", padx=1, pady=1)


        username_label = tk.Label(border, text="Username", font=("Helvetica", 15))
        username_label.place(x=0, y=100)
        username_entry = tk.Entry(border, width=30, bd=5)
        username_entry.place(x=200, y=100)

        password_text = tk.Label(border, text="Password", font=("Helvetica", 15))
        password_text.place(x=0, y=200)
        password_entry = tk.Entry(border, width=30, show='*', bd=5)
        password_entry.place(x=200, y=200)

        def auth():
            try:
                with open("user.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for i in info:
                        ur, pw = i.split(",")
                        if ur.strip() == username_entry.get() and pw.strip() == password_entry.get():
                            c.show_frame(DataEntry)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo(title='Error', message='Please Register')
            except:
                messagebox.showinfo(title='Error', message='Please Register')

        login_button = tk.Button(border, text="Enter", font=("Helvetica", 15), command=auth)
        login_button.place(x=650, y=400)

        def register():

            window = tk.Tk()
            window.configure(bg="#ffffff")
            window.title("Registration")
            window.resizable(0, 0)

            nu = tk.Label(window, text="Username", font=("Helvetica", 15))
            nu.place(x=10, y=10)
            nu_entry = tk.Entry(window, width=30, bd=5)
            nu_entry.place(x=200, y=10)

            np = tk.Label(window, text="Password", font=("Helvetica", 15))
            np.place(x=10, y=60)
            np_entry = tk.Entry(window, width=30, bd=5)
            np_entry.place(x=200, y=60)

            np2 = tk.Label(window, text="Confirm Password", font=("Helvetica", 15))
            np2.place(x=10, y=110)
            np_entry2 = tk.Entry(window, width=30, bd=5)
            np_entry2.place(x=200, y=110)

            def verify():
                if nu_entry.get() != "" or np_entry.get() != "" or np_entry2.get() != "":
                    if np_entry.get() == np_entry2.get():
                        with open("user.txt", "a") as f:
                            f.write(nu_entry.get() + "," + np_entry.get() + "\n")
                            messagebox.showinfo(title="Welcome", message="Successfully Registered")
                    else:
                        messagebox.showinfo(title="Error", message="Incorrect Password")
                else:
                    messagebox.showinfo(title="Error", message="Box empty check again")

            rb = tk.Button(window, text="Confirm New user", font=("Helvetica", 15), command=verify)
            rb.place(x=200, y=200)

            window.geometry("500x500")
            window.mainloop()

        registration_button = tk.Button(border, text="Register", font=("Helvetica", 15), command=register)
        registration_button.place(x=650, y=100)

        def admin():
            window = tk.Tk()
            window.configure(bg="#ffffff")
            window.title("Admin Verification")
            window.resizable(0, 0)

            nu = tk.Label(window, text="What is the admin code that is definitely not: 1111", font=("Helvetica", 15))
            nu.place(x=10, y=10)
            nu_entry = tk.Entry(window, width=30, bd=5)
            nu_entry.place(x=10, y=100)

            def verifya():
                if nu_entry.get() == "1111":
                    c.show_frame(ADataEntry)

            rb = tk.Button(window, text="Enter", font=("Helvetica", 15), command=verifya)
            rb.place(x=200, y=200)

            window.geometry("500x500")
            window.mainloop()

        admin_button = tk.Button(border, text="Admin", font=("Helvetica", 15), command=admin)
        admin_button.place(x=650, y=150)


class DataEntry(tk.Frame):
    def __init__(self, p, c):
        tk.Frame.__init__(self, p)

        iteminfoframe = tk.LabelFrame(self, text="Employee Data Entry", bg="#ffffff", bd=10, font=("Helvetica"))
        iteminfoframe.pack(fill="both", expand="yes", padx=1, pady=1)

        categorieslistlabel = tk.Label(iteminfoframe, text="Categories")
        categorieslistlabel.place(x=100, y=50)
        item_combobox = ttk.Combobox(iteminfoframe,
                                     values=["Case", "MotherBoard", "CPU", "CPU Cooler", "Memory", "Storage",
                                             "Graphics Card", "Power Supply", "Operating System"])
        item_combobox.place(x=100, y=100)

        itembrandlabel = tk.Label(iteminfoframe, text="Brand")
        itembrandlabel.place(x=100, y=150)
        itembrandentry = tk.Entry(iteminfoframe, width=30, bd=5)
        itembrandentry.place(x=100, y=200)

        namelabel = tk.Label(iteminfoframe, text="Name")
        namelabel.place(x=100, y=250)
        nameentry = tk.Entry(iteminfoframe, width=30, bd=5)
        nameentry.place(x=100, y=300)


        formfactorlabel = tk.Label(iteminfoframe, text="Form Factor")
        formfactorlabel.place(x=350, y=50)
        formfactor_combobox = ttk.Combobox(iteminfoframe,
                                           values=["Fit All", "ATX", "Micro ATX", "Mini ITX", "Non Applicable"])
        formfactor_combobox.place(x=350, y=100)

        memorylabel = tk.Label(iteminfoframe, text="Memory")
        memorylabel.place(x=350, y=150)
        memory_combobox = ttk.Combobox(iteminfoframe,
                                       values=["Not Integrated", "2 GB", "4 GB", "8 GB", "16 GB", "32 GB", "64 GB",
                                               "128 GB", "256 GB", "512 GB"])
        memory_combobox.place(x=350, y=200)

        quantitylabel = tk.Label(iteminfoframe, text="Quantity")
        quantitylabel.place(x=350, y=250)
        quanity_spinbox = tk.Spinbox(iteminfoframe, from_=0, to="infinity")
        quanity_spinbox.place(x=350, y=300)

        def add_inventory():
            invent = open("Inventory.csv", "a", newline='')
            Writer = csv.writer(invent, delimiter="|")
            if item_combobox.get() != "" and itembrandentry.get() != "" and nameentry.get() != "" and formfactor_combobox.get() and memory_combobox.get() != "" and quanity_spinbox.get() != "":
                Writer.writerow([item_combobox.get(), itembrandentry.get(), nameentry.get(), formfactor_combobox.get(),
                                 memory_combobox.get(), quanity_spinbox.get()])

        backbut = tk.Button(self, text="Back", font=("Helvetica", 15), command=lambda: c.show_frame(Loginpage))
        backbut.place(x=550, y=450)

        confirm_ent = tk.Button(self, text="Confirm Entry", font=("Helvetica", 15), command=add_inventory)
        confirm_ent.place(x=750, y=450)


class ADataEntry(tk.Frame):
    def __init__(self, p, c):
        tk.Frame.__init__(self, p)

        iteminfoframe2 = tk.LabelFrame(self, text="Admin Data Entry", bg="#ffffff", bd=10, font=("Helvetica"))
        iteminfoframe2.pack(fill="both", expand="yes", padx=1, pady=1)

        categorieslistlabel = tk.Label(iteminfoframe2, text="Categories")
        categorieslistlabel.place(x=100, y=50)
        item_combobox = ttk.Combobox(iteminfoframe2,
                                     values=["Case", "MotherBoard", "CPU", "CPU Cooler", "Memory", "Storage",
                                             "Graphics Card", "Power Supply", "Operating System"])
        item_combobox.place(x=100, y=100)

        # Creates and places the texts
        itembrandlabel = tk.Label(iteminfoframe2, text="Brand")
        itembrandlabel.place(x=100, y=150)
        itembrandentry = tk.Entry(iteminfoframe2, width=30, bd=5)
        itembrandentry.place(x=100, y=200)

        namelabel = tk.Label(iteminfoframe2, text="Name")
        namelabel.place(x=100, y=250)
        nameentry = tk.Entry(iteminfoframe2, width=30, bd=5)
        nameentry.place(x=100, y=300)

        formfactorlabel = tk.Label(iteminfoframe2, text="Form Factor")
        formfactorlabel.place(x=350, y=50)
        formfactor_combobox = ttk.Combobox(iteminfoframe2,
                                           values=["Fit All", "ATX", "Micro ATX", "Mini ITX", "Non Applicable"])
        formfactor_combobox.place(x=350, y=100)

        memorylabel = tk.Label(iteminfoframe2, text="Memory")
        memorylabel.place(x=350, y=150)
        memory_combobox = ttk.Combobox(iteminfoframe2,
                                       values=["Not Integrated", "2 GB", "4 GB", "8 GB", "16 GB", "32 GB", "64 GB",
                                               "128 GB", "256 GB", "512 GB"])
        memory_combobox.place(x=350, y=200)

        quantitylabel = tk.Label(iteminfoframe2, text="Quantity")
        quantitylabel.place(x=350, y=250)
        quanity_spinbox = tk.Spinbox(iteminfoframe2, from_=0, to="infinity")
        quanity_spinbox.place(x=350, y=300)

        def add_inventory():
            invent = open("Inventory.csv", "a", newline='')
            Writer = csv.writer(invent, delimiter="|")
            if item_combobox.get() != "" and itembrandentry.get() != "" and nameentry.get() != "" and formfactor_combobox.get() and memory_combobox.get() != "" and quanity_spinbox.get() != "":
                Writer.writerow([item_combobox.get(), itembrandentry.get(), nameentry.get(), formfactor_combobox.get(),
                                 memory_combobox.get(), quanity_spinbox.get()])

        confirm_ent = tk.Button(self, text="Confirm Entry", font=("Helvetica", 15), command=add_inventory)
        confirm_ent.place(x=350, y=450)

        def update_quant():
            invent = open("Inventory.csv", "r")
            reader = csv.reader(invent)
            t = []
            itemchose = nameentry.get()
            Found = False
            for row in reader:
                if row[2] == itemchose:
                    Found = True
                else:
                    t.append(row)
            invent.close()
            if Found == True:
                invent = open("Inventory.csv", "w+", newline='')
                Writer = csv.writer(invent)
                Writer.writerows(t)
                invent.seek(0)
                invent.close()

        update = tk.Button(self, text="Update", font=("Helvetica", 15), command=update_quant)
        update.place(x=550, y=450)

        def delete_entry():
            invent = open("Inventory.csv", "r")
            reader = csv.reader(invent)
            t = []
            itemchose = nameentry.get()
            newquant = quanity_spinbox.get()
            Found = False
            for row in reader:
                if row[2] == itemchose:
                    Found = True
                    row[5] = newquant
                t.append(row)
            invent.close()
            if Found == True:
                invent = open("Inventory.csv", "w+", newline=' ')
                Writer = csv.writer(invent)
                Writer.writerows(t)
                invent.seek(0)
                invent.close()

        del_ent = tk.Button(self, text="Delete Entry", font=("Helvetica", 15), command=delete_entry)
        del_ent.place(x=750, y=450)
        
        def view_csv():
            view = tk.Tk()
            view.title ("Current inventory")
            view.geometry("500x500")


            invent = open("Inventory.csv")
            Reader = csv.reader(invent)
            l1 =[]
            l1=next(Reader)
            data = [row for row in  Reader]

            trv = ttk.Treeview(view, selectmode='browse')
            trv.grid(row=1, column=1, padx=30,pady=20)
            trv['height'] = 5
            trv['show'] = 'headings'
            trv['columns'] = l1

            # for i in l1:
            #     trv.column(i,width=100,anchor='c')
            #     trv.heading(i, text=i)
            # for da in data:
            #     v=[r for r in da]
            #     trv.insert('','end',iid=v[0],values=v)

            view.mainloop()
        

        viewinv = tk.Button(self, text="View Inventory", font=("Helvetica", 15), command=view_csv)
        viewinv.place(x=650, y=100)

        backbut = tk.Button(self, text="Back", font=("Helvetica", 15), command=lambda: c.show_frame(Loginpage))
        backbut.place(x=750, y=400)



#This class initializes the the window frame for the pages
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=1000)

        self.frames = {}
        for F in (Loginpage, DataEntry, ADataEntry):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="news")

        self.show_frame(Loginpage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.title("Chis PC Inventory")
app.mainloop()
