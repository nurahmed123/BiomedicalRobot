import tkinter as tk
import serial
import time


servo1_previous_value = 90
servo2_previous_value = 90
servo3_previous_value = 90
servo4_previous_value = 90
servo5_previous_value = 90
servo6_previous_value = 90
    
    
    
# Define the COM port where your Arduino is connected
arduino_port = "COM4"  # Change this to your Arduino's port

# Create a serial connection to the Arduino
ser = serial.Serial(arduino_port, 9600, timeout=1)

def update_servo_values(value):
    global    servo1_previous_value 
    global    servo2_previous_value 
    global    servo3_previous_value 
    global    servo4_previous_value 
    global    servo5_previous_value 
    global    servo6_previous_value 
    servo1_value = servo1_scale.get()
    servo2_value = servo2_scale.get()
    servo3_value = servo3_scale.get()
    servo4_value = servo4_scale.get()
    servo5_value = servo5_scale.get()
    servo6_value = servo6_scale.get()

    servo1_label.config(text=f"Servo1: {servo1_value}")
    servo2_label.config(text=f"Servo2: {servo2_value}")
    servo3_label.config(text=f"Servo3: {servo3_value}")
    servo4_label.config(text=f"Servo4: {servo4_value}")
    servo5_label.config(text=f"Servo5: {servo5_value}")
    servo6_label.config(text=f"Servo6: {servo6_value}")

    # Send servo positions to Arduino
    if servo1_previous_value != servo1_value:
        ser.write(f'1{servo1_value}\n'.encode())
        print(f'1{servo1_value}\n'.encode())
    if servo2_previous_value != servo2_value:
        ser.write(f'2{servo2_value}\n'.encode())
        print(f'2{servo2_value}\n'.encode())
    if servo3_previous_value != servo3_value:
        ser.write(f'3{servo3_value}\n'.encode())
        
    if servo4_previous_value != servo4_value:
        ser.write(f'4{servo4_value}\n'.encode())
        
    if servo5_previous_value != servo5_value:
        ser.write(f'5{servo5_value}\n'.encode())
        
    servo1_previous_value = servo1_value
    servo2_previous_value = servo2_value
    servo3_previous_value = servo3_value
    servo4_previous_value = servo4_value
    servo5_previous_value = servo5_value
    servo6_previous_value = servo6_value
# Create the main window
window = tk.Tk()
window.title("Servo Sliders")

# Create servo labels
servo1_label = tk.Label(window, text="Servo1:")
servo2_label = tk.Label(window, text="Servo2:")
servo3_label = tk.Label(window, text="Servo3:")
servo4_label = tk.Label(window, text="Servo4:")
servo5_label = tk.Label(window, text="Servo5:")
servo6_label = tk.Label(window, text="Servo6:")

servo1_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
servo2_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
servo3_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
servo4_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
servo5_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
servo6_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

# Create servo sliders
servo1_scale = tk.Scale(window, from_=0, to=180, orient="horizontal", length=300, command=update_servo_values)
servo2_scale = tk.Scale(window, from_=0, to=180, orient="horizontal", length=300, command=update_servo_values)
servo3_scale = tk.Scale(window, from_=0, to=180, orient="horizontal", length=300, command=update_servo_values)
servo4_scale = tk.Scale(window, from_=0, to=180, orient="horizontal", length=300, command=update_servo_values)
servo5_scale = tk.Scale(window, from_=0, to=180, orient="horizontal", length=300, command=update_servo_values)
servo6_scale = tk.Scale(window, from_=0, to=180, orient="horizontal", length=300, command=update_servo_values)

servo1_scale.grid(row=0, column=1, padx=10, pady=5)
servo2_scale.grid(row=1, column=1, padx=10, pady=5)
servo3_scale.grid(row=2, column=1, padx=10, pady=5)
servo4_scale.grid(row=3, column=1, padx=10, pady=5)
servo5_scale.grid(row=4, column=1, padx=10, pady=5)
servo6_scale.grid(row=5, column=1, padx=10, pady=5)

# Start the Tkinter main loop
window.mainloop()
