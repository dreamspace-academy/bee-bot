
import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')

    # Set the voice - replace '1' with the index of the voice you want from the voices list
    # For example, on Windows, you might have 2 voices: 0 (Male) and 1 (Female)
    # Here, I'm using the second voice (index 1)
    engine.setProperty('voice', voices[1].id)

    # Change the speech rate (speed). Default might be 200 words per minute, but you can set your desired rate.
    # Set speed. Lower is slower, and higher is faster.
    engine.setProperty('rate', 150)

    engine.say(text)
    engine.runAndWait()
