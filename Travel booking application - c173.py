# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:35:40 2024

@author: ARV0002
"""

'''US/Central, Asia/Kolkata, Australia/ACT, Japan'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.maxsize(600, 600)
root.minsize(600, 600)
root.title('Travel booking')

l_title = Label(root, text='Travel booking', font=(20))
l_title.place(relx=0.5, rely=0.05, anchor=CENTER)

l_q1 = Label(root, text='Where would you like to go?')
l_q1.place(relx=0.5, rely=0.1, anchor=CENTER)

list1 = ['India','USA','Japan','Australia']
v1 = StringVar()
choice_e1 = ttk.Combobox(root, values=list1, textvariable=v1, state='readonly')
choice_e1.place(relx=0.5, rely=0.15, anchor=CENTER)



l_q2 = Label(root, text='How long do you want your trip to be?')
l_q2.place(relx=0.5, rely=0.2, anchor=CENTER)

list2 = ['1 week','2 weeks','3 weeks','4 weeks']
v2 = StringVar()
choice_e2 = ttk.Combobox(root, values=list2, textvariable=v2, state='readonly')
choice_e2.place(relx=0.5, rely=0.25, anchor=CENTER)



l_q3 = Label(root, text='How many people are coming?')
l_q3.place(relx=0.5, rely=0.3, anchor=CENTER)

list3 = ['1','2','3','4','5','6']
v3 = StringVar()
choice_e3 = ttk.Combobox(root, values=list3, textvariable=v3, state='readonly')
choice_e3.place(relx=0.5, rely=0.35, anchor=CENTER)

class choice:
    def cost(self):
        option1 = v1.get()
        option2 = v2.get()
        option3 = v3.get()
        
        if option1 == '':
            messagebox.showerror('Error', 'You have missed out an option')
        
        score = 500
        if option2 == '1 week':
            score = score * 1
        elif option2 == '2 weeks':
            score = score * 2
        elif option2 == '3 weeks':
            score = score * 3
        elif option2 == '4 weeks':
            score = score * 4
        else:
            messagebox.showerror('Error', 'You have missed out an option')
        
        if option3 == '1':
            score = score * 1
            messagebox.showinfo('Notification', 'Success - Booking complete!')
        elif option3 == '2':
            score = score * 2
            messagebox.showinfo('Notification', 'Success - Booking complete!')
        elif option3 == '3':
            score = score * 3
            messagebox.showinfo('Notification', 'Success - Booking complete!')
        elif option3 == '4':
            score = score * 4
            messagebox.showinfo('Notification', 'Success - Booking complete!')
        elif option3 == '5':
            score = score * 5
            messagebox.showinfo('Notification', 'Success - Booking complete!')
        elif option3 == '6':
            score = score * 6
            messagebox.showinfo('Notification', 'Success - Booking complete!')
        else:
            messagebox.showerror('Error', 'You have missed out an option')
            
        Label(root, text='<--><--><--><--><--><--><--><--><--><-->').place(relx=0.5, rely=0.5, anchor=CENTER)
        str1 = 'You will be going to '+option1+' for '+option2+' in a group of '+option3+'.'
        Label(root, text=str1).place(relx=0.5, rely=0.55, anchor=CENTER)
        str2 = 'The total cost will be: $'+str(score)
        Label(root, text=str2).place(relx=0.5, rely=0.6, anchor=CENTER)
        
        
def con():
    o1 = choice()
    o1.cost()

b_confirm = Button(root, text='Confirm booking', command=con)
b_confirm.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()