import logging
import sys
import os.path

try:
    import serial
except ImportError:
    me = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0,os.path.join(me,'pyserial25'))
    logging.getLogger(__name__).info("Using local copy of pyserial")
    import serial

def get_ports():
    ports = [serial.device(i) for i in range(5)]
    if os.name == "posix":
        for device in ["/dev/ttyUSB%d" % i for i in range(5)]:
            if os.path.exists(device):
                ports.append(device)
    return ports

def get_speeds():
    return [9600, 19200, 38400, 57600, 115200]
