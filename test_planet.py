import unittest 
from planet import Planet 

class TestPlanet(unittest.TestCase): 
    
    def setUp(self):
        ''' creating example objects across sevaral test cases '''
        ''' to test the attributes I have created two test planets , earth and jupiter '''

        self.earth = Planet("Earth", 5.97e24, 6371, 1.496e8, 365.25)
        self.jupiter = Planet("Jupiter", 1.9e27, 69911, 7.78e8, 4333)
    
    def test_planet_attributes(self): 
        ''' test that each instance has its attributes assigned properly'''
        self.assertEqual(self.earth.name,"Earth")
        self.assertEqual(self.earth.mass, 5.97e24)
        self.assertEqual(self.earth.radius, 6371)
        self.assertEqual(self.earth.distance_from_sun, 1.496e8)
        self.assertEqual(self.earth.orbital_period, 365.25)
        '''testing for the second planet object jupiter to ensure attributes are properly assigned'''

        self.assertEqual(self.jupiter.name,"Jupiter")
        self.assertEqual(self.jupiter.mass, 1.9e27)
        self.assertEqual(self.jupiter.radius, 69911)
        self.assertEqual(self.jupiter.distance_from_sun, 7.78e8)
        self.assertEqual(self.jupiter.orbital_period, 4333)
        ''' thus testing that the attributes of the planet class are properly assigned during initialization'''
    def test_orbital_speed(self): 
        self.assertIsInstance(self.earth.orbital_speed(), float)
        self.assertIsInstance(self.jupiter.orbital_speed(), float)
        ''' testing that the orbital speed method returns a float value for both planets'''
    def test_surface_gravity(self): 
        self.assertIsInstance(self.jupiter.surface_gravity(), float)
        self.assertIsInstance(self.earth.surface_gravity(), float)
        
        ''' testing that the surface gravity method returns a float value for both planets'''
       
        ''' testing that the methods for calculating orbital speed and gravity are worlking and returning the correct data types '''
    def test_get_info(self): 
        info = self.earth.get_info()
        info = self.jupiter.get_info()
        expected_keys = { "name" 
                        , "mass" 
                        , "radius"
                        , "distance_from_sun"
                        , "orbital_period"} 
        self.assertEqual(set(info.keys(), expected_keys))
        ''' testing that the get into method returns a dictionary with expected keys '''
    def test_planet_type_terrerstrial(self):
        self.assertEqual(self.earth.planet_type(), "Terrestrail")
        self.assertEqual(self.jupiter.planet_type(), "Terrestrial")

        ''' testing that the planet type method correctly classifies the planetsbased on their attributes'''

    def test_planet_type_gas_giant(self):
        self.assertEqual(self.earth.planet_type(), "Gas Giant") 
        self.assertEqual(self.jupiter.planet_type(), "Gas Giant")
        ''' testing so for every possible output of planet type ensuring it is behaving properly'''
    def test_planet_type_unknown(self): 
        self.assertEqual(self.earth.planet_type(), "Unknown") 
        self.assertEqual(self.jupiter.planet_type(), "Unknown")
        '''testing for every possible output of planet type ensuring it is behaving properly''' 
    def test_ishabitableTrue(self): 
        self.assertTrue(self.earth.is_habitable(),)
        self.assertTrue(self.jupiter.is_habitable(),)
        ''' testing for another output'''
        
    def test_ishabitableFalse(self): 
        self.assertFalse(self.earth.is_habitable())
        self.assertFalse(self.jupiter.is_habitable())
    
    if __name__ == '__main__': 
        unittest.main() 
        


    
    ''' this testing class tests the planet class and its methods using two setup data sets , it tests all the relevant attributes and methods and also incorporates class interaction by importing the previous class '''

    
    


    