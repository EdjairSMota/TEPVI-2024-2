# ask_arduino_repeat_plot.py
import serial, time, atexit
def cleanup():                  # garante que a serial seja fechada apos CTRL-C
    ser.close()
atexit.register(cleanup)        # registra a funcao cleanup
query="A0?\n".encode('utf-8')   # string da query
amin=0                          # valor minimo esperado
amax=5                          # value maximo esperado
width=70                        # numero de caracteres usados no plot
ser=serial.Serial("/dev/ttyUSB0",9600,timeout=1)
lll=len(query)-1                # necessario para remover 'A0' da resposta
time.sleep(3)                   # espera a serial estar pronta
t0=time.time()                  # tempo inicial
while 1:                        # repete para sempre
    ser.write(query)            # envia query
    time.sleep(0.1)             # espera um pouco
    reply=ser.readline().decode('utf-8')      # le a resposta
    value=reply[lll:].strip()                 # transforma para numerico
    k=int((width-2)*float(value)/(amax-amin)) # onde colocar * no plot
    p='%8.1f %4s |' % (time.time()-t0,value)
    for j in range(0,width-1):
        if j==k:
            p+='*'
        else:  
            p+=' '
    p+='|'
    print(p)
    time.sleep(1)               # espera um pouco antes da proxima medida