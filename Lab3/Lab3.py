#from http import self.client
import sys
from Adafruit_IO import MQTTClient
import time 
import random
from simple_ai import *
from uart import *

AIO_FEED_IDs = ["button_1", "button_2"]
AIO_USERNAME = "Nhat_Tien_2002"
AIO_KEY = "aio_NArt58FYoM575sjz7Y4S6UCPmZzo"
client = MQTTClient(AIO_USERNAME , AIO_KEY)
counter = 10
sensor_type = 1
ai_counter = 5

# def __init__(self):
#     self.client.on_connect = self.connected
#     self.client.on_disconnect = self.disconnected
#     self.client.on_message = self.message
#     self.client.on_subscribe = self.subscribe
#     self.client.connect()
#     self.client.loop_background()
    
def connected(client):
    print("Connected...")
    for feed in AIO_FEED_IDs:
        client.subscribe(feed)

def subscribe(client, userdata, mid, granted_qos):
    print("Subscribed...")

def disconnected(client):
    print("Disconnected...")
    sys.exit(1)

def message(client ,feed_id, payload):
    print('Feed name: ' + feed_id + ', Received data: ' + payload)
    if feed_id == 'button_1':
        if payload == '0':
            writeData('1_0')
        else:
            writeData('1_1')
    
    elif feed_id == 'button_2':
        if payload == '0':
            writeData('2_0')
        else:
            writeData('2_1')
                    
                    
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10
    #     print("Recorded data is publishing")
    #     if sensor_type == 1:
    #         temperature = random.randint(25, 75) 
    #         print("Temperature is", str(temperature) + "°C")
    #         client.publish("sensor_1", str(temperature) + "°C")
    #         sensor_type = 2
    #     elif sensor_type == 2:
    #         humidity = random.randint(15, 85)
    #         print("Humidity is", str(humidity) + "%")
    #         client.publish("sensor_2", str(humidity) + "%")
    #         sensor_type = 3
    #     elif sensor_type == 3:
    #         luminous_intensity = random.randint(35, 480)
    #         print("Luminous intensity is", str(luminous_intensity) + "lx")
    #         client.publish("sensor_3", str(luminous_intensity) + "lx")
    #         sensor_type = 1
            
    ai_counter = ai_counter - 1
    if ai_counter <= 0:
        ai_counter = 5
        ai_result = imageDetector()
        print("AI output is", ai_result)
        client.publish("AI", ai_result)
        # time.sleep(5)
        readSerial(client)
        time.sleep(10)
    #print("successfully connected")