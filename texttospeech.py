# Import the necessary module from the `pyttsx3` library, which is a text-to-speech conversion library in Python.
import pyttsx3


def text_to_speech(text):
    """
    Convert the provided text to speech.

    This function uses the `pyttsx3` library, which is a text-to-speech 
    conversion library in Python. It initializes an engine, selects a voice, 
    sets a speech rate, and speaks out the given text.

    Parameters:
    - text (str): The text to be converted to speech.

    Note:
    - Make sure your system has multiple voices installed if you want to experiment with different voice types.
    - Adjust the `rate` as per your preference. Lower values will make speech slower and higher values will make it faster.
    """

    # Initialize the speech engine.
    engine = pyttsx3.init()

    # Retrieve a list of all available voices.
    voices = engine.getProperty('voices')

    # Set the voice for the speech engine. By default, the second voice (usually female) is used.
    # You can experiment with the index to choose different voices available on your system.
    engine.setProperty('voice', voices[1].id)

    # Set the rate (speed) of speech. Here, it's set to 150 words per minute.
    # You can adjust this value according to your preference.
    engine.setProperty('rate', 150)

    # Instruct the engine to convert the given text to speech.
    engine.say(text)

    # Block while processing all the currently queued commands.
    engine.runAndWait()
