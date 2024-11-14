# query_arduino.py
import serial, time
query="A0?\n"
ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
time.sleep(1)     # aguarda ate a serial estar pronta
ser.write(query)
time.sleep(0.1)
reply=ser.readline()
print(reply.strip())
ser.close()