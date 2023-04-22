import time
import os
import argparse

from tqdm import tqdm
import serial


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--folder_path",
                default="received_files",
                type=str,
                help="path to saved file")

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
folder_path = args["folder_path"]

os.makedirs(folder_path, exist_ok=True)




ser = serial.Serial(port=port,
                    baudrate=boudrate,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=0)

print("connected to: " + ser.portstr)


flag_receiving_start = False
flag_receiving_end = True
delay_receving = 0.1
start_receiving_time = 0.0
received_filename = ""

received_bytes = []
while True:

     for line in ser.read():
          received_bytes.append(line)

          flag_receiving_start = True
          flag_receiving_end = False
          start_receiving_time = time.time()

          if received_filename != "":
               pbar.update(1)


     end_receving_time = time.time()

     if (end_receving_time - start_receiving_time) > delay_receving:
          flag_receiving_start = False
          flag_receiving_end = True
          

     if flag_receiving_end and (len(received_bytes) > 0):

          if received_filename == "":
               received_filename = bytes(received_bytes).decode('ascii')
               received_filename, len_file = received_filename.split(",")
               print(received_filename, len_file)
               
               if int(len_file) > 0:
                    pbar = tqdm(total=int(len_file))
               else: 
                   with open(os.path.join(folder_path, received_filename), "wb") as f: #write empty files
                        f.write(b"") 
                   received_filename = ""

          else:
               with open(os.path.join(folder_path, received_filename), "wb") as f : #write non-empty files
                    f.write(bytes(received_bytes))

               print(f"{received_filename} is writed!!!")
               received_filename = ""
               #break

          received_bytes = []

ser.close()
