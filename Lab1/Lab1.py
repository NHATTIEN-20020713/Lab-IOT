#from http import self.client
import sys
from Adafruit_IO import MQTTClient
import time 
import random

class Adafruit_MQTT:
    AIO_FEED_IDs = ["button_1", "button_2"]
    AIO_USERNAME = "Nhat_Tien_2002"
    AIO_KEY = "aio_NArt58FYoM575sjz7Y4S6UCPmZzo"
    client = MQTTClient(AIO_USERNAME , AIO_KEY)
    counter = 10
    sensor_type = 1
    
    def connected(self, client):
        print("Connected...")
        for feed in self.AIO_FEED_IDs:
            self.client.subscribe(feed)

    def subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed...")

    def disconnected(self, client):
        print("Disconnected...")
        sys.exit(1)

    def message(self, client ,feed_id, payload):
        print("Received: " + payload)

    def __init__(self):
        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.message
        self.client.on_subscribe = self.subscribe
        self.client.connect()
        self.client.loop_background()
        
        
user_1 = Adafruit_MQTT()

while True:
    user_1.counter = user_1.counter - 1
    if user_1.counter <= 0:
        user_1.counter = 10
        print("Recorded data is publishing")
        if user_1.sensor_type == 1:
            temperature = random.randint(25, 75) 
            print("Temperature is", str(temperature) + "°C")
            user_1.client.publish("sensor_1", str(temperature) + "°C")
            user_1.sensor_type = 2
        elif user_1.sensor_type == 2:
            humidity = random.randint(15, 85)
            print("Humidity is", str(humidity) + "%")
            user_1.client.publish("sensor_2", str(humidity) + "%")
            user_1.sensor_type = 3
        elif user_1.sensor_type == 3:
            luminous_intensity = random.randint(35, 480)
            print("Luminous intensity is", str(luminous_intensity) + "lx")
            user_1.client.publish("sensor_3", str(luminous_intensity) + "lx")
            user_1.sensor_type = 1
            
        time.sleep(2)
    #print("successfully connected")