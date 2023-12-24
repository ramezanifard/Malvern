import GUI
from tkinter import * 
import config.motor_1 as Motor1
import config.Pump as P
import time
import u6
import threading
import config.MeerstetterTEC as TEC
import json


#------------------- Constants -----------------------------------------
BS1_THRESHOLD = 2.5  #Threshold value for bubble sensor 1
BS2_THRESHOLD = 2.5  #Threshold value for bubble sensor 2
BS3_THRESHOLD = 2.5  #Threshold value for bubble sensor 3
BS4_THRESHOLD = 2.5  #Threshold value for bubble sensor 4
BS5_THRESHOLD = 2.5  #Threshold value for bubble sensor 5
BS6_THRESHOLD = 2.5  #Threshold value for bubble sensor 6
BS7_THRESHOLD = 2.5  #Threshold value for bubble sensor 7
BS8_THRESHOLD = 2.5  #Threshold value for bubble sensor 8
BS9_THRESHOLD = 2.5  #Threshold value for bubble sensor 9
BS10_THRESHOLD = 2.5  #Threshold value for bubble sensor 10
BS11_THRESHOLD = 2.5  #Threshold value for bubble sensor 11
BS12_THRESHOLD = 2.5  #Threshold value for bubble sensor 12
BS13_THRESHOLD = 2.5  #Threshold value for bubble sensor 13
BS14_THRESHOLD = 2.5  #Threshold value for bubble sensor 14
##--------------------------------------------------------------------------


class run_GUI(GUI.GUI):
    def __init__(self,root):
        super().__init__( root)
        #---- extract port numbers for config.json
        with open('./config/config.json') as json_file:
            ports = json.load(json_file)

        print('ports:', ports)
        TEC_PORT = ports['TEC']
        PUMP1_PORT = ports['PUMP1']
        MOTOR1_PORT = ports['MOTOR1']

        print('tec port:', TEC_PORT, '  ,  motor1 port:', MOTOR1_PORT, '  , pump1:', PUMP1_PORT)
        self.Ltecport.config(text=TEC_PORT)
        self.Lpump1port.config(text=PUMP1_PORT)
        self.Lmotor1port.config(text=MOTOR1_PORT)

        print("Initializing hardware ----------------------------------------------")
        #------ init. motor 1
        print("Initializing Motors.....")
        self.motor1 = Motor1.motor_1(0,1.5)
        print("Motors Initialized")

        #------ init. Pump 1
        # print(" Initializing Pumps/Valves.....",end=' ')
        # self.pump1 = P.Pump("COM6")
        # print(" Pumps initialized")
        # self.pump1.pump_Zinit(1)
        # initialize labjack
        print(" Initializing Labjack.....",end=' ')
        self.labjack = u6.U6()
        self.labjack.writeRegister(50590, 15)        
        print('labjack initialized')
        # #------ Starts timer
        print('starting internal timer')
        self.timer = threading.Timer(1.0, self.timerCallback_1)
        self.timer.start()
        self.scalefactor = 1
        # self.microstep = False         
        # self.pump_scale_factor(1)
        # print('mircostep off')
        # self.set_step_mode(False)
        self.BS= 1        

        # # ------create object of TEC5 
        # # print("----------------------------------------------")
        # self.mc = TEC.MeerstetterTEC("COM5")
        # print(self.mc.get_data())
        # # print(self.mc.set_temp(35.3))
        # # print("----------------------------------------------")
        # # #-------- set the motor1 speed to 0
        # valid = self.motor1.set_speed(0)
        # time.sleep(.25)
        # if (valid == True):
        #     self.m1_cur_spd.config(text="0")        

        # #------ init valve 1 to 'E' 
        # self.pump1.set_valve(1, 'E')
        # time.sleep(.75)
        # self.v1_cur_pos.config(text = "Pump to Air (P1)")





    def timerCallback_1(self):  
        # print('--->timer tick')
        #------------------------------- update pump 1 position
        # p1_cur_pos = self.pump1.get_plunger_position(1)            
        # p1_cur_pos = int(p1_cur_pos / self.scalefactor)
        # self.p1_cur_pos.config(text = str(p1_cur_pos))
        # # print('cur pos:', p1_cur_pos)
    
        # #------------------------------- update  of TEC controller parameters
        # # print(self.mc.get_data())
        # tec_dic =  self.mc.get_data()
        # obj_temp = round(tec_dic['object temperature'][0], 1)
        # target_temp = round(tec_dic['target object temperature'][0], 1)
        # TEC_cur_status = tec_dic['loop status'][0]
        # # print('--->', float(obj_temp), '   ,  ', target_temp, ' status:',TEC_cur_status)
        # # 1: ON, 0:OFF, 
        # if (TEC_cur_status== 1):            
        #     self.t_status.config(text = "ON")                        
        # else:
        #     self.t_status.config(text = "OFF")        
        # self.tec_cur_tmp.config(text=str(obj_temp))
        # self.tec_desired_tmp.config(text=str(target_temp))
        
        # #------------------------------- read bubble sensor and update the LEDs
        input0 = (self.labjack.getAIN(0))
        input1 = (self.labjack.getAIN(1))
        input2 = (self.labjack.getAIN(2))
        input3 = (self.labjack.getAIN(3))
        input4 = (self.labjack.getAIN(4))
        input5 = (self.labjack.getAIN(5))
        input6 = (self.labjack.getAIN(6))
        input7 = (self.labjack.getAIN(7))
        input8 = (self.labjack.getAIN(8))
        input9 = (self.labjack.getAIN(9))
        input10 = (self.labjack.getAIN(10))
        input11 = (self.labjack.getAIN(11))
        input12 = (self.labjack.getAIN(12))
        input13 = (self.labjack.getAIN(13))
        # print("AI0={:0.2f}".format(input0))        
        X3 = 1050
        Y1 = 100
        dY1 = 40
        dd=50

        if (input0 < BS1_THRESHOLD):
            self.led_on_1.place_forget()
            self.led_off_1.pack()
            self.led_off_1.place(x = X3+50,y = Y1 + 0*dY1)
        else:
            self.led_off_14.place_forget()
            self.led_on_1.pack()            
            self.led_on_1.place(x = X3+50,y = Y1 + 0*dY1)

        if (input1 < BS2_THRESHOLD):
            self.led_on_2.place_forget()
            # self.led_off_14.pack()
            self.led_off_2.place(x = X3+50,y = Y1 + 1*dY1)
        else:
            self.led_off_2.place_forget()
            # self.led_on_14.pack()            
            self.led_on_2.place(x = X3+50,y = Y1 + 1*dY1)

        if (input2 < BS3_THRESHOLD):
            self.led_on_3.place_forget()
            # self.led_off_14.pack()
            self.led_off_3.place(x = X3+50,y = Y1 + 2*dY1)
        else:
            self.led_off_3.place_forget()
            # self.led_on_14.pack()            
            self.led_on_3.place(x = X3+50,y = Y1 + 2*dY1)

        if (input3 < BS4_THRESHOLD):
            self.led_on_4.place_forget()
            # self.led_off_14.pack()
            self.led_off_4.place(x = X3+50,y = Y1 + 3*dY1)
        else:
            self.led_off_4.place_forget()
            # self.led_on_14.pack()            
            self.led_on_4.place(x = X3+50,y = Y1 + 3*dY1)

        if (input4 < BS5_THRESHOLD):
            self.led_on_5.place_forget()
            # self.led_off_14.pack()
            self.led_off_5.place(x = X3+50,y = Y1 + 4*dY1)
        else:
            self.led_off_5.place_forget()
            # self.led_on_14.pack()            
            self.led_on_5.place(x = X3+50,y = Y1 + 4*dY1)
            
        if (input5 < BS6_THRESHOLD):
            self.led_on_6.place_forget()
            # self.led_off_14.pack()
            self.led_off_6.place(x = X3+50,y = Y1 + 5*dY1)
        else:
            self.led_off_6.place_forget()
            # self.led_on_14.pack()            
            self.led_on_6.place(x = X3+50,y = Y1 + 5*dY1)

        if (input6 < BS7_THRESHOLD):
            self.led_on_7.place_forget()
            # self.led_off_14.pack()
            self.led_off_7.place(x = X3+50,y = Y1 + 6*dY1)
        else:
            self.led_off_7.place_forget()
            # self.led_on_14.pack()            
            self.led_on_7.place(x = X3+50,y = Y1 + 6*dY1)
        
        if (input7 < BS8_THRESHOLD):
            self.led_on_8.place_forget()
            # self.led_off_14.pack()
            self.led_off_8.place(x = X3+50,y = Y1 + 7*dY1)
        else:
            self.led_off_8.place_forget()
            # self.led_on_14.pack()            
            self.led_on_8.place(x = X3+50,y = Y1 + 7*dY1)

        if (input8 < BS9_THRESHOLD):
            self.led_on_9.place_forget()
            # self.led_off_14.pack()
            self.led_off_9.place(x = X3+50,y = Y1 + 8*dY1)
        else:
            self.led_off_9.place_forget()
            # self.led_on_14.pack()            
            self.led_on_9.place(x = X3+50,y = Y1 + 8*dY1)

        if (input9< BS10_THRESHOLD):
            self.led_on_10.place_forget()
            # self.led_off_14.pack()
            self.led_off_10.place(x = X3+50,y = Y1 + 9*dY1)
        else:
            self.led_off_10.place_forget()
            # self.led_on_14.pack()            
            self.led_on_10.place(x = X3+50,y = Y1 + 9*dY1)

        if (input10 < BS11_THRESHOLD):
            self.led_on_11.place_forget()
            # self.led_off_14.pack()
            self.led_off_11.place(x = X3+50,y = Y1 + 10*dY1)
        else:
            self.led_off_11.place_forget()
            # self.led_on_14.pack()            
            self.led_on_11.place(x = X3+50,y = Y1 + 10*dY1)

        if (input11 < BS12_THRESHOLD):
            self.led_on_12.place_forget()
            # self.led_off_14.pack()
            self.led_off_12.place(x = X3+50,y = Y1 + 11*dY1)
        else:
            self.led_off_12.place_forget()
            # self.led_on_14.pack()            
            self.led_on_12.place(x = X3+50,y = Y1 + 11*dY1)

        if (input13 < BS13_THRESHOLD):
            self.led_on_13.place_forget()
            # self.led_off_14.pack()
            self.led_off_13.place(x = X3+50,y = Y1 + 12*dY1)
        else:
            self.led_off_13.place_forget()
            # self.led_on_14.pack()            
            self.led_on_13.place(x = X3+50,y = Y1 + 12*dY1)

        if (input13 < BS14_THRESHOLD):
            self.led_on_14.place_forget()
            self.led_off_14.pack()
            self.led_off_14.place(x = X3+50,y = Y1 + 13*dY1)
        else:
            self.led_off_14.place_forget()
            self.led_on_14.pack()
            self.led_on_14.place(x = X3+50,y = Y1 + 13*dY1)                    



        #------------------------------- repeat the timer
        self.timer = threading.Timer(1.0, self.timerCallback_1)
        self.timer.start()





    def tec_b_tmpset_click(self):
        print("child: TECt new tmp:")
        s =   self.ent_tmp.get()
        if (is_float(s) == True):
            # print(s)
            self.mc.set_temp(float(s))
        else:
            print("invalid input")



    def tec_b_start_click(self):
        print("child: TEC start")
        self.mc.enable()
        pass

    def tec_b_stop_click(self):
        print("child: TEC stop")
        self.mc.disable()
        pass


    def checkComboCfg1(self, event):
        # def option_selected(event):
        s = self.comboCfg1.get()
        print('child :', s)
        ss=s.partition(')')
        # index = self.comboCfg1.get(0, "end") 
        index = ss[0]
        print('int number:', int(index))        
        # print("INDEX = ", index)
        self.pump_scale_factor(int(index))
        if (self.microstep == False):
            print('mircostep off')
            self.set_step_mode(False)            
        else:  #self.microstep = True
            print('mircostep on')
            self.set_step_mode(True)
            

    def p1_b_pickup_pos_click(self):
        print("child: p1_pickup ")
        s =   self.ent_pickup_pos.get()
        print(int(s))
        self.pump1.set_pickup(1, int(s))

    def p1_b_dispense_pos_click(self):
        print("child: p1_dispense ")
        s =   self.ent_dispemse_pos.get()
        print(int(s))
        self.pump1.set_dispense(1, int(s))


    def checkComboCfg2(self, event):
        # def option_selected(event):
        print('child:', self.comboCfg1.get())






    def m1_b_abs_pos_click(self):
        print("child: m1_new_spd")
        s =   self.ent_m1_spd_.get()
        print(s)
        if (is_float(s) == True):
            print('it\'s a number:', float(s))
            m1_speed = float(s)
            motor1_speed = float(m1_speed)
            print("motor 1 speed: ", motor1_speed)
            valid = self.motor1.set_speed(motor1_speed)
            if (valid == True):
                 self.m1_cur_spd.config(text=s)            
        else:
            print("not a number")
            
    
    # def p1_b_Zinit_click(self):
    #      print("child: p1 Z initialized")
    #      self.pump1.pump_Zinit(1)

    # def p1_b_Yinit_click(self):
    #      print("child: p1 Y initialized")
    #      self.pump1.pump_Yinit(1)



    # def p1_b_abs_pos_click(self):
    #     print("----> p1_abs pos")
    #     s =   self.ent_abs_pos.get()
    #     print(s)
    #     self.p1_cur_pos["text"]=  s


    def p1_b_abs_pos_click(self):
        print("child: p1_abs pos")
        s =   self.ent_abs_pos.get()
        print(s)
        if (is_float(s) == True):
            val = int(s)
            abs_pos = int(val * self.scalefactor)
            print('position is:', abs_pos)
            self.pump1.set_pos_absolute(1, abs_pos)
            ####===============to be moved to the timer thread
            # time.sleep(.25)
            # cur_plunger_pos = self.pump1.get_plunger_position(1)            
            # self.p1_cur_pos.config(text = str(cur_plunger_pos))


    def p1_b_dispenseUntillbubble(self):
        print(' dispense until bubble: to be completed later')
        pass


    def p1_b_teminateP1(self):
        print('child: termnate p1')
        self.pump1.stop(1)



    def p1_b_pickupUntillbubble(self):
        print("child: pickup until bubble")
        # send pump1 to 0 position
        # self.pump1.set_pos_absolute(1, 0)
        prev_speed = self.pump1.get_peakspeed(1)
        # change to high speed for retraction
        if (self.microstep == False):
            print('micro step is off')
            self.pump1.set_speed(1,1000)
        else:
            print('micro step is on')
            self.pump1.set_speed(1,1000*8)

        a =self.pump1.get_peakspeed(1)
        time.sleep(.25)
        print('peak speed:', a)
        self.pump1.set_pos_absolute(1, 0)

        cur_pos = 24000
        print('going to 0 pos')
        while (cur_pos > 0):
            # print('cur pos:', cur_pos)
            cur_pos = self.pump1.get_plunger_position(1)            
            time.sleep(1)

        # change to low speed for forward motion
        if (self.microstep == False):
            print('micro step is off')
            self.pump1.set_speed(1,48)
        else:
            print('micro step is on')
            self.pump1.set_speed(1,48*8)

        print('going to final pos')
        self.pump1.set_pos_absolute(1, 10000)

        # continue until a bubble detected or reaching end of travel
        input0 = (self.labjack.getAIN(0))
        while (cur_pos < 2000 and  input0>2.5):
            input0 = (self.labjack.getAIN(0))
            print('        selcted BS',self.BS, ' , reading: ',self.labjack.getAIN(self.BS-1))
            print('bubble sensor output:', input0)
            # time.sleep(1)
            print('cur pos ==', cur_pos)
            cur_pos = self.pump1.get_plunger_position(1)            
        self.pump1.stop(1)
        time.sleep(.25)
        self.pump1.set_speed(1, prev_speed)


    def p1_b_top_spd_click(self):
        print("p1_top speed")
        s =   self.ent_top_spd.get()
        print(s)
        if (is_float(s) == True):
            max_spd = int(s)
            self.pump1.set_speed(1,max_spd)
             ####===============to be moved to the timer thread
            time.sleep(.25)
            self.p1_cur_spd.config(text = s)

    def checkCombo1(self,event):
        s = self.combo1.get()
        print('child -->'+s)
        ("Pump to Air (P1)","Air to Gas (P2)","Gas to Line (P3)",
                                 "Line to Pump (P4)")
        if (s == "Pump to Air (P1)"):
            # print(" P1   --- E ")
            new_valve_pos = 'E'
        elif (s == "Air to Gas (P2)"):
            # print(" P2 ---- O")
            new_valve_pos = 'O'
        elif (s == "Gas to Line (P3)"):
            # print(" P3 --- I")
            new_valve_pos = 'I'
        elif (s == "Line to Pump (P4)"):
            # print(" P4 ---- B ")
            new_valve_pos = 'B'
        else:
            print(' invalid valve selection')
            new_valve_pos = 'E'
        self.pump1.set_valve(1, new_valve_pos)
        time.sleep(1)
        s = self.pump1.get_valve(1)
        # print("-----> ",s)
        cur_valve = "----"
        if (s=='e'):
            cur_valve = "Pump to Air (P1)"
            # print('EEEE')
        elif(s=='o'):
            cur_valve = "Air to Gas (P2)"
            # print('OOOO')
        elif(s=="i"):
            cur_valve = "Gas to Line (P3)"
            # print("IIII")
        elif(s=="b"):
            cur_valve = "Line to Pump (P4)"
            # print("BBBB")
        else:
            cur_valve = "error"

        self.v1_cur_pos.config(text=cur_valve)


    def checkCombo0(self,event):        
        s = self.combo0.get()        
        ss=s.partition('S')
        index = int(ss[2])
        print('bubble sensor number:', index)
        X3 = 1050
        Y1 = 100
        dY1 = 40
        # Label(self.tab1, text = "     ",font=("Arial", 15) , bg='#D9D9D9',fg='red').place(x = X3-40,y = Y1 + 0*dY1)         
        self.lbs1.place_forget()
        self.lbs2.place_forget()
        self.lbs3.place_forget()
        self.lbs4.place_forget()
        self.lbs5.place_forget()
        self.lbs6.place_forget()
        self.lbs7.place_forget()
        self.lbs8.place_forget()
        self.lbs9.place_forget()
        self.lbs10.place_forget()
        self.lbs11.place_forget()
        self.lbs12.place_forget()
        self.lbs13.place_forget()
        self.lbs14.place_forget()

        if (index == 1):
            self.lbs2.pack()
            self.lbs2.place(x = X3-40,y = Y1 + 0*dY1)
            self.BS = 1
        elif (index == 2):
            self.lbs2.pack()
            self.lbs2.place(x = X3-40,y = Y1 + 1*dY1)
            self.BS = 2
        elif (index == 3):
            self.lbs3.pack()
            self.lbs3.place(x = X3-40,y = Y1 + 2*dY1)  
            self.BS = 3
        elif (index == 4):
            self.lbs4.pack()
            self.lbs4.place(x = X3-40,y = Y1 + 3*dY1)
            self.BS = 4
        elif (index == 5):
            self.lbs5.pack()
            self.lbs5.place(x = X3-40,y = Y1 + 4*dY1)
            self.BS = 5
        elif (index == 6):
            self.lbs6.pack()
            self.lbs6.place(x = X3-40,y = Y1 + 5*dY1)
            self.BS = 6
        elif (index == 7):
            self.lbs7.pack()
            self.lbs7.place(x = X3-40,y = Y1 + 6*dY1)
            self.BS = 7
        elif (index == 8):
            self.lbs8.pack()
            self.lbs8.place(x = X3-40,y = Y1 + 7*dY1)
            self.BS = 8
        elif (index == 9):
            self.lbs9.pack()
            self.lbs9.place(x = X3-40,y = Y1 + 8*dY1)
            self.BS = 9
        elif (index == 10):
            self.lbs10.pack()
            self.lbs10.place(x = X3-40,y = Y1 + 9*dY1)
            self.BS = 10
        elif (index == 11):
            self.lbs11.pack()
            self.lbs11.place(x = X3-40,y = Y1 + 10*dY1)
            self.BS = 11
        elif (index == 12):
            self.lbs12.pack()
            self.lbs12.place(x = X3-40,y = Y1 + 11*dY1)
            self.BS = 12
        elif (index == 13):
            self.lbs13.pack()
            self.lbs13.place(x = X3-40,y = Y1 + 12*dY1)  
            self.BS = 13
        elif (index == 14):
            self.lbs14.pack()
            self.lbs14.place(x = X3-40,y = Y1 + 13*dY1)
            self.BS = 14



    def checkCombob1(self,event):        
        s = self.combob1.get()        
        ss=s.partition('S')
        index = int(ss[2])
        print('bubble sensor number:', index)
        X3 = 1050
        Y1 = 100
        dY1 = 40
        # Label(self.tab1, text = "     ",font=("Arial", 15) , bg='#D9D9D9',fg='red').place(x = X3-40,y = Y1 + 0*dY1)         
        self.lbs1.place_forget()
        self.lbs2.place_forget()
        self.lbs3.place_forget()
        self.lbs4.place_forget()
        self.lbs5.place_forget()
        self.lbs6.place_forget()
        self.lbs7.place_forget()
        self.lbs8.place_forget()
        self.lbs9.place_forget()
        self.lbs10.place_forget()
        self.lbs11.place_forget()
        self.lbs12.place_forget()
        self.lbs13.place_forget()
        self.lbs14.place_forget()

        if (index == 1):
            self.lbs2.pack()
            self.lbs2.place(x = X3-40,y = Y1 + 0*dY1)
            self.BS = 1
        elif (index == 2):
            self.lbs2.pack()
            self.lbs2.place(x = X3-40,y = Y1 + 1*dY1)
            self.BS = 2
        elif (index == 3):
            self.lbs3.pack()
            self.lbs3.place(x = X3-40,y = Y1 + 2*dY1)  
            self.BS = 3
        elif (index == 4):
            self.lbs4.pack()
            self.lbs4.place(x = X3-40,y = Y1 + 3*dY1)
            self.BS = 4
        elif (index == 5):
            self.lbs5.pack()
            self.lbs5.place(x = X3-40,y = Y1 + 4*dY1)
            self.BS = 5
        elif (index == 6):
            self.lbs6.pack()
            self.lbs6.place(x = X3-40,y = Y1 + 5*dY1)
            self.BS = 6
        elif (index == 7):
            self.lbs7.pack()
            self.lbs7.place(x = X3-40,y = Y1 + 6*dY1)
            self.BS = 7
        elif (index == 8):
            self.lbs8.pack()
            self.lbs8.place(x = X3-40,y = Y1 + 7*dY1)
            self.BS = 8
        elif (index == 9):
            self.lbs9.pack()
            self.lbs9.place(x = X3-40,y = Y1 + 8*dY1)
            self.BS = 9
        elif (index == 10):
            self.lbs10.pack()
            self.lbs10.place(x = X3-40,y = Y1 + 9*dY1)
            self.BS = 10
        elif (index == 11):
            self.lbs11.pack()
            self.lbs11.place(x = X3-40,y = Y1 + 10*dY1)
            self.BS = 11
        elif (index == 12):
            self.lbs12.pack()
            self.lbs12.place(x = X3-40,y = Y1 + 11*dY1)
            self.BS = 12
        elif (index == 13):
            self.lbs13.pack()
            self.lbs13.place(x = X3-40,y = Y1 + 12*dY1)  
            self.BS = 13
        elif (index == 14):
            self.lbs14.pack()
            self.lbs14.place(x = X3-40,y = Y1 + 13*dY1)
            self.BS = 14



    def set_step_mode(self, flag):

        if (flag == False):
            print('switch to normal mode')
            self.pump1.set_microstep_position(1,0)
        else:
            print(" switched to p&v  ")
            self.pump1.set_microstep_position(1,2)



    def pump_scale_factor(self, N):        
        if (N == 1):
            STEP_RANGE = 48000.
            VOLUME = 1000.
            self.microstep = False
        elif (N == 2):
            STEP_RANGE = 48000.
            VOLUME = 1000.
            self.microstep = True
        elif (N == 3):
            STEP_RANGE = 48000.
            VOLUME = 500.
            self.microstep = False
        elif (N == 4):
            STEP_RANGE = 48000.
            VOLUME = 500.
            self.microstep = True
        elif (N == 5):
            STEP_RANGE = 48000.
            VOLUME = 250.
            self.microstep = False
        elif (N == 6):
            STEP_RANGE = 48000.
            VOLUME = 250.
            self.microstep = True
        elif (N == 7):
            STEP_RANGE = 24000.
            VOLUME = 2500.
            self.microstep = False
        elif (N == 8):
            STEP_RANGE = 24000.
            VOLUME = 2500.
            self.microstep = True
        elif (N == 9):
            STEP_RANGE = 1
            VOLUME = 1
            self.microstep = False
            pass
        elif (N == 10):
            STEP_RANGE = 1
            VOLUME = 1
            self.microstep = True
            pass
        else:
            print("invalid scale factor")
            self.scalefactor = 1

        self.scalefactor = STEP_RANGE / VOLUME
        print('scale factor:', self.scalefactor)



    ###------------------- END OF CLASS DEFINITION ------------------------------------------------------








def is_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False
    



def main(): #run mianloop 
    
    root = Tk()
    # app = GUI.GUI(root)
    run_GUI(root)

    root.mainloop()

if __name__ == '__main__':
    main()