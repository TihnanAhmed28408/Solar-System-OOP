"""
solar_system.py

This module defines the SolarSystem class, representing a solar system
with a central star and a list of planets.
"""

from star import Star
from planet import Planet
from read_data import ReadPlanets

class SolarSystem:
    """
    A class representing a solar system with relevant attributes names star and planets """


    def __init__(self, name="Unknown", star=None):
        """
        Initialize a SolarSystem object.

        with attributes name and star in the init function 
        """
        self.name = name if name else "Unknown"
        self.star = star if star else Star("Unknown", 0.0, "Unknown")
        self.planets = self.read_planets()

    def read_planets(self):
        """
        Read planet data from a CSV using ReadPlanets and create Planet objects.
        this method reads planets from csv file using the imported ReadPlanets CSV reader class
        """
    
        planet_list = []
        reader = ReadPlanets()
        data = reader.read()
        for row in data:
            planet = Planet(
                name=row['name'],
                mass=float(row['mass']),
                radius=float(row['radius']),
                distance=float(row['distance']),
                habitable=row['habitable'].strip().lower() == 'true'
            )

            planet_list.append(planet)

        return planet_list

    def add_planet(self, planet):
        """
        Add a planet to the solar system if it does not already exist.
        """

        for existing in self.planets:
            if existing.name.lower() == planet.name.lower():
                return False
        else:
            self.planets.append(planet)
            return True

    def find_habitable_planets(self):
        """
        Find and return all habitable planets in the solarsystem"""
        
        return [planet for planet in self.planets if planet.habitable]
    
    def __str__(self):
        result = f'{self.name}:\n  {self.star}\n'
        for planet in self.planets:
            result += (f"  {planet.name}: Mass={planet.mass:.2e} kg, Radius={planet.radius} km, "
                    f"Distance={planet.distance_from_sun} million km, "
                    f"Orbital Speed={planet.calculate_orbital_speed()} km/s "
                    f"Surface Gravity={planet.calculate_surface_gravity()}  m/s^2\n\n")
            
        return result
    

""" this is string representation of the solar system class which includes name of the solar system star and planets with relevant attributes such as mass radius distance etc"""

