# -*- coding: utf-8 -*-

from xiaolisensor import temperature

tempHum = temperature.Temp_Hum()
print(tempHum.get_temperature())
