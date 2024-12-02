import requests                 # for creating the HTTP request
import math                     # for generating random values
import time                     # for waiting (sleep) after sending a request

# REMOVED: API_KEY = "XXXXXXXXXXXXXXXX"
SETS = 5                        # number of measurements to generate and send

def generate_random_data(round:int) -> tuple:
    """
    Generates random values for pressure, temperature and humidity.
    Values are generated based on the parameter round and returned in a tuple.
    """
    pressure = 1024 + 5 * math.sin(round / 10)
    temperature = 300 + 2 * math.cos(round / 3)
    humidity = 33 + round % 50

    return (pressure, temperature, humidity)

def main():
    """
    Generates a number of sets (defined in SETS) of three measurements
    (pressure, temperature and humidity) with random values into a dictionary
    (dict). Also generates and sends a request to localserver:5000
    where the measurements are in JSON format.  
    """
    for round in range(SETS):
        # generate the data
        pressure, temperature, humidity = generate_random_data(round)

        # create a dict with the API-key and the generated data
        measurement = {} 
        # REMOVED: measurement["api_key"] = API_KEY
        # ADDED:
        measurement["id"] = round
        # CHANGED: "field1" => "pressure":
        measurement["pressure"] = pressure
        # CHANGED: "field2" => "temperature":
        measurement["temperature"] = temperature
        # CHANGED: "field3" => "humidity":
        measurement["humidity"] = humidity

        # transform the dict to json format and send it using HTTP POST

        # REPLACED: response = requests.post('https://api.thingspeak.com/update.json',
        #                         json = measurement)
        response = requests.post('http://localhost:5000/newmeasurement/',
                                 json = measurement)

        # check the result (based on the HTTP response)
        if response.ok == True:
            print("Data sent successfully.")
            # print(response.json())
        else:
            print("Failed to send the data.")

        # CHANGED: wait for 3 seconds
        time.sleep(3)

if __name__ == "__main__":
    main()