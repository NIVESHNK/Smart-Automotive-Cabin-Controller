import tkinter as tk


# ==================================================
# VEHICLE CONTROL ECU
# ==================================================

class VehicleControlECU:

    def __init__(self):

        self.speed = 0
        self.ignition_status = "OFF"
        self.gear_status = "PARK"


    def ignition_on(self):

        self.ignition_status = "ON"


    def ignition_off(self):

        self.ignition_status = "OFF"
        self.speed = 0


    def set_park(self):

        if self.speed == 0:

            self.gear_status = "PARK"
            return True

        return False


    def set_drive(self):

        if self.speed == 0:

            self.gear_status = "DRIVE"
            return True

        return False


    def set_reverse(self):

        if self.speed == 0:

            self.gear_status = "REVERSE"
            return True

        return False


    def increase_speed(self):

        self.speed = self.speed + 10


    def brake(self):

        self.speed = self.speed - 10

        if self.speed < 0:

            self.speed = 0


# ==================================================
# CREATE VEHICLE ECU
# ==================================================

vehicle_ecu = VehicleControlECU()


# ==================================================
# WINDOW
# ==================================================

window = tk.Tk()

window.title("Virtual Vehicle ECU Simulator")
window.geometry("800x850")


# ==================================================
# OTHER VEHICLE VARIABLES
# ==================================================

door_status = "CLOSED"
interior_light = "OFF"
seat_belt_status = "UNFASTENED"


# ==================================================
# GUI FUNCTIONS
# ==================================================

def increase_speed():

    if vehicle_ecu.ignition_status == "OFF":

        warning_label.config(
            text="Warning: Turn Ignition ON first!"
        )

    elif vehicle_ecu.gear_status == "PARK":

        warning_label.config(
            text="Warning: Shift to DRIVE first!"
        )

    elif vehicle_ecu.gear_status == "REVERSE":

        warning_label.config(
            text="Warning: Vehicle is in REVERSE gear!"
        )

    elif door_status == "OPEN":

        warning_label.config(
            text="Warning: Close the door before moving!"
        )

    else:

        # Ask Vehicle Control ECU to increase speed
        vehicle_ecu.increase_speed()

        speed_label.config(
            text=f"Speed: {vehicle_ecu.speed} km/h"
        )

        if seat_belt_status == "UNFASTENED":

            warning_label.config(
                text="Warning: Fasten Seat Belt!"
            )

        else:

            warning_label.config(text="")


# ==================================================
# BRAKE
# ==================================================

def brake():

    vehicle_ecu.brake()

    speed_label.config(
        text=f"Speed: {vehicle_ecu.speed} km/h"
    )

    brake_label.config(
        text="Brake Status: APPLIED"
    )

    # Check seat belt warning again
    if vehicle_ecu.speed > 0 and seat_belt_status == "UNFASTENED":

        warning_label.config(
            text="Warning: Fasten Seat Belt!"
        )

    else:

        warning_label.config(text="")


# ==================================================
# DOOR
# ==================================================

def open_door():

    global door_status
    global interior_light

    if vehicle_ecu.speed == 0:

        door_status = "OPEN"
        interior_light = "ON"

        door_label.config(
            text=f"Door: {door_status}"
        )

        light_label.config(
            text=f"Interior Light: {interior_light}"
        )

        warning_label.config(text="")

    else:

        warning_label.config(
            text="Warning: Cannot open door while vehicle is moving!"
        )


def close_door():

    global door_status
    global interior_light

    door_status = "CLOSED"
    interior_light = "OFF"

    door_label.config(
        text=f"Door: {door_status}"
    )

    light_label.config(
        text=f"Interior Light: {interior_light}"
    )

    warning_label.config(text="")


# ==================================================
# IGNITION
# ==================================================

def ignition_on():

    vehicle_ecu.ignition_on()

    ignition_label.config(
        text=f"Ignition: {vehicle_ecu.ignition_status}"
    )

    warning_label.config(text="")


def ignition_off():

    vehicle_ecu.ignition_off()

    ignition_label.config(
        text=f"Ignition: {vehicle_ecu.ignition_status}"
    )

    speed_label.config(
        text=f"Speed: {vehicle_ecu.speed} km/h"
    )

    warning_label.config(text="")


# ==================================================
# GEAR
# ==================================================

def set_park():

    success = vehicle_ecu.set_park()

    if success:

        gear_label.config(
            text=f"Gear: {vehicle_ecu.gear_status}"
        )

        warning_label.config(text="")

    else:

        warning_label.config(
            text="Warning: Stop the vehicle before changing gear!"
        )


def set_drive():

    success = vehicle_ecu.set_drive()

    if success:

        gear_label.config(
            text=f"Gear: {vehicle_ecu.gear_status}"
        )

        warning_label.config(text="")

    else:

        warning_label.config(
            text="Warning: Stop the vehicle before changing gear!"
        )


def set_reverse():

    success = vehicle_ecu.set_reverse()

    if success:

        gear_label.config(
            text=f"Gear: {vehicle_ecu.gear_status}"
        )

        warning_label.config(text="")

    else:

        warning_label.config(
            text="Warning: Stop the vehicle before changing gear!"
        )


# ==================================================
# SEAT BELT
# ==================================================

def fasten_seat_belt():

    global seat_belt_status

    seat_belt_status = "FASTENED"

    seat_belt_label.config(
        text=f"Seat Belt: {seat_belt_status}"
    )

    warning_label.config(text="")


def unfasten_seat_belt():

    global seat_belt_status

    seat_belt_status = "UNFASTENED"

    seat_belt_label.config(
        text=f"Seat Belt: {seat_belt_status}"
    )

    if vehicle_ecu.speed > 0:

        warning_label.config(
            text="Warning: Fasten Seat Belt!"
        )


# ==================================================
# TITLE
# ==================================================

title = tk.Label(
    window,
    text="VIRTUAL VEHICLE ECU SIMULATOR",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)


# ==================================================
# VEHICLE STATUS
# ==================================================

speed_label = tk.Label(
    window,
    text="Speed: 0 km/h",
    font=("Arial", 18, "bold")
)

speed_label.pack(pady=5)


brake_label = tk.Label(
    window,
    text="Brake Status: RELEASED",
    font=("Arial", 14)
)

brake_label.pack(pady=5)


door_label = tk.Label(
    window,
    text="Door: CLOSED",
    font=("Arial", 14)
)

door_label.pack(pady=5)


light_label = tk.Label(
    window,
    text="Interior Light: OFF",
    font=("Arial", 14)
)

light_label.pack(pady=5)


ignition_label = tk.Label(
    window,
    text="Ignition: OFF",
    font=("Arial", 14)
)

ignition_label.pack(pady=5)


gear_label = tk.Label(
    window,
    text="Gear: PARK",
    font=("Arial", 14)
)

gear_label.pack(pady=5)


seat_belt_label = tk.Label(
    window,
    text="Seat Belt: UNFASTENED",
    font=("Arial", 14)
)

seat_belt_label.pack(pady=5)


# ==================================================
# WARNING AREA
# ==================================================

warning_label = tk.Label(
    window,
    text="",
    font=("Arial", 13, "bold")
)

warning_label.pack(pady=10)


# ==================================================
# BUTTONS
# ==================================================

speed_button = tk.Button(
    window,
    text="Increase Speed",
    font=("Arial", 12),
    command=increase_speed
)

speed_button.pack(pady=4)


brake_button = tk.Button(
    window,
    text="Brake",
    font=("Arial", 12),
    command=brake
)

brake_button.pack(pady=4)


# ==================================================
# DOOR BUTTONS
# ==================================================

open_door_button = tk.Button(
    window,
    text="Open Door",
    font=("Arial", 12),
    command=open_door
)

open_door_button.pack(pady=4)


close_door_button = tk.Button(
    window,
    text="Close Door",
    font=("Arial", 12),
    command=close_door
)

close_door_button.pack(pady=4)


# ==================================================
# IGNITION BUTTONS
# ==================================================

ignition_on_button = tk.Button(
    window,
    text="Ignition ON",
    font=("Arial", 12),
    command=ignition_on
)

ignition_on_button.pack(pady=4)


ignition_off_button = tk.Button(
    window,
    text="Ignition OFF",
    font=("Arial", 12),
    command=ignition_off
)

ignition_off_button.pack(pady=4)


# ==================================================
# GEAR BUTTONS
# ==================================================

park_button = tk.Button(
    window,
    text="PARK",
    font=("Arial", 12),
    command=set_park
)

park_button.pack(pady=4)


drive_button = tk.Button(
    window,
    text="DRIVE",
    font=("Arial", 12),
    command=set_drive
)

drive_button.pack(pady=4)


reverse_button = tk.Button(
    window,
    text="REVERSE",
    font=("Arial", 12),
    command=set_reverse
)

reverse_button.pack(pady=4)


# ==================================================
# SEAT BELT BUTTONS
# ==================================================

fasten_seat_belt_button = tk.Button(
    window,
    text="Fasten Seat Belt",
    font=("Arial", 12),
    command=fasten_seat_belt
)

fasten_seat_belt_button.pack(pady=4)


unfasten_seat_belt_button = tk.Button(
    window,
    text="Unfasten Seat Belt",
    font=("Arial", 12),
    command=unfasten_seat_belt
)

unfasten_seat_belt_button.pack(pady=4)


# ==================================================
# KEEP WINDOW RUNNING
# ==================================================

window.mainloop()