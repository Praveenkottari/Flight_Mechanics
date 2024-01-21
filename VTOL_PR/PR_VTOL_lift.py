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
Altitude2 = float(input("Enter the Altitude: \n"))
if Altitude2 <= 11000:
    g2 = (gravity_constant * Mass_earth)/((Radi_earth + int(Altitude2))**2)
    g2 = float(g2)
    
else:
    print("\nFly below Troposhepre")

W = float(input("Enter the Model Weight in Kg: "))
W= W*g2
V = float(input("Enter in what velocity you want to Lift the model in m/s: " ))

Power = W*V
print("Power Required to Lift the model is :" + str(Power) + " Watt")
HP = (Power/746)
print("Power Required to Lift the model is :" + str(HP) + " HP")


