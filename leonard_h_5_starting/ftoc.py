#Andrew leonard
# ftoc.py -> h5-1
#

# formula for converted Fahrenheit f to Celsius c:
#
# c = (f-32.0) * (5/9)
#

def f2c(fahr):
    celsius = (fahr-32.0) * (5/9)
    return round(celsius, 2)

def main():
    fahr = float(input("enter a farenheit temp as a float: "))
    celsius = f2c(fahr)
    print (f'{fahr} degrees F is to {celsius} degrees C')

main()