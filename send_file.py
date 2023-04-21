import time
import os
import argparse

import serial


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--file_path",
                required=True,
                type=str,
                help="path to file")

ap.add_argument("-p", "--port",
                default="/dev/ttyUSB0", #Replace ttyUSB0 with ttyAM0 for Pi1,Pi2,Pi0 and ttyUSB0 with ttyS0 for Pi3,Pi4
                type=str,
                help="port that use for transfer data")

ap.add_argument("-b", "--boudrate",
                default=115200,
                type=int,
                help="transfer boudrate")


args = vars(ap.parse_args())

port = args["port"]
boudrate = args["boudrate"]
filename = args["file_path"]
base_filename = os.path.basename(filename)



ser = serial.Serial(
        port=port,
        baudrate=boudrate,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0,
)


content = open(filename,"rb").read()

ser.write(f"{base_filename},{len(content)}".encode("ascii"))
time.sleep(0.2)

ser.write(content)
print(f"{base_filename} sended!!!")
ser.close()