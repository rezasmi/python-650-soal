from math import pi,tan

side_lenght=float(input('give me a number '))
num_of_sides=int(input('give me a number '))

masahat_=(num_of_sides*side_lenght**2)/(4*tan(pi/num_of_sides))
print(masahat_)

