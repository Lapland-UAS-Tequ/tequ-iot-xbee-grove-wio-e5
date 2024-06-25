import time
import struct


def log(string):
    #logTime = time.localtime()
    #logTime = "%02d-%02d-%02d %02d:%02d:%02d" % (
    #    logTime[0], logTime[1], logTime[2], logTime[3], logTime[4], logTime[5]
    #)
    logTime = 0
    #print("%s : %s" % (logTime, string))
    print(string)


# Pack sensor data into binary to save space
def pack_binary_data(data):
    # Create identifier for data packet
    identifier = struct.pack("B", int(1))

    binaryDataPacket = identifier
    for i in data:
        binaryDataPacket += struct.pack("h", int(i*100))

    return binaryDataPacket
