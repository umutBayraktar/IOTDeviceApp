#!/usr/bin/env python3

import selectors
import socket
import sys
import traceback
import libclient
from decouple import config
import random
import time

sel = selectors.DefaultSelector()


def create_request_data():
    devices = ["device1", "device2", "device3", "device4", "device5"]
    latitude = round(random.uniform(36,42), 15)
    longitude = round(random.uniform(26,45), 15)
    timestamp = time.time()
    device = random.choice(devices)
    return device, latitude, longitude, timestamp


def create_request():
    device, latitude, longitude, timestamp = create_request_data()
    return dict(
        type="text/json",
        encoding="utf-8",
        content=dict(device=device, latitude=latitude, longitude=longitude, timestamp=timestamp),
    )


def start_connection(host, port, request):
    addr = (host, port)
    print(f"Starting connection to {addr}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = libclient.Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)


host = config("HOST", default="localhost")
port = config("PORT", default=65432)

request = create_request()
start_connection(host, port, request)

try:
    while True:
        events = sel.select(timeout=1)
        for key, mask in events:
            message = key.data
            try:
                message.process_events(mask)
            except Exception:
                print(
                    f"Main: Error: Exception for {message.addr}:\n"
                    f"{traceback.format_exc()}"
                )
                message.close()
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
