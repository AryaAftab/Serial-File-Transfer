# Serial-File-Transfer
File Transfer Using Serial Protocol and Python (I used these codes for file transfer between my pc and RaspberryPi 4B)

In this repository, two pieces of code are provided for sending and receiving files. Can be used for two-way sending.

## Run
First, run the ```receive_file.py``` code on receiver side.

```bash
python receive_file.py -i {path to saved file}
                       -p {port that use for transfer data}
                       -b {transfer boudrate}               
```

On Sender side, you must run ```send_file.py``` code.
```bash
python send_file.py -i {path to file}
                       -p {port that use for transfer data}
                       -b {transfer boudrate}               
```

#### Example:

***receiver:***
```bash
python receive_file.py -i "recevied_files"
                       -p "/dev/ttyUSB0"
                       -b 115200
```

***sender:***
```bash
python send_file.py -i "/path/to/file"
                       -p "/dev/ttyUSB0"
                       -b 115200
```

***Note:*** boundrate must be same in the both sides
