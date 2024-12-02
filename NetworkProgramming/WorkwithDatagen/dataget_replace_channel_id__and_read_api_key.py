import requests
import time

INTERVAL = 30 # at least 15 s (because of ThingSpeak free account limitation)

def main():
    """
    Fetches a field value (field2) from ThingSpeak using a request according
    to ThingSpeak's REST API.
    """
    full_data = {}
    feed_data = []
    data = {}
    temperature = 0.0

    while (True):
        # send a GET request

        # replace AAAAAAA with your channel id and
        # BBBBBBBBBBBBBBBB with you channel's read api key 
        response = requests.get('')

        # handle response
        if response.ok == True:
            # print the field value
            full_data = response.json()
            print(full_data)

            feed_data = full_data["feeds"]
            print(full_data["feeds"])
            
            data = feed_data[0]
            print(feed_data[0])

            print(data["field2"])
        else:
            print("Data could not be retrieved.")

        # odota 
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()