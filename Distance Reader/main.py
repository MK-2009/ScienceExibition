import serial
import turtle
import time

# Open the serial connection to Arduino
arduinoData = serial.Serial('com3', 9600)  # Replace 'com3' with your Arduino's port

# Set up the screen
win = turtle.Screen()
win.title("Ultrasonic Sensor Distance")
win.bgcolor("white")

# Set up the turtle
dist_turtle = turtle.Turtle()
dist_turtle.hideturtle()

try:
    while True:
        while arduinoData.inWaiting() == 0:
            pass
        arduinoString = arduinoData.readline().decode('utf-8').strip()

        # Check if the received data is numeric
        if not arduinoString.isdigit():
            continue

        try:
            distance = float(arduinoString)
        except ValueError as e:
            print(f"Error: {e}")
            continue

        # Clear the previous text
        dist_turtle.clear()

        # Write the new distance
        dist_turtle.write(f"Distance: {distance} cm", align="center", font=("Courier", 24, "bold"))

        # Delay for 0.5 seconds
        #time.sleep(0.5)

except KeyboardInterrupt:
    # Close the serial connection and exit gracefully on keyboard interrupt
    arduinoData.close()
    turtle.bye()