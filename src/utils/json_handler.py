def load_waypoints_from_json(file_path):
    import json
    with open(file_path, 'r') as file:
        waypoints = json.load(file)
    return waypoints

def save_waypoints_to_json(waypoints, file_path):
    import json
    with open(file_path, 'w') as file:
        json.dump(waypoints, file)