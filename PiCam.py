#Interfacing Pi Camera with Raspberry Pi
#Step:1.Connect Camera MOdule to RPI
#Step:2.Open terminal
#-> Run Commends
#->sudo pip3 install picamzero --bread-system-packages
#->sudo apt-get update
#Step:3.Open Thonny IDE
#->Write a code


from picamzero import Camera
from time import sleep
cam = Carmera()
cam.start preview()
cam.record_video('vid/Check1.mp4,duration=5)
                 cam.stop_preview()
                 sleep(5)

                 
#Step:4.Save the code as "cam.py"on a specific folder or 'Camera'
#Setp:5.Open terminal-> Run Command->python3 cam.py
