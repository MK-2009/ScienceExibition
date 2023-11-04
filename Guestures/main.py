import serial
import pyautogui

# Open serial port
ser = serial.Serial('COM3', 9600)

while True:
    try:
        # Read line from Arduino
        line = ser.readline().decode('utf-8').strip()

        # Perform action based on line
        if line == 'VOLUME DOWN':
            pyautogui.press('volumedown')
            print(line)
        elif line == 'VOLUME UP':
            pyautogui.press('volumeup')
            print(line)
        elif line == 'MUTE':
            pyautogui.press('volumemute')
            print(line)
    except KeyboardInterrupt:
        break

# Close serial port
ser.close()
