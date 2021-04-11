import paho.mqtt.client as mqtt
from time import sleep

def on_message(client, userdata, message):
    print(f"message received: {message.payload.decode('utf-8')}, topic: {message.topic}, retained:{message.retain}")

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Client: {client}")
    print(f"  userdata:    {userdata}")
    print(f"  mid:         {mid}")
    print(f"  granted_qos: {granted_qos}")

broker_address="18.139.115.83"
client = mqtt.Client("P1")
client.on_message = on_message
client.on_subscribe = on_subscribe
client.connect(broker_address)
client.loop_start()

topic = "bvtxn/seg101"
QoS   = 1
print(f"Subscribing to topic:{topic} with QoS={QoS}")
result, mid = client.subscribe(topic, QoS)
print(f"Result = {result}, mid = {mid}")

try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass

client.disconnect()
client.loop_stop()