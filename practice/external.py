import requests, json

keyword = input("Enter keyword: ")
request = "https://api.tvmaze.com/search/shows?q=" + keyword

response = requests.get(request).json()

print(response)
print(len(response))

print(json.dumps(response,indent=2))
# for a in response:
#     print(a["show"]["name"])