from ctypes import *
import time

mydll1 =CDLL("./TML_LIB.dll")
AXIS_ID_01 = 24
POWER_ON = 1

fd = mydll1.TS_OpenChannel(b"COM7",0, AXIS_ID_01, 115200)
print("result:", fd)

#/*	Load the *.t.zip with setup data generated with EasyMotion Studio or EasySetUp */
# idxSetup = mydll1.TS_LoadSetup(b"./test1.t.zip")
idxSetup = mydll1.TS_LoadSetup(b"./SpdTst.t.zip")
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

POWER_ON = 1
POWER_OFF =0
#/*	Enable the power stage of the drive (AXISON) */ 
# tt = mydll1.TS_Power(POWER_ON)
# print('Power On successful:', tt)

y = mydll1.TS_ReadStatus
y.restype = c_bool
y.argtypes = [c_int,POINTER(c_int)]

p = c_int()
buf = create_string_buffer(1)

tt = mydll1.TS_Power(POWER_ON)
print('Power On successful:', tt)


# sAxisOn_flag = pointer to unsinged short
sAxiOn_flag = 0
REG_SRL =3
while ((p.value & (1<<15)) == 0):
    tt = y(REG_SRL,  byref(p))
    
print('{:X} = {:b} '.format(p.value,p.value))

speed = 300.
acceleration = .1

x = mydll1.TS_MoveVelocity
x.restype = c_bool
x.argtypes = [c_double,c_double, c_int, c_int]
# tt = x(100., .01,1,0)
tt = x(speed, acceleration,1,0)
print(tt)

time.sleep(5)

speed = 0
tt = x(speed, acceleration,1,0)
print(tt)


tt = mydll1.TS_Power(POWER_OFF)
print('Power Off successful:', tt)

mydll1.TS_CloseChannel(fd);