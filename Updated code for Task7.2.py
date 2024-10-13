import speech_recognition as sr  # Import speech recognition library to recognize voice commands
from gpiozero import LED         # Import gpiozero library to control the GPIO pins on Raspberry Pi
from time import sleep           # Import sleep function to add delays between operations

# Setup GPIO using gpiozero
light = LED(18)  # Initialize an LED object connected to GPIO pin 18 (you can change the pin number based on your setup)

# Function to turn the light ON
def light_on():
    light.on()  # Turns the LED ON
    print("Light ON")  # Print confirmation to the console

# Function to turn the light OFF
def light_off():
    light.off()  # Turns the LED OFF
    print("Light OFF")  # Print confirmation to the console

# Function to listen for a voice command using the microphone
def listen_for_command():
    # Initialize the recognizer to process the speech input
    recognizer = sr.Recognizer()
    # Initialize the microphone as the audio input source
    microphone = sr.Microphone()

    try:
        # Using the microphone for capturing audio input
        with microphone as source:
            print("Adjusting for background noise... Please wait.")
            # Automatically adjust for any background noise to improve recognition accuracy
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for command...")
            # Capture audio input from the user
            audio = recognizer.listen(source)

            # Convert the audio to text using Google’s Speech Recognition API
            command = recognizer.recognize_google(audio).lower()  # Convert to lowercase for easier command matching
            print(f"Command received: {command}")  # Print the recognized command for debugging

            return command  # Return the recognized command
    except sr.UnknownValueError:
        # If the recognizer cannot understand the audio, catch the error and notify the user
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        # If there is an issue with the request to the recognition service, handle it here
        print("Could not request results from the speech recognition service.")
    return ""  # Return an empty string if an error occurs

# Function to process the recognized command and act accordingly
def process_command(command):
    if "light on" in command:  # If the command contains "light on"
        light_on()  # Call the function to turn the light ON
    elif "light off" in command:  # If the command contains "light off"
        light_off()  # Call the function to turn the light OFF
    else:
        # If the command is not recognized, print an error message
        print("Command not recognized. Please say 'light on' or 'light off'.")

# Main program
if __name__ == "__main__":
    try:
        # Infinite loop to continuously listen for voice commands
        while True:
            command = listen_for_command()  # Listen for a command
            if command:  # If a valid command is received (i.e., it's not an empty string)
                process_command(command)  # Process the command to turn the light ON or OFF
            sleep(1)  # Pause for 1 second before listening again to avoid overwhelming the system
    except KeyboardInterrupt:
        # If the user interrupts the program (e.g., by pressing Ctrl+C), exit the loop
        print("Exiting program.")  # Print a message indicating the program is exiting