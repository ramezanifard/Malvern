import time
import Pump as P

if __name__ == "__main__":
    p1 = P.Pump("COM9")
    # p1.pump_Zinit(1)
    # p1.pump_Zinit(2)
    # p1.pump_Zinit(3)
    # p1.pump_Zinit(4)
    # time.sleep(5)
    

    ##--------------- testing pump + valve1    
    p1.set_speed(1,600)
    time.sleep(2)
    p1.set_pos_absolute(1, 0)
    # time.sleep(2)
    # a = p1.get_plunger_position(1)    
    # print('plunger pos:', a)

    # time.sleep(.5)
    # a = p1.set_valve(1,'I')
    # time.sleep(.5)
    # a = p1.get_valve(1)
    # print('valve 1  pos:', a)


    # # -------------- testing 4 port valve: address=2
    # for i in ['I', 'O', 'E', 'B']:
    #     time.sleep(.5)
    #     a = p1.set_valve(2,i)  
    #     time.sleep(.5)
    #     a = p1.get_valve(2)
    #     print('valve pos:', a)



    # ##------------------- testing 3 way valvue: address=4
    # # set valve in address 4 as 3 way valve:
    # # p1.config_valve(4, 3)
    # for i in range(3):
    #     time.sleep(1)
    #     #set the positon of 6 way valve
    #     a = p1.set_multiwayvalve(4,str(i+1))
    #     time.sleep(1)    
    #     #now, read the position of 6 way valve
    #     a = p1.get_valve(4)
    #     print('valve pos:', a)



    # ##------------------- testing 6 way valvue: address=3
    # # set valve in address 4 as 3 way valve:
    # # p1.config_valve(4, 3)
    # for i in range(6):
    #     time.sleep(1)
    #     #set the positon of 6 way valve
    #     a = p1.set_multiwayvalve(3,str(i+1))
    #     # p1.set_valve(4,'I')
    #     time.sleep(1)    
    #     #now, read the position of 6 way valve
    #     a = p1.get_valve(3)
    #     print('valve pos:', a)
        


    p1.close()