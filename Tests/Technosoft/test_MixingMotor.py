from ctypes import *

# mydll1 = cdll.LoadLibrary(".\\TML_lib.dll")
# mydll2 = cdll.LoadLibrary(".\\tmlcomm.dll")

mydll1 =CDLL("./TML_LIB.dll")
# mydll1 =CDLL("./tmlcomm.dll")

AXIS_ID_01 = 24
POWER_ON = 1

fd = mydll1.TS_OpenChannel(b"COM6",0, AXIS_ID_01, 115200)
print("result:", fd)



#/*	Load the *.t.zip with setup data generated with EasyMotion Studio or EasySetUp */
idxSetup = mydll1.TS_LoadSetup(b"./test1.t.zip")
if (idxSetup < 0):
    print('cannot load setup')
else:
    print("setup loaded sucessfully")

#/*	Setup the axis based on the setup data previously loaded */
tt = mydll1.TS_SetupAxis(AXIS_ID_01, idxSetup)
print(' setup axis:', tt)

#	Select the destination axis of the TML commands 
tt = mydll1.TS_SelectAxis(AXIS_ID_01)
print(' select dest. axis:', tt)

#/*	Execute the initialization of the drive (ENDINIT) */
tt = mydll1.TS_DriveInitialisation()
print('init successful:', tt)

#/*	Enable the power stage of the drive (AXISON) */ 
tt = mydll1.TS_Power(POWER_ON)
print('Power On successful:', tt)


sAxiOn_flag = 0
REG_SRL =3
#/*	Wait for power stage to be enabled */
while(sAxiOn_flag == 0):
    #/* Check the status of the power stage */
    if(mydll1.TS_ReadStatus(REG_SRL, sAxiOn_flag)==0): 
        print('failed')
        break
    print('sAxiOn_flag:', sAxiOn_flag)
    
print('sAxiOn_flag:', sAxiOn_flag)



# /*	Set the speed profile parameters */
speed = 3000;		#/* jogging speed [drive internal speed units, encoder counts/slow loop sampling] */
acceleration = 1#0.015;#/* acceleration rate [drive internal acceleration units, encoder counts/slow loop sampling^2] */
# /*	Set the speed level when the acceleration is changed */
speed_1 = 60;	#/* intermediate speed [drive internal speed units, encoder counts/slow loop sampling] */
# /*	Set the time period */
time = 2000;	#	/* time period [drive internal time units, slow loop sampling] */

tt = mydll1.TS_MoveVelocity(speed, acceleration,1,0)
print('set speed:', tt)




mydll1.TS_CloseChannel(fd);