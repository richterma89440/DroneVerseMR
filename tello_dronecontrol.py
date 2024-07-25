# Maximilian Richter
# Sina Steinmüller
# Stand: 2024-07-17
""" 
This program provides a simple Tello drone controller for demonstration purposes.
Needs to be updated, not tested yet.
"""
from djitellopy import Tello

 
class TelloDroneController:
    def __init__(self):
        self.drone = Tello()
        print("Drone initialized.")
        self.drone.connect()
        print("Drone connected.")
        
        self.drone.streamoff()
        self.drone.streamon()

        # Initialisiere die Geschwindigkeiten für alle Richtungen auf 0
        self.speed_left_right = 0  # Links/Rechts
        self.speed_up_down = 0     # Auf/Ab
        self.speed_forward_back = 0  # Vorwärts/Rückwärts
        self.yaw_speed = 0         # Yaw (Drehung)

    def update_movement(self):
        self.drone.send_rc_control(self.speed_left_right, self.speed_forward_back, self.speed_up_down, self.yaw_speed)

    def up(self):
        self.speed_up_down = 30
        self.update_movement()

    def down(self):
        self.speed_up_down = -30
        self.update_movement()

    def left(self):
        self.speed_left_right = -30
        self.update_movement()

    def right(self):
        self.speed_left_right = 30
        self.update_movement()

    def forward(self):
        self.speed_forward_back = 30
        self.update_movement()

    def backward(self):
        self.speed_forward_back = -30
        self.update_movement()
    
    def takeoff(self):
        self.drone.takeoff()
        print("Drone took off.")

    def stop(self):
        # Setze alle Geschwindigkeiten auf 0, um die Drohne zu stoppen
        self.speed_left_right = 0
        self.speed_up_down = 0
        self.speed_forward_back = 0
        self.yaw_speed = 0
        self.update_movement()

    def up(self):
        print("Tello: Up")

    def down(self):
        print("Tello: down")

    def left(self):
        print("Tello: left")

    def right(self):
        print("Tello: right")

    def forward(self):
        print("Tello: forward")

    def backward(self):
        print("Tello: backward")
