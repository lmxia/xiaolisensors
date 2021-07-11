# -*- coding: utf-8 -*-

# from xiaolisensor import temperature

# tempHum = temperature.Temp_Hum()
# print(tempHum.get_temperature())


from xiaolisensor import  light
light = light.Light()
if light.shiny_or_dark():
    print("dark now")
else:
    print("bling bling")
