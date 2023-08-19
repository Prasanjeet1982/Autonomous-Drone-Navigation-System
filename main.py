import threading
from drone_controller import DroneController
from web_interface import run_server

if __name__ == "__main__":
    drone_controller = DroneController()
    
    # Create a thread to control the drone
    control_thread = threading.Thread(target=run_server)
    control_thread.start()

    # Perform drone control tasks
    drone_controller.run_tasks()

    # Wait for the control thread to finish
    control_thread.join()
