import requests, json
api="db0c848403918b27dbfc022003ae213a"
munic=input("Enter the city: ")
request = f"https://api.openweathermap.org/data/2.5/weather?q={munic}&appid={api}"
response = requests.get(request).json()

description=response["weather"][0]["description"]
temp_kelvin=response["main"]["temp"]
temp_celc=temp_kelvin - 273.15

print(f"Weather: {description}")
print(f"Temperature: {temp_celc}")