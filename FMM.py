from tkinter import *
import tkinter.messagebox as tmsg
from functools import partial
# import MessageBox 
def getval():       #getvalue
    a = vel.get()
    # At a Room Tempreture We are Defining the Type of Nozzle by Calculating Mach Number
    # a = int(input("Enter the velocity of fluid is :"))   #add the velocity of the fluid as run time a = velocity of fluid
    v = 346    #taking the velocity of sound as 346m/s
    Mach_no = a/v #for Calculation of Mach number
    # print("The Mach Number is :", Mach_no)
    Label(root,text=f"The Mach Number is :{Mach_no}").grid(row=6,)

    if Mach_no <= 1:
    #   Label(root,text=f"This is a subsonic flow or Convergent Type of Nozzle").pack()
        # Label(root,text="TYPE: SUBSONIC FLOW OR CONVERGENT ").grid(row=8,column=0)
        tmsg.showinfo("INFO",f"The Mach Number is :{Mach_no} \nSUBSONIC FLOW OR CONVERGENT NOZZLE")
    else:
    #   print("This is a Supersonic floe or Divergent Type of Nozzle")
    #   Label(root,text="TYPE : SUPERSONIC FLOW OR DIVERGENT ").grid(row=10,column=0)
      tmsg.showinfo("INFO",f"The Mach Number is :{Mach_no} \nSUPERSONIC FLOW OR DIVERGENT NOZZLE")
    

root = Tk()
root.geometry('300x200')
globalF1=Frame(root)

    # by vaaring the cross section the velocity get increase and the pressure get decrease   
Label(root,text=f"Enter Fluid velocity").grid(row=0,pady=10,padx=90)
vel=IntVar()
E=Entry(root,width=20,textvariable=vel)
E.grid(row=2)

B =Button(root, text ="Show info", command = getval)
B.grid(row=4,pady=10)
root.mainloop()