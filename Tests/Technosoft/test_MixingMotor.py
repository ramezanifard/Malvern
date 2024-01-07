from config.motor_mixer import motor_mixer
import time





if __name__ == "__main__":

    AXIS_ID = 24    
    acceleration = 1
    motor = motor_mixer(b"COM7", AXIS_ID, b"Mixer",acceleration)
    

    #/*	Setup and initialize the axis */	
    if (motor.InitAxis()==False):
        print("Failed to start up the drive")



    motor.set_speed(1000)
    time.sleep(3)
    motor.set_speed(0)
