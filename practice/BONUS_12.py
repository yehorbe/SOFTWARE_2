import requests, json


state=input('Enter the country code:')

request=f'https://restcountries.com/v3.1/name/{state}'
response=requests.get(request).json()

country_name = response[0]["name"]["official"]
capital_city = response[0]["capital"][0]
population = response[0]["population"]

print(f"Official Name: {country_name}")
print(f"Capital: {capital_city}")
print(f"Population: {population}")