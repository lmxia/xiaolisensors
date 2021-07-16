# -*- coding: utf-8 -*-

# from xiaolisensor import temperature

# tempHum = temperature.Temp_Hum()
# print(tempHum.get_temperature())


from xiaolisensor import  light
light_sensor = light.Light()
if light_sensor.shiny_or_dark():
    print("dark now")
else:
    print("bling bling")
