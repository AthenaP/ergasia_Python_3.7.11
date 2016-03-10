import pyowm

owm = pyowm.OWM('e1d08c400e77df9b80ec04581a73b2aa')  

lat = input('Enter Latitude: ')
lon = input('Enter Longitude: ')

observation = owm.weather_at_coords(lat,lon)
w = observation.get_weather()  
temp = w.get_temperature(unit='celsius')  
current_temp = temp['temp']
l = observation.get_location()
print(l.get_name())
print(w.get_status())  
if w.get_status() == 'Rain':
    print("I'm singing in the rain!")
print(current_temp)
if current_temp > 20:
    print("nice...")
elif current_temp < 5:
    print("brrrr")
