import time
from djitellopy import Tello

class DroneController:
    def __init__(self):
        self.drone = Tello()

    def run_tasks(self):
        try:
            self.drone.connect()
            self.drone.takeoff()

            # Perform drone control tasks here
            self.move_forward(100)  # Example: Move forward by 100 cm

            self.drone.land()
            self.drone.disconnect()
        except Exception as e:
            print("An error occurred:", str(e))

    def move_forward(self, distance):
        self.drone.move_forward(distance)
        print(f"Moving forward by {distance} cm")
