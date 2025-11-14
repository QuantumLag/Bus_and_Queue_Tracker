import time
import random
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

def simulate_bus(route, start_lat, start_lon):
    lat = start_lat
    lon = start_lon
    i = 30
    while i > 0 :
        lat += random.uniform(-0.0005, 0.0005)
        lon += random.uniform(-0.0005, 0.0005)

        coordinates = { "latitude" : lat, "longitude" : lon}

        print(f"Updating {route}: {lat}, {lon}")

        resp = requests.patch(f"{FASTAPI_URL}/bus/{route}/location", json = coordinates)
        
        if resp.status_code not in (200,201):
            print("Error:", res.text)
        
        time.sleep(5)
        i -= 1

if __name__ == "__main__":

    from threading import Thread

    buses = [
        ("375D", 12.9716, 77.5946),
        ("410FA", 12.9453, 77.6275),
        ("NICE5K", 13.0067, 77.6060)
    ]

    for b in buses:
        Thread(target=simulate_bus, args=b).start()
