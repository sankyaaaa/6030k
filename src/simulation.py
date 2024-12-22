import json
import numpy as np
import matplotlib.pyplot as plt
from utils.json_handler import load_waypoints

class PurePursuit:
    def __init__(self, waypoints, lookahead_distance):
        self.waypoints = waypoints
        self.lookahead_distance = lookahead_distance
        self.current_position = np.array([0.0, 0.0])
        self.current_heading = 0.0

    def update_position(self, new_position, new_heading):
        self.current_position = np.array(new_position)
        self.current_heading = new_heading

    def get_target_waypoint(self):
        for waypoint in self.waypoints:
            distance = np.linalg.norm(self.current_position - np.array(waypoint))
            if distance >= self.lookahead_distance:
                return waypoint
        return None

    def simulate(self):
        target_waypoint = self.get_target_waypoint()
        if target_waypoint is not None:
            # Simulate vehicle movement towards the target waypoint
            # This is a placeholder for the actual movement logic
            print(f"Moving towards waypoint: {target_waypoint}")

def run_simulation(json_file):
    waypoints = load_waypoints(json_file)
    pure_pursuit = PurePursuit(waypoints, lookahead_distance=1.0)

    # Example simulation loop
    for _ in range(10):  # Simulate for 10 steps
        pure_pursuit.simulate()
        # Update position and heading here as needed

if __name__ == "__main__":
    run_simulation("path_to_your_waypoints.json")