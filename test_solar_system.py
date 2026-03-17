import unittest 
from planet import Planet
from solar_system import SolarSystem 
''' writing unittests for solar system class to test the attributes and methods of this class'''

class TestSolarSystem(unittest.TestCase):
       
    def setUp(self):
        self.star = Star("Sun", 1.99e30, "G-type")
        self.system = SolarSystem("TestSystem", self.star)
          
        ''' testing solar system class by running unittests for attributes'''


    

        """testing solar system class by running unittests for their attributes """
    def test_solar_system_attributes(self):
        solar_system = SolarSystem("Solar System" ,self.star) 
        self.assertEqual(solar_system.name, "Solar System") 
        self.assertEqual(solar_system.star, self.star) 
        self.assertEqual(solar_system.planets, [])
     #Tests that the attributes of solarsystem class are properly assigned during initialization
 
    def test_add_planet_success(self):
        """
        Test adding a new planet not already in the solar system.
        """
        venus = Planet("Venus", 4.867e24, 6051.8, 0.723,  8.87)  # initializing attribute 
        result = self.system.add_planet(venus) # setting up a result 
        self.assertTrue(result) 
        self.assertIn(venus, self.system.planets)

    def test_add_planet_duplicate(self):
        """
        Test adding a duplicate planet (case-insensitive) is rejected.
        """
        duplicate_earth = Planet("earth", 5.972e24, 6371, 1.0, 9.81) 
        result = self.system.add_planet(duplicate_earth)
        self.assertFalse(result)
        self.assertEqual(len([p for p in self.system.planets if p.name.lower() == "earth"]), 1)

    def test_find_habitable_planets(self):
        """
        Test that find_habitable_planets returns only habitable planets.
        """
        earth = Planet("Earth", 5.97e24 , 6371 , 1.496e8 , 365.25 , 9.81 )  # initializing attribute
        habitable = self.system.find_habitable_planets() # the result 
        self.assertEqual(len(habitable), 1) # assert equal for testing 
        self.assertEqual(habitable[0].name, "Earth") # assert equal for testing 

    def test_planet_attributes_types(self):
        """
        Test that planet attributes are correctly converted to proper types.
        """
        earth = next(p for p in self.system.planets if p.name == "Earth")
        self.assertIsInstance(earth.mass, float)
        self.assertIsInstance(earth.radius, float)
        self.assertIsInstance(earth.distance, float)
        self.assertIsInstance(earth.habitable, bool)
        self.assertIsInstance(earth.surface_gravity, float)


if __name__ == "__main__":
    unittest.main()



""" class with unittests for solar system class """