import u6
import time
import Pump as P

TIMEOUT = 70 #time out for detecting bubble
THRESHOLD = 2 #Threshold for bubble detection

d = u6.U6()
print (d.configU6())
print (d.getCalibrationData())
d.writeRegister(50590, 15)
print (d.configU6())
print (d.getCalibrationData())




if __name__ == "__main__":    
    p1 = P.Pump("COM9")
    # p1.pump_Zinit(1)
    # time.sleep(1)    
    p1.set_speed(1,1000)
    time.sleep(1)
    p1.set_pos_absolute(1, 0)
    time.sleep(3)
    p1.set_speed(1,100)
    time.sleep(1)
    
    p1.set_pos_absolute(1, 10000)

    
    start_time = time.time()
    # check the bubble sensor. Stop if bubble detected
    while (True):
        # print('-------------------')
        input0 = (d.getAIN(0))
        
        print('----------------',input, 'position:', p1.get_plunger_position(1))
        # print('----------------',input)
        # input1 = (d.getAIN(1))
        # input2 = (d.getAIN(2))
        # input3 = (d.getAIN(3))
        # input4 = (d.getAIN(4))
        # input5 = (d.getAIN(5))

        run_time = time.time() - start_time        
        if ((input0 < THRESHOLD)   or (run_time > TIMEOUT)):
            p1.stop(1)
            break
        # print("AI0={:0.2f}".format(input0))
        time.sleep(1)

    

