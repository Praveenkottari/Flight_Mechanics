import math
import sys,os
import tkinter
from tkinter import *

os.chdir(sys._MEIPASS)
root=Tk()
root.title("Propellar Thrust Calculator")
root.geometry("550x500")
root.iconbitmap('data\\edall.ico')

def Calculation():
    Density =float(Densityentry.get())
    Prop_Rot = float(Prop_Rotationentry.get())
    prop_dia = float(Prop_Diameterentry.get())
    Prop_pitch = float(Prop_Pitchvalueentry.get())

    Thrust_N = ((Density*(math.pi))*(((0.0254*prop_dia)/2)**2)*((Prop_Rot*0.0254*Prop_pitch/60)**2)*(((prop_dia)/(3.29546*Prop_pitch))**1.5))
    Label(text=f"{Thrust_N}",font="arial 15 bold").place(x=300,y=250)

    Thrust_kg = (Thrust_N/9.81)
    Label(text=f"{Thrust_kg}",font="arial 16 bold").place(x=300,y=300)

#parameters
param1 =Label(root,text="Density(Kg/m^3):",font="arial 14")
param2 =Label(root,text="Prop Rotation(RPM):",font="arial 14")
param3 =Label(root,text="Prop Diameter(inch):",font="arial 14")
param4 =Label(root,text="Prop Pitch(inch):",font="arial 14")
Thrust_N =Label(root,text="Static Thrust(Newton) :",font="arial 16")
Thrust_kg =Label(root,text="Static Thrust(Kg):",font="arial 16")

param1.place(x=50,y=20)
param2.place(x=50,y=70)
param3.place(x=50,y=120)
param4.place(x=50,y=170)
Thrust_N.place(x=50,y=250)
Thrust_kg.place(x=50,y=300)

Densityvalue=StringVar()
Prop_Rotationvalue=StringVar()
Prop_Diametervalue=StringVar()
Prop_Pitchvalue=StringVar()

Densityentry=Entry(root,textvariable=Densityvalue,font="arial 15",width=15)
Prop_Rotationentry=Entry(root,textvariable=Prop_Rotationvalue,font="arial 15",width=15)
Prop_Diameterentry=Entry(root,textvariable=Prop_Diametervalue,font="arial 15",width=15)
Prop_Pitchvalueentry=Entry(root,textvariable=Prop_Pitchvalue,font="arial 15",width=15)

Densityentry.place(x=300,y=20)
Prop_Rotationentry.place(x=300,y=70)
Prop_Diameterentry.place(x=300,y=120)
Prop_Pitchvalueentry.place(x=300,y=170)

Button(text="Calculate",font="arial 15",bg="grey",bd=15,command=Calculation).place(x=50,y=400)
Button(text="Exit",font="arial 15",bg="grey",bd=15,width=10,command=lambda:exit()).place(x=350,y=400)

root.mainloop()
