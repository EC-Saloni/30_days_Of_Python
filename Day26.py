import requests
import pprint #pretty print module

API_KEY = "9444d2efa8116f0bdc1b75a8637a8b8b"
city = "Lucknow"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    #Accessing and printing values
    print("---------------------------------")
    print(f"City :{data['name']}")
    print(f"Country: {data['sys']['country']}")
    print(f"Temparature: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['main']}")
    print("---------------------------------")
else:
    print("Failed to fetch data.")

#Output : 
'''
---------------------------------
City :Lucknow
Country: IN
Temparature: 35°C
Condition: Clouds
---------------------------------
'''
