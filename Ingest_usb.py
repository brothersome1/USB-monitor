# ingest_usb.py
import pandas as pd
import json

LOG_PATH = r"C:\USBMonitor\usb_events.json"

def load_events():
    with open(LOG_PATH, "r") as f:
        lines = f.readlines()
    events = [json.loads(line) for line in lines]
    return pd.DataFrame(events)

df = load_events()
print(df.tail())
