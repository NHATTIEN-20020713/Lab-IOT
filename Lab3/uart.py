import serial.tools.list_ports
# import random
# import time
# import  sys
# from  Adafruit_IO import  MQTTClient
# real, com3 for hercules, com4 for python
# virtual, com2 for hercules, com3 for python
# echo "!1:T:60.38##!2:H:71.88##!3:L:300.14##" > /dev/pts/2, 2 can be another number when socat in wsl again be careful
# echo "!1:T:35.23##!2:H:60.27##!3:L:200.96##" > /dev/pts/2

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    # return commPort
    # return "COM4" # directly return
    return '/dev/pts/4'

if getPort() != "None": # check if getPort is successful
    ser = serial.Serial(port=getPort(), baudrate=115200)
    print(ser)

# mess = ""
def processData(client, data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        client.publish("sensor_1", splitData[2])
    elif splitData[1] == "H":
        client.publish("sensor_2", splitData[2])
    elif splitData[1] == "L":
        client.publish("sensor_3", splitData[2])

mess = ""
def readSerial(client):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("utf-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(client, mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def writeData(data):
    ser.write(str(data).encode("utf-8"))
# while True:
#     readSerial()
#     time.sleep(1)