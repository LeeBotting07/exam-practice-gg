import requests
import threading

def call_weather():
    url = "https://task-2-wepl.onrender.com/weather"
    params = {"city": "London"}
    responce = requests.get(url, params=params)
    responce.raise_for_status()
    return "success"

def thread_target():
    try:
        result = call_weather()
        print(result)
    except requests.RequestException as e:
        print("API call failed:", e)

if __name__ == "__main__":
    while True:
        threads = []
        for _ in range(1000000000000000000000):
            t = threading.Thread(target=thread_target)
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()