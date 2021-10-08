#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)

from picarmini import forward
from picarmini import stop
from ezblock import Pin
from ezblock import ADC
from ezblock import delay
from ezblock import Ultrasonic
from picarmini import set_dir_servo_angle
from picarmini import set_camera_servo1_angle
from picarmini import set_camera_servo2_angle
from picarmini import dir_servo_angle_calibration
from picarmini import camera_servo1_angle_calibration
from picarmini import camera_servo2_angle_calibration
from ezblock import TTS
from Music import sound_effect_play
from picamera import PiCamera

pin_D0 = Pin("D0")
pin_D1 = Pin("D1")

adc_A0=ADC("A0")
adc_A1=ADC("A1")
adc_A2=ADC("A2")

dir_servo_angle_calibration(0)
camera_servo1_angle_calibration(0)
camera_servo2_angle_calibration(0)
stop()

tts = TTS()

def run():
    tts.say("Watch out. Testing the wheels")
    delay(2000)

    for i in [0, 25, 50, 75, 100, 0, -25, -50, -75, -100, 0]:
        forward(i)
        delay(500)
    delay(1000)
    stop()
    delay(1000)

    for i in [0, 10, 20, 30, 20, 10, 0, -10, -20, -30, -20, -10, 0]:
        set_dir_servo_angle(i)
        delay(500)

    tts.say("Testing the camera servos")
    delay(1000)
    for i in [0, 10, 20, 30, 20, 10, 0, -10, -20, -30, -20, -10, 0]:
        set_camera_servo1_angle(i)
        delay(500)
    for i in [0, 10, 20, 30, 20, 10, 0, -10, -20, -30, -20, -10, 0]:
        set_camera_servo2_angle(i)
        delay(500)

    tts.say("Taking a picture")
    camera = PiCamera()
    delay(1000)
    camera.capture("test.jpg")

    tts.say("Testing ultrasonic sensor")
    for i in range(10):
        print("Ultrasonic:", Ultrasonic(pin_D0, pin_D1).read())
        delay(500)

    tts.say("Testing grayscale sensor")
    for i in range(10):
        print(f"Grayscale: {adc_A0.read()} {adc_A1.read()} {adc_A2.read()}")
        delay(500)

    tts.say('Testing playing sound')
    delay(500)
    sound_effect_play('Weapon_Continue_Shooting.wav',50)

    


if __name__ == "__main__":
    run()  
