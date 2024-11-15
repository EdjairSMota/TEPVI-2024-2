# query_arduino.py
import serial, time
query="A0?\n".encode('utf-8')
ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
time.sleep(3)     # aguarda ate a serial estar pronta
ser.write(query)
time.sleep(0.1)
reply=ser.readline().decode('utf-8')
print(reply.strip())
ser.close()