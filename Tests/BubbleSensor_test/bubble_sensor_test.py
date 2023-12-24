import u6
import time

THRESHOLD = 2 #Threshold for bubble detection

d = u6.U6()
print (d.configU6())
print (d.getCalibrationData())
d.writeRegister(50590, 15)
print (d.configU6())
print (d.getCalibrationData())



start_time = time.time()
# check the bubble sensor. Stop if bubble detected
while (True):
    input0 = (d.getAIN(0))
    input1 = (d.getAIN(1))
    input2 = (d.getAIN(2))
    input3 = (d.getAIN(3))
    input4 = (d.getAIN(4))
    input5 = (d.getAIN(5))
    input6 = (d.getAIN(6))
    input7 = (d.getAIN(7))
    input8 = (d.getAIN(8))
    input9 = (d.getAIN(9))
    input10 = (d.getAIN(10))
    input11 = (d.getAIN(11))
    input12 = (d.getAIN(12))
    input13 = (d.getAIN(13))


    
    print("AI0={:0.1f}".format(input0), end=',')
    print(" ,AI1={:0.1f}".format(input1), end=',')
    print(" ,AI2={:0.1f}".format(input2), end=',')
    print(" ,AI3={:0.1f}".format(input3), end=',')
    print(" ,AI4={:0.1f}".format(input4), end=',')
    print(" ,AI5={:0.1f}".format(input5), end=',')
    print(" ,AI6={:0.1f}".format(input6))

    
    print("AI7={:0.1f}".format(input7), end=',')
    print(" ,AI8={:0.1f}".format(input8), end=',')
    print(" ,AI9={:0.1f}".format(input9), end=',')
    print(" ,AI10={:0.1f}".format(input10), end=',')
    print(" ,AI11={:0.1f}".format(input11), end=',')
    print(" ,AI12={:0.1f}".format(input12), end=',')
    print(" ,AI13={:0.1f}\n\n".format(input13),)
    time.sleep(1)
