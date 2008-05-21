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
    'one': 20.,
    'two': 20.,
    'three': 20.
    }
    
# and pass them to shoebox
setvars(variables)
    

def block(x,y,z,hue): 
    '''
    draw an isometric square prism; x,y are the coordinates of 
    the BOTTOM-CENTER corner, z is the height
    '''
    #TODO : variables for width+depth instead of fixed value
    
    # no strokes in the inside
    nostroke()
    
    # LEFT FACE
    # first, set the color
    c = color(hue,40,120)
    fill(c)
    # and draw the path
    beginpath(x,y)
    lineto(x-20,y-10)
    lineto(x-20,y-10-z)
    lineto(x,y-z)
    endpath()

    # RIGHT FACE
    c = color(hue,40,80)
    fill(c)
    beginpath(x,y)
    lineto(x+20,y-10)
    lineto(x+20,y-10-z)
    lineto(x,y-z)
    endpath()

    # TOP FACE
    c = color(hue,40,40)
    fill(c)
    beginpath(x,y-z)
    lineto(x+20,y-10-z)
    lineto(x,y-20-z)
    lineto(x-20,y-10-z)
    endpath()

    # CONTOUR
    # now, we'll make a stroke around the faces
    # set the color
    c = color(hue,40,20)
    # set the stroke
    stroke(c)
    # and unset fill
    nofill()
    # draw the path
    beginpath(x,y)
    lineto(x-20,y-10)
    lineto(x-20, y-10-z)
    lineto(x, y-20-z)
    lineto(x+20, y-10-z)
    lineto(x+20, y-10)
    endpath()    

def setup():
    # set the colour range to 255
    colorrange(255)
    colormode(HSB)
      
def draw():
    # khaki background
    background(76, 102, 51)
    
    block(50, 180, one, hue=30)
    block(100, 180, two, hue=120)
    block(150, 180, three, hue=210)
    
    
