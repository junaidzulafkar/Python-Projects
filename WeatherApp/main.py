import  requests
import  json
text = input("Enter You City Name: ")
url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={text}" # Using API
r = requests.get(url)
# print(r.text)
dweather = json.loads(r.text)
print("Name: ",dweather["location"]["name"])
print("Region: ",dweather["location"]["region"])
print("Country: ",dweather["location"]["country"])
print("Localtime: ",dweather["location"]["localtime"])
print("Temperature: ",dweather["current"]["temp_c"])
print("Fahrenheit: ",dweather["current"]["temp_f"])
print("condition: ",dweather["current"]["condition"]["text"])
print("Cloud: ",dweather["current"]["cloud"],'%')
print("Humidity: ",dweather["current"]["humidity"],'%')

































































































































































































































































































































































































































































