#
# trig.py -> h4-2
#

import math

# example shown in handout: mimic this for the three given trig identities

theta_degrees = float(input("Enter theta in degrees: "))
theta_radians = math.radians(theta_degrees)
print ("theta_degrees in radians (theta_radians) is:", theta_radians)
print ("The formula is: sin(theta_radians)=cos(PI/2.0 – theta_radians):")
print ("Substituting into the formula gives: sin(",theta_radians,") = cos(",math.pi/2.0 - theta_radians,")")
print ("The left side is:",math.sin(theta_radians))
print ("The right side is:", math.cos(math.pi/2.0 - theta_radians))

# the first identity is done for you - almost!

# sin(x+y) = sin(x)*cos(y) + cos(x)*sin(y)

x_degrees = float(input("Enter x in degrees: "))
y_degrees = 0.0 # read float from console

x_radians = 0.0 # fix this conversion
y_radians = math.radians(y_degrees) #

print (f"x_degrees in radians (x_radians) is: {x_radians}")
print (f"y_degrees in radians (y_radians) is: {y_radians}")
print ("The formula is: sin(x_radians+y_radians) = sin(x_radians)*cos(y_radians) + cos(x_radians)*sin(y_radians)")
print (f'Substituting into the formula gives: sin({x_radians+y_radians}) = sin({x_radians})*cos({y_radians}) + cos({x_radians})*sin({y_radians})')
print (f'The left side is: {math.sin(x_radians+y_radians)}')
print (f'The right side is: {math.sin(x_radians)*math.cos(y_radians) + math.cos(x_radians)*math.sin(y_radians)}')

# now do the same for the other two identities...

# cos(x+y) = cos(x)*cos(y) - sin(x)*sin(y)


# tan(x+y) = (tan(x) + tan(y)) / (1 – tan(x)*tan(y))