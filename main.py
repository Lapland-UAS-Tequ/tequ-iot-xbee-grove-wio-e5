import sys
import time
from umachine import I2C
from tmp102 import Tmp102
from ina260 import INA260
from lora import Lora
from functions import log, pack_binary_data

# Setup I2C communication
bus = I2C(1)
tempSens = Tmp102(bus, 0x48)
elecSens = INA260(bus)

# Initialize Grove Wio-E5
lora = Lora()

# Time for the device to sleep between measurements and sending data, in ms
sleepTime_ms = 10000

while True:
    #log("Woken up from sleep")

    # Get sensor data
    #log("Getting sensor data...")
    temperature = tempSens.temperature
    voltage = elecSens.voltage()
    current = elecSens.current()
    power = elecSens.power()
    packedData = f"{temperature}/{voltage}/{current}/{power}"


    #dataPacket = [temperature, voltage, current, power]  # Pack data into list, modify this to add more sensor values
    #log("Sensor data got")

    # Currently not in use, since not sure if data can be sent as binary
    # Pack data to binary format
    #packedBinaryData = str(pack_binary_data(dataPacket))
    #packedBinaryData = "Hello, LoRaWAN"

    #log("Sending data...")
    lora.wake_up()  # Wake the Wio-E5 module from sleep
    lora.send_data(packedData)  # Send data to LoRaWAN server
    log("Going to sleep...")
    print("")
    #lora.sleep()  # Put the Wio-E5 module to sleep
    time.sleep_ms(sleepTime_ms)
