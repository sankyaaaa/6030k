# Pure Pursuit Simulation

This project implements a Pure Pursuit algorithm simulation that utilizes waypoints defined in a JSON file. The simulation visualizes the movement of a vehicle along a defined path, allowing for testing and analysis of the Pure Pursuit steering method.

## Project Structure

```
pure-pursuit-simulation/
├── src/
│   ├── __init__.py
│   ├── purePlanner.py        # Main logic for the Pure Pursuit algorithm and waypoint handling
│   ├── simulation.py         # Runs the Pure Pursuit simulation using waypoints from JSON
│   ├── utils/
│   │   ├── __init__.py
│   │   └── json_handler.py   # Functions for reading and writing JSON files
│   └── types/
│       └── __init__.py       # Custom types or data structures
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd pure-pursuit-simulation
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare a JSON file containing waypoints for the simulation.
2. Run the simulation:
   ```
   python src/simulation.py <path-to-json-file>
   ```

## Main Components

- **purePlanner.py**: Contains the core logic for the Pure Pursuit algorithm, including functions for adding waypoints and visualizing the simulation.
- **simulation.py**: Responsible for executing the simulation and managing the vehicle's movement along the waypoints.
- **json_handler.py**: Handles loading and saving waypoints to and from JSON files.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.