import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            json_data = response.json()
            print(json_data["value"])
        else:
            print(f"Error: Could not fetch joke. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


get_chuck_norris_joke()
