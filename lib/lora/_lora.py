import time
from sys import stdin, stdout
from functions import log


class Lora:

    # Initialize the Wio-E5 module
    def __init__(self):
        log("Initializing Wio-E5...")
        response = self.send_at_command('AT+JOIN')
        if "Joined already" in response:
            log("Device already in network")
            return
        while "Done" not in response:
            response = self.receive_data()
            time.sleep_ms(1000)
        log("Connection successful")

    # Send AT command to Wio-E5
    def send_at_command(self, command, delay=1):
        self.write_data(command + '\r\n')
        time.sleep(delay)
        response = self.receive_data()
        return response

    # Receive data from stdin/Wio-E5
    def receive_data(self):
        data = stdin.buffer.readline()
        return data

    # Write data to stdout/Wio-E5
    def write_data(self, data_out):
        stdout.write(bytearray(data_out, 'utf-8'))

    # Send data to the LoRaWAN server
    def send_data(self, data):
        hex_data = data.encode('utf-8').hex()
        command = f'AT+CMSGHEX={hex_data}'
        response = self.send_at_command(command).decode('utf-8')
        #log(f"right before: {response}")
        if "ERROR" in response:
            #log(f"Error in sending data")
            return
        while "Done" not in response:
            response = self.receive_data()
            #print(response)
            time.sleep_ms(1000)
        print("Data sent succesfully")

    # Put the module to sleep, until woken up
    def sleep(self):
        command = f'AT+LOWPOWER'
        self.send_at_command(command)

    # Wake up the module
    def wake_up(self):
        self.write_data("wake up\r\n")
        time.sleep_ms(100)  # The module takes a bit of time to fully wake up
