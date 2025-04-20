import serial
import pyvjoy
import subprocess

subprocess.Popen([]) # Open vJoy App, insert the file path 

# Arduino serial setup
arduino = serial.Serial('COM6', 9600, timeout=0.1)

# Virtual joystick setup
joystick = None
try: 
    joystick = pyvjoy.VJoyDevice(1)  # Virtual joystick ID (ensure vJoy is set up)
    print("vJoy device initialized successfully.")
except pyvjoy.exceptions.vJoyNotEnabledException:
    print("vJoy is not enabled. Please ensure vJoy is installed and enabled.")
except pyvjoy.exceptions.vJoyException as e:
    print(f"An error occurred with vJoy: {e}")

if joystick:
    def handleButtonState(button_value):

        joystick.set_axis(pyvjoy.HID_USAGE_X, button_value *32)
        

    # Main loop to read serial data and process it
    while True:
        data = arduino.readline().decode('utf-8', errors='replace').strip()
        
        if data:
            print(f"Raw data received: {data}")
            try:
                button_value = int(data)  # Convert serial data to integer
                print(f"Received value: {button_value}")

                handleButtonState(button_value)  # Handle L2 button press/release logic

            except ValueError:
                print(f"Invalid data: {data}, skipping.")
else:
    print("Exiting script due to vJoy initialization failure.")
