#At sea level
temp0 = 288.15 #K
pressure0 = 101325 #pa
density0 = 1.225 # kg/m3
Dyn_visc0 = 1.784e-5 # kg/ms
Kina_visc0 = 1.45e-5 #m2/s
gravity_constant = 6.674e-11 #m3/kg-s2
Mass_earth = 5.972e24 # Kg
Radi_earth = 6378000 #m
gas_constant = 287.05 # J/Kg-K
Tropo_lapse = -0.0065 #K/m
g0 = 9.79798 #m/s2

#Atmosphere Properties
Altitude2 = float(input("Eneter the cruise Altitude: \n"))
if Altitude2 <= 11000:
    g2 = (gravity_constant * Mass_earth)/((Radi_earth + int(Altitude2))**2)

    

    print("\nGravity at this Altitude" + str(g2) + " m/s^2")

    Temp_2 = temp0 + (Altitude2*Tropo_lapse)
    print("Temparature at " + str(Altitude2) + " is " + str(Temp_2) +" Kelvin")

    constant = 5.25 # g/(lapse rate * gas_constant)

     # Desnity at troposhpere
    Density_2 = density0 * ((Temp_2/temp0)**(constant-1))
    print("Density at altitude " + str(Altitude2) + " is " + str(Density_2) + " Kg/m3")



    #pressure at tropospahere
    Pressure_2 = (pressure0 * ((Temp_2/temp0)**constant))
    print("Pressure at altitude " + str(Altitude2) + " is " + str(Pressure_2) + " Pa")

    Dyn_viso_2 = Dyn_visc0*(Temp_2/temp0)**0.75
    print("Dynamic viscosity at altitude " + str(Altitude2) + " is " + str(Dyn_viso_2) + " Kg/m-s")

    Kin_Vis_2 = Dyn_viso_2/Density_2
    print("Kinamatic viscosity at altitude " + str(Altitude2) + " is " + str(Kin_Vis_2) + " m2/s")

else:
    print("\nFly below Troposhepre")
