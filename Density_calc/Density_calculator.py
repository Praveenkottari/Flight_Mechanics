import math
from math import sqrt as sr
import matplotlib.pyplot as plt
import numpy as np

#Universal constants
G_C = 6.674e-11 #Gravity_constants
M_E = 5.972e+24 #Mass of the Earth
R_E = 6378000 #Radius of Earth in meter
R_gas = 287 #Charecteristic gas constant

#Sea Level Parameters
T_0 = 288.15 #Temp at sea level
P_0 = 101325 #pressure at sea level in pascle
g_0 = 9.797989 #Gravity at sea level in kg m/s^2
Den_0 = 1.225 #Density at sea level in Kg/m^3
vis_0 = 1.79e-5 #Viscosity at sea level
L_R = -0.0065 #LapseRate at troposphere
gmuhR_Ratio = 5.25 

#Density calculation
Altitude = int(input("Enter the Altitude in meter: "))
#x = np.arange(0,Altitude+250,250)
#T_Altitude = (L_R * x)+T_0
T_Altitude = (L_R * Altitude)+T_0
Den_Altitude = (Den_0*((T_Altitude/T_0)**(gmuhR_Ratio-1)))

print("The Density of the Altitude is: " + str(Den_Altitude) + " Kg/m^3")

#for i in range (0,len(x)):
    #print(x[i],Den_Altitude[i])


