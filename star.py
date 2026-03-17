"""

This module defines the Star class, representing a star
with a name, mass, and classification type as the relevant attributes
"""

class Star:
    """
    A class to represent a star.

    Attributes:
        name, mass , star type """

    def __init__(self, name, mass, star_type):
        
       

        """init method to initialize the star object with relevant attributes such as name mass star type"""

        self.name = name
        self.mass = mass
        self.type = star_type

    def __str__(self):

        """
        Return a string representation of the Star object.

            str: A formatted string describing the star.
        """

        return f"Star {self.name}: Type={self.type}, Mass={self.mass} kg"
    

    """ human readable string representtatin of the object including name mass type of star"""