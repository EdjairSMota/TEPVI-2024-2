# single_request.py
import serial, time
ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
time.sleep(2)        # espera ate a serial ficar pront
ser.write(b"A0?\n")  # notacao abreviada para a codificacao
time.sleep(0.1)
reply=ser.readline().decode('utf-8')
print(int(time.time()), reply[3:].strip())
ser.close()
