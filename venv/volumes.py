from math import pi

#cube function that asks for input, calculates and returns the volume.
def cubevolume():
    cubelength = int(input("Enter a side length: "))
    c_vol = abs(cubelength**3)
    e_vol = round(e_vol,3)
    print("The volume of a cube with a side length of {} is: {}".format(cubelength,c_vol))
    return c_vol

#pyramid function that asks for input, calculates and returns the volume.
def pyramidvolume():
    pybase = int(input("Enter a base length: "))
    pyheight = int(input("Enter a height: "))
    p_vol = 1/3 * (pybase**2 * abs(pyheight))
    p_vol =round(p_vol,3)
    print("The volume of a pyramid with a base of {} and a height of {} is: {}".format(pybase,pyheight,p_vol))
    return p_vol

#ellipsoid
#  function that asks for input, calculates and returns the volume.
def ellipsoidvolume():
    r1 = int(input("Enter a radius: "))
    r2 = int(input("Enter another radius: "))
    r3 = int(input("Enter the last radius: "))
    e_vol = abs(4/3*pi * r1 * r2 * r3)
    e_vol = round(e_vol,3)
    print("The volume of an ellipsoid with the radiuses {}, {} and {} is: {}".format(r1,r2,r3,e_vol))
    return e_vol
