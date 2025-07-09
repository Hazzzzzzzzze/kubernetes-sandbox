import requests
import threading
import time

URL = "http://localhost:8080/"
THREADS = 15
REQUESTS_PER_THREAD = 100

def spam():
    for _ in range(REQUESTS_PER_THREAD):
        try:
            requests.get(URL, timeout=2)
        except Exception as e:
            print("Error:", e)

threads = []
for _ in range(THREADS):
    t = threading.Thread(target=spam)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Done spamming!")