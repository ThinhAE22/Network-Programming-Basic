import requests #genererate http request
import time #default library in python. generate 15s delay between each request
import math #generate random value

API_KEY = "" #API KEY
SETS = 5

def generate_random_data(round:int) -> tuple:
    pressure = 1024 + 5  * math.sin(round/10)
    temperature = 300 + 2  * math.cos(round/10)
    humidity = 33 + 5  * round%10

    return (pressure, temperature, humidity)


def main():

    '''
        Generate some json data of sensor and POST them to thingspeak
    '''
    #pass
    for round in range(SETS):
        pressure, temperature, humidity = generate_random_data(round)

        measurements = {}
        measurements["api_key"] = API_KEY
        measurements["field1"] = pressure
        measurements["field2"] = temperature
        measurements["field3"] = humidity

        response = requests.post("https://api.thingspeak.com/update.json", json = measurements)
        
        if (response.ok == True):
            print("Data sent successfully.")
        else:
            print("Fail to sent data")

        time.sleep(16)

if __name__ == "__main__":
    main()