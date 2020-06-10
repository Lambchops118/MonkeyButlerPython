import requests
from mcstatus import MinecraftServer
import cryptocompare

def temperature():
    key = "c5bbe0c6b2d7ab5f9ae92a9441d47253"
    urlBase = "http://api.openweathermap.org/data/2.5/weather?"
    nameCity = "Chadds Ford"
    urlComplete = urlBase + "appid=" + key + "&q=" + nameCity
    response = requests.get(urlComplete)
    x= response.json()

    if x["cod"] != "404":
            y = x["main"]
            current_temp = y["temp"]
            current_pres = y["pressure"]
            current_hum = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
    else:
        print("I cannot find that city.")

    temp = round(current_temp * 9/5-459.67)
    humidity = round(current_hum)
    return temp
    

def serverstatus():
    try:
        server = MinecraftServer.lookup("10.0.0.202:25565")
        status = server.status()
    except:
        status = "Error.ScrapeMinecraftServer"
    return status



##########  Output  #############

#print(str(temperature()) + " degrees fahrenheit.")
#print(serverstatus())
