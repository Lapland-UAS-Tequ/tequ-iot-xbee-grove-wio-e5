# tequ-iot-xbee-grove-wio-e5
XBee 3 based datalogger that uses Grove Wio-E5 module to send data to LoRaWAN network.

## Hardware
| Hardware               | Model            | Link           |
| -------------          |:-------------:   | :-------------:|
| Main computer | XBee Digi 3 | <a href="https://www.digi.com/products/embedded-systems/digi-xbee/rf-modules/2-4-ghz-rf-modules/xbee3-zigbee-3">Link</a>|
| Computer board | XBee Explorer USB-C | <a href="https://www.sparkfun.com/products/22043">Link</a>|
| LoRaWAN module | Grove Wio-E5 | <a href="https://www.seeedstudio.com/Grove-LoRa-E5-STM32WLE5JC-p-4867.html">Link</a>|
| Voltage/Current/Power sensor | Adafruit INA260 | <a href="https://www.adafruit.com/product/4226">Link</a>|
| Temperature sensor | Sparkfun TMP102 | <a href="https://www.sparkfun.com/products/13314">Link</a>|


## Connections
Connections of the hardware used. 
| Device                        | PIN            | Device             | PIN            | 
| ----------------------------- |:--------------:| :-----------------:| :-------------:|
| XBee Explorer USB-C | VIN | Battery | + |
| XBee Explorer USB-C | GND | Battery | - |

| XBee Explorer USB-C | 3V3 | INA260 | VCC |
| XBee Explorer USB-C | GND | INA260 | GND |
| XBee Explorer USB-C | SDA(7) | INA260 | SDA |
| XBee Explorer USB-C | SCL(19) | INA260 | SCL |

| XBee Explorer USB-C | 3V3 | TMP102 | 3V3 |
| XBee Explorer USB-C | GND | TMP102 | GND |
| XBee Explorer USB-C | SDA(7) | TMP102 | SDA |
| XBee Explorer USB-C | SCL(19) | TMP102 | SCL |

| XBee Explorer USB-C | 3V3 | Grove Wio-E5 | 3V3 |
| XBee Explorer USB-C | GND | Grove Wio-E5 | GND |
| XBee Explorer USB-C | TX(2) | Grove Wio-E5 | TX |
| XBee Explorer USB-C | RX(3) | Grove Wio-E5 | RX |

## Setup
### 1. Download and install PyCharm
Programming of the XBee modules is done easiest with PyCharm, download it and install it from <a href="https://www.jetbrains.com/pycharm/download/?section=windows">here</a>.

Once installed, open the `plugins` tab and download the `Digi XBee` plugin.

### 2. Download repository code and open
Download this repository's code as a ZIP file or clone it directly to your device. Unpack the ZIP file somewhere.

Next open up PyCharm and navigate to `File -> Open...`. From the pop-up window, find where you unpacked this repository's code and open the folder, this will create a PyCharm project out of it. The code should already contain all the required libraries. 

### 3. Verify operation
Upload the code to the built device and check that it is sending data to your LoRaWAN server.

## NOTE
The XBee 3 that is used here only has 1 UART line which means that both the USB and the Wio-E5 UART connection are on the same line. This causes messages and commands sent to one device appear for the other. The Wio-E5 shouldn't get confused with normal print statements intented for the PC connected, but it may confuse the user 
