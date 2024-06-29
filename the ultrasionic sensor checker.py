import serial
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Set up the serial connection (change 'COM5' to your Arduino port)
ser = serial.Serial('COM5', 9600, timeout=1)

# Set up the 1D plot
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_xlabel('Time')
ax.set_ylabel('Distance (cm)')
ax.set_title('Ultrasonic Sensor 1D Visualization')

# Initialize data
data = np.zeros((2, 100))  # Pre-allocate space for 100 time steps
line, = ax.plot(data[0], data[1], 'b-')

def update(num):
    global data
    try:
        distance = float(ser.readline().decode().strip())
        data[1] = np.roll(data[1], -1)  # Shift data to the left
        data[1, -1] = distance  # Update the last value with new distance
        data[0] = np.arange(len(data[0]))  # Update time axis
        line.set_data(data[0], data[1])
    except ValueError:
        # If the conversion to float fails, just skip the current line
        pass

ani = animation.FuncAnimation(fig, update, interval=100)
plt.show()

# Close the serial connection when done
ser.close()
     