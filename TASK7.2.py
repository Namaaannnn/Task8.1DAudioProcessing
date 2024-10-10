import RPi.GPIO as GPIO
import speech_recognition as sr
import time

# Set up GPIO
GPIO.setwarnings(False)  # Disable warnings
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Create a speech recognition object
r = sr.Recognizer()

while True:
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Try to recognize the speech
    try:
        command = r.recognize_google(audio)
        print("You said: " + command)

        # Check if the command is to turn the LED on or off
        if "on" in command.lower():
            print("LED on")
            GPIO.output(18, GPIO.HIGH)
        elif "of" in command.lower():
            print("LED off")
            GPIO.output(18, GPIO.LOW)

    # Handle any errors
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that")
    except sr.RequestError as e:
        print("Error; {0}".format(e))

    # Wait for 1 second before listening again
    time.sleep(1)