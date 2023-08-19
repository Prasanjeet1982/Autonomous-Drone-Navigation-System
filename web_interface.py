from fastapi import FastAPI
from drone_controller import DroneController

app = FastAPI()
drone_controller = DroneController()

@app.post("/takeoff")
def takeoff():
    try:
        drone_controller.drone.connect()
        drone_controller.drone.takeoff()
        return {"status": "success", "message": "Drone has taken off."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/land")
def land():
    try:
        drone_controller.drone.land()
        return {"status": "success", "message": "Drone is landing."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/move")
def move(distance: int):
    try:
        drone_controller.drone.move_forward(distance)
        return {"status": "success", "message": f"Drone moved forward by {distance} cm."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def run_server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
