import time
import Pump as P

if __name__ == "__main__":
    p1 = P.Pump("COM6")
    # p1.pump_Zinit(1)

    
    
    # p1.set_speed(1,6000)
    # time.sleep(2)
    p1.set_pos_absolute(1, 0)
    time.sleep(2)
    a = p1.get_plunger_position(1)    
    print('plunger pos:', a)



    time.sleep(.5)
    a = p1.set_valve(2,'E')
    time.sleep(.5)
    a = p1.get_valve(2)
    print('valve 2  pos:', a)



    time.sleep(.5)
    a = p1.get_valve(3)
    print('valve 3  pos:', a)


    # time.sleep(2)
    # p1.set_pos_absolute(1, 500)
    # time.sleep(2)
    # a = p1.get_plunger_position(1)    
    # print('plunger pos:', a)
    # p1.set_pickup(1, 5000)
    # p1.set_dispense(1, 5000)

    # testing valve
    # p1.set_valve(1,'I')
    # time.sleep(1)
    # ss = p1.get_valve(1)
    # print('valve pos:', ss)
    # time.sleep(1)
    # p1.set_valve(1,'O')
    # time.sleep(1)
    # ss = p1.get_valve(1)
    # print('valve pos:', ss)

    p1.close()