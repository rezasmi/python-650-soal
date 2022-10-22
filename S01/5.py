v_wind=float(input('give me a number '))
t_height=float(input('give me a number '))
wci=3.12+0.615*t_height-11.37*v_wind**0.16+0.3965*t_height*v_wind**0.16

print('the wind cill index is ',int(round(wci, 0)))

