#from http import self.client
import sys
from Adafruit_IO import MQTTClient
import time 
import random

class Adafruit_MQTT:
    AIO_FEED_IDs = ["button1", 	"button2"]
    AIO_USERNAME = "NPNLab_"
    AIO_KEY = "aio_NArt58FYoM575sjz7Y4S6UCPmZzo"
    client = MQTTClient(AIO_USERNAME , AIO_KEY)
    counter = 10
    sensor_type = 0
    
    def connected(self, client):
        print("Connected...")
        for feed in self.AIO_FEED_IDs:
            self.client.subscribe(feed)

    def subscribe(self, client , userdata , mid , granted_qos):
        print("Subscribed...")

    def disconnected(self, client):
        print("Disconnected...")
        sys.exit (1)

    def message(self, client , feed_id , payload):
        print("Received: " + payload)

    def __init__(self):
        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.message
        self.client.on_subscribe = self.subscribe
        self.client.connect()
        self.client.loop_background()
        
    

object = Adafruit_MQTT()

while True:
    object.counter = object.counter - 1
    if object.counter <= 0:
        object.counter = 10
        print("Random data is publishing")
        if object.sensor_type == 0:
            print("Temperature...")
            temperature = random.randint(10, 75)
            object.client.publish("sensor_1", temperature)
        elif object.sensor_type == 1:
            print("Humidity...")
            humidity = random.randint(50, 70)
            object.client.publish("sensor_2", humidity)
        elif object.sensor_type == 2:
            print("Lightness...")
            lightness = random.randint(10, 80)
            object.client.publish("sensor_3", lightness)
    #time.sleep(1)
    #print("successfully connected")
        