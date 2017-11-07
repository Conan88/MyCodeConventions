#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Example of comments

This is a 'real' example for how to use comments.
This is a shorter version then the python_convention.py
"""


import os
import random
import sys

import json
import xml

#import my_file


class TheDoctor():
    """Will handle everything about the doctor

    Methods
    -------
    __init__(self) :
        return : object
    time_travle(self, string(optional), int(optional)) :
        return : list
    say_cheesy_things(self) :
        return : list
    """
    def __init__(self):
        """Init for class TheDoctor

        This is the first method that's called, and it set's
        name, known_as and age for for the class object when created.

        Attributes
        ----------
        string : self.name
        string : self.known_as
        int : self.age
        boolean : has_sonic_screwdriver
        """
        self.name = "Unknown"
        self.known_as = "The Doctor"
        self.age = 2000
        self.has_sonic_screwdriver = True

    def time_travle(self, destination="", time=2047):
        """Handles time travel and returnes a planet and time

        Attributes
        ----------
        list : planets
        int : time
        return : list : planet, time
        """
        planets = ["Gallifray", "Earth", "The Library"
                    , "Raxacoricofallapatorius", "Skaro"]
        planet_number = random.randint(0, len(planets) - 1)  # index start at 0

        if destination in planets:  # if list planets contains destination
            """Short description of if statment.
            
            This comment section is optional, but usefull when the 
            if statment is complex.
            """
            return time, destination
        else:
            return time, planets[planet_number]

    def say_cheesy_things(self):
        """Handles quotes, and returnes them randomly

        Attributes
        ----------
        list : quotes : list of string quotes
        int : quote_number : random int
        return : list : quotes
        """
        quotes = ["Allons-y!", "Trust me, i'm the doctor",
                      "Fezzes are cool", "People assume that time is a strict"
                                         + " progression of cause to effect,"
                                         + " but"
                                         + " *actually* from a non-linear,"
                                         + " non-subjective viewpoint - it's"
                                         + " more like a big ball of"
                                         + " wibbly wobbly... time-y wimey..."
                                         + " stuff. "]
        quote_number = random.randint(0, len(quotes) - 1)  # index start at 0
        return quotes[quote_number]

    @staticmethod
    def companion(arg):
        """Handles companion and returnes a method

        Python suports nested methods(method inside a method).

        Attributes
        ----------
        string : name
        return : method : help_the_doctor or explore_alone

        Methods
        -------
        help_the_doctor(string) :
            returns : list
        explore_alone(string) :
            return : list
        """
        name = "Rose"

        def help_the_doctor():
            """A method that returnes a list

            Attributes
            ----------
            return : list : name and a string
            """
            return name, "is helping the doctor"

        def explore_alone():
            """A method that returnes a list

            Attributes
            ----------
            return : list : name and a string
            """
            return name, "is explore alone"

        switcher = {  # "switch case" if needed?
            0: help_the_doctor(),
            1: explore_alone()
        }

        func = switcher.get(arg)
        return func


def print_method(obj=TheDoctor()):
    """Method for handling printing"""
    print("Name:", obj.name)
    print("Known as:", obj.known_as)
    print("Age:", obj.age)
    print("Has a sonic screwdriver?", obj.has_sonic_screwdriver)
    print("Quote:", obj.say_cheesy_things())
    print("Traveled to", obj.time_travle()[1]
          , "in year", obj.time_travle()[0])
    print(obj.companion(0)[0], obj.companion(0)[1])

print_method()
