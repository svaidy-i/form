# This program creates a form where the entered data is stored in a csv file.

from tkinter import*
import csv
from tkinter import messagebox

root=Tk()

Label(root,text="Registration Form",bg="blue",fg="white").grid(row=1,column=5)

# Takes Entries 

Label(root,text="Name").grid(row=2,column=1)
name=Entry(root)
name.grid(row=2,column=2)

Label(root,text="Language").grid(row=4,column=1)
lang=Entry(root)
lang.grid(row=4,column=2)

gend = IntVar()
gvalue = StringVar()

def gender():
    if gend.get()==1:
        gvalue.set("Male")
    else:
        gvalue.set("Female")
        
Label(root,text="Gender").grid(row=6,column=1)
Label(root, text="Gender").grid(row=6, column=1)
Radiobutton(root, text="Male", variable=gend, value=1, command=gender).grid(row=6, column=2)
Radiobutton(root, text="Female", variable=gend, value=2, command=gender).grid(row=7, column=2)


Label(root,text="Address").grid(row=8,column=1)
address=Entry(root,width=60)
address.grid(row=8,column=2)


Label(root,text="E-mail").grid(row=10,column=1)
email=Entry(root)
email.grid(row=10,column=2)


Label(root,text="Contact info:").grid(row=12,column=1)
contact=Entry(root)
contact.grid(row=12,column=2)


Label(root,text="Country").grid(row=14,column=1)
country=Entry(root)
country.grid(row=14,column=2)


Label(root,text="State").grid(row=16,column=1)
state=Entry(root)
state.grid(row=16,column=2)

core = IntVar()
cvalue=StringVar()

def course():
    if core.get()==1:
        cvalue.set("Science")
        
    elif core.get()==2:
        cvalue.set("Commerce")
        
    else:
        cvalue.set("Arts")
        
Label(root,text="Course").grid(row=18,column=1)
Radiobutton(root, text="Science", variable=core, value=1, command=course).grid(row=18, column=2)
Radiobutton(root, text="Commerce", variable=core, value=2, command=course).grid(row=19, column=2)
Radiobutton(root, text="Arts", variable=core, value=3, command=course).grid(row=20, column=2)

# Data is stored in a csv file
def reg():
    messagebox.showinfo("Status","Registration Complete!")
    
    data= [name.get(),lang.get(),gvalue.get(),address.get(),email.get(),contact.get(),country.get(),state.get(),cvalue.get()]
    
    with open ("____",mode="a") as file: # please enter your csv file path in "____"
        o=csv.writer(file)
        o.writerow(data)
        
    print("Data written to file")
    
    with open("____",mode="r")as f: # please enter your csv file path in "____"
        read=csv.reader(f)
        for i in read:
            print(i)
           
b = Button(root, text="Complete Registration", command=reg).grid(row=21,column=5)

root.mainloop()


