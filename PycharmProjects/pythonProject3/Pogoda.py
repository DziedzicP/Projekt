import requests, json

tempe = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Denver&appid=7c071f3544f19e65a3289ef9fb1f05e6&units=metric')

if tempe:
    print ('Prawidłow pobrano informacje')
else:
    print ('Błąd')

x = tempe.json()

print ('Temperatura')
print(x['main']['temp'], 'st*C')
print ('Pogoda')
print(x['weather'][0]['main'])



