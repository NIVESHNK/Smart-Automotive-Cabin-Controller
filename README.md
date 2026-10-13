# Virtual Vehicle ECU Simulator

## Overview

The Virtual Vehicle ECU Simulator is a Python-based graphical application that simulates selected vehicle states and driver-control functions. It provides an interactive interface for viewing vehicle status and triggering actions related to speed, braking, doors, ignition, gear selection, and seat-belt status.

## Features

- **Speed Control:** Displays vehicle speed and provides an option to increase it.
- **Brake Monitoring:** Displays brake status and provides a brake control.
- **Door Control:** Supports opening and closing the vehicle door.
- **Ignition Control:** Provides ignition ON and OFF controls.
- **Gear Selection:** Provides PARK, DRIVE, and REVERSE selection options.
- **Interior Light Status:** Displays the current interior-light state.
- **Seat-Belt Monitoring:** Displays seat-belt status and provides fasten and unfasten controls.
- **Warning Display:** Shows a warning prompting the user to stop the vehicle before changing gear.

## Technologies Used

- Python
- Tkinter for the graphical user interface

## Application Output

The graphical interface displays the vehicle's current state, including speed, brake status, door status, interior-light status, ignition state, selected gear, and seat-belt status.

The supplied screenshot shows an example state with the vehicle speed at 70 km/h, ignition ON, gear in DRIVE, brakes RELEASED, door CLOSED, interior light OFF, and seat belt UNFASTENED. It also displays a warning to stop the vehicle before changing gear.

These values describe the supplied screenshot and should not be interpreted as the application's default state or as proof of every control's behavior.

## How to Run

1. Install Python with Tkinter support.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run the application using:

   `python main.py`

5. Use the interface controls to explore the available vehicle-state and driver-control functions.

The instructions assume the entry-point file is named `main.py`; adjust the command if the actual source file uses a different name.

## OUTPUT
<img width="866" height="633" alt="image" src="https://github.com/user-attachments/assets/b6204c8e-d057-419c-8faa-92b49f09dcd4" />


## Scope and Limitations

This project demonstrates vehicle-state monitoring and driver-control interactions through a software-based graphical interface. It does not, by itself, establish communication with a physical vehicle or verify real automotive ECU hardware.

CAN/SPI communication, hardware integration, and simulation test results should be documented only if they are implemented and independently verified in the project.

## Author

Nivesh N K
