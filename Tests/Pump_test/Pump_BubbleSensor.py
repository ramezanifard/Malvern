import serial
import u6
import time
TIMEOUT = 7 #time out for detecting bubble
THRESHOLD = 2 #Threshold for bubble detection

d = u6.U6()
print (d.configU6())
print (d.getCalibrationData())
d.writeRegister(50590, 15)
print (d.configU6())
print (d.getCalibrationData())


def _read( size):
    """
    Read n=size bytes from serial, if <n bytes are received (serial.read() return because of timeout), raise a timeout.
    """
    recv = ser.read(size=size)
    if len(recv) < size:
        print("miatake!!!")
    else:
        return recv
    

# setup connection to the Pump
ser = serial.Serial()
ser.baudrate = 9600
ser.timeout = 3
ser.port = 'COM8'
print(ser)
ser.open()


# move the pump 
# clear buffers
ser.reset_output_buffer()
ser.reset_input_buffer()
ser.write('/1A16000R\r\n'.encode())
ser.flush()

start_time = time.time()
# check the bubble sensor. Stop if bubble detected
while (True):
    input0 = (d.getAIN(0))
    # input1 = (d.getAIN(1))
    # input2 = (d.getAIN(2))
    # input3 = (d.getAIN(3))
    # input4 = (d.getAIN(4))
    # input5 = (d.getAIN(5))

    run_time = time.time() - start_time        
    if ((input0 > THRESHOLD)   or (run_time > TIMEOUT)):
        break
    # print("AI0={:0.2f}".format(input0))
    time.sleep(.01)

# stop the pump
ser.write('/1TR\r\n'.encode())
ser.flush()

# try:
#     cr = "\r".encode()
#     response_frame = b''
#     response_byte = _read(size=1)  # read one byte at a time, timeout is set on instance level

#     # read until stop byte
#     while response_byte != cr:
#         response_frame += response_byte
        
#         response_byte = _read(size=1)
#         print(response_byte)
# except:
#     print("excepton!!")
# else:    
#     print(response_frame)
# # res = ser.readline()

ser.close()

