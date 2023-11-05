#!/usr/bin/env python3
"""
This module is for the rotors.


"""
class Rotor():
    """
    Rotor class to be inherited by every rotor in the program.
    Rotor will contain an array of  letters.
    with their index used to refer to the letters.

    methods and attributes:
        rotate: move from one index to the next
        delete: remove the rotor
        start: set the start position of the rotor.
        position: set the rotor position in the program.
        
    """
    def __init__(self, name);
        self.name = name

