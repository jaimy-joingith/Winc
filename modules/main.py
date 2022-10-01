# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

#1 At the top of your main.py, import a module that prints the Zen of Python. 

import this
from xml.sax.handler import DTDHandler
print(this)

#2 Write a function wait that takes one argument -- seconds (int) -- that uses a function in the time module to make the computer wait for that number of seconds, then returns nothing.

import time
def wait(seconds):
    time.sleep(seconds)
    return

#3 Implement a function my_sin that takes one float as an argument and returns the sine of that float. Use the math module.

import math
def my_sin(x):
    return math.sin(x)

#4 Implement a function iso_now that takes no arguments and returns a string containing the current date and time up to the minute in the ISO 8601 format. Example: 2000-12-31T17:00. Use the datetime module.

import datetime
def iso_now():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")

#5 Implement a function platform that takes no arguments and returns a string that shows which platform (Linux, Windows, macOS, and so on) we are on. Use the sys module.

import sys
def platform():
    return sys.platform.lower()

#6 Create a new file greet.py, and in that file implement a function supergreeting that takes a name as an argument (str) and returns a string of the form 'Hellooo...ooo, Bob!'. Then import this function in main.py and write a function supergreeting_wrapper that takes the exact same type of argument, calls supergreeting with it and returns the result.

from greet import supergreeting

def supergreeting_wrapper(name):
    return supergreeting(name)

print (supergreeting_wrapper('Bob'))