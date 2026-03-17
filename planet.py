''' class to represent a planet with attributes such as name , mass radius etc'''
from math import pi
''' class to represent a planet with attributes such as name, mass, radius , distance from sun and orbital period with relevant class methods '''

class Planet:



    def __str__(self):

        return (f"{self.name}: Mass={self.mass:.2e} kg, Radius={self.radius} km, "
                f"Distance={self.distance_from_sun} million km, "
                f"Orbital Speed={self.calculate_orbital_speed()} km/s, "
                f"Surface Gravity={self.calculate_surface_gravity()} m/s^2")  
    '''init method to initialize the planet objects with attributes such as name, mass , radius , distance from sun and orbital period'''
    
    def __init__(self, name, mass, radius, distance_from_sun , orbital_period): 
        self.name = name 
        self.mass = mass 
        self.radius = radius 
        self.distance_from_sun = distance_from_sun
        self.orbital_period = orbital_period 
    '''orbital speed method to calculate the orbital speed of the planet using the formula '''

   
    def calculate_orbital_speed(self):

        # Simplified orbital speed formula: v = 2πr / T
        r_km = self.distance_from_sun * 1e6  # convert million km to km
        T_sec = self.orbital_period * 24 * 3600  # convert days to seconds
        speed = (2 * pi * r_km) / T_sec
        return round(speed, 2)
    '''surface gravity method to calculate surface gravity of the planet using formula derived from physics'''

    def calculate_surface_gravity(self):

        G = 6.67430e-11  # m^3/kg/s^2
        radius_m = self.radius * 1000  # convert km to meters
        gravity = (G * self.mass) / (radius_m ** 2)
        return round(gravity, 2)  # m/s^2
    ''' get info method to return a dictionary containing planet information and calculated values such as orbita speed and surface gravity'''
 
    
    def get_info(self): 
        return { 
            "name" : self.name, 
            "mass" : self.mass, 
            "radius" : self.radius, 
            "distance_from_sun" : self.distance_from_sun, 
            "orbital_period" : self.orbital_period, 
            "surface_gravity" : self.calculate_surface_gravity(),
            "orbital_speed" : self.calculate_orbital_speed()
        }
    '''planet method to classify the planet based on its mass and radius using a nested elseif loop'''
    def planet_type(self):
 	  	
         """
 	  	      Classify the planet based on its mass and radius.
 	  	
         uses a nested elseif loop to test and classify a planet as either terrestrial or gas giant 
   	
 
 	  	
         """
   	
 
   	
         if 1e23 < self.mass < 5e25 and 1500 <= self.radius <= 10000:
 	  	
 
   	
             return "Terrestrial"
 	  	
         
 	  	
         elif self.mass > 1e25 and self.radius > 30000:
 
	  	
             return "Gas Giant"
	  	
         
  	
         else:
 	  	
             return "Unknown"
 	  	
 
    '''is habitable method to determine if a planet is habitable or not'''

    
    def is_habitable(self):
            if self.planet_type() == "Terrestrial": 
   	
             return True 
   	
            else: 
   	
             return False
            


''' this class represents a planet with relevant attributes and methods to calculate speed and gravity '''
    
