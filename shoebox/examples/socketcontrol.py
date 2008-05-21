'''

socketcontrol.py
=-=-=-=-=-=-=-=-

simplest example possible of external vars usage in Shoebox

copyleft 2008 ricardo lafuente
licensed under the GPLv3

this file is part of Shoebox

'''

size(200,200)

# create the variables we want to use in the script
# and that should be accessible from outside;
#
# the values set here will be used if we use Shoebox
# to create a still image instead of a GTK window.
#
# NOTE that only floats are accepted for the moment

variables = {
    'one': 186.,
    'two': 186.,
    'three': 93.
    }
    
# and pass them to shoebox
setvars(variables)
    
def setup():
    # set the colour range to 255
    colorrange(255)
      
def draw():
    # khaki background
    background(76,102,51)
    
    # use the outside variables to set the fill
    red = one
    green = two
    blue = three
        
    fill(red, green, blue)
    
    # draw the shape
    star(100, 100, 20, outer=25, inner=15)

