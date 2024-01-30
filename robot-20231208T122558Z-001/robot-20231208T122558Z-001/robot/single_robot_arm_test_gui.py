import tkinter as tk
import serial

# Define the COM port where your Arduino is connected
arduino_port = "COM4"  # Change this to your Arduino's port
ser = serial.Serial(arduino_port, 9600, timeout=1)

def update_servo():
    angle = servo_scale.get()
    ser.write(f'{angle}'.encode())

# Create the main window
window = tk.Tk()
window.title("Servo Control")

# Create a scale (slider) widget to control the servo
servo_scale = tk.Scale(window, from_=0, to=180, orient="horizontal", length=300)
servo_scale.set(90)  # Set an initial position
servo_scale.pack(padx=20, pady=20)

# Create a button to send the servo command
update_button = tk.Button(window, text="Update Servo", command=update_servo)
update_button.pack()

# Start the Tkinter main loop
window.mainloop()
