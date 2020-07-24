import maya.cmds as cmds

#Create a function  with two parameters by default
# The number of teeth is the subdivisions multiply by 2
def createGear(teeth=10, length=0.3):
    print "Creating Gear", teeth, length