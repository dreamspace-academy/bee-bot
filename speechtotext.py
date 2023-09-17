# Import the necessary module from the `speech_recognition` library.
import speech_recognition as sr


def speech_to_text():
    """
    Convert speech to text using the microphone.

    This function captures audio from the default system microphone and 
    uses the Google Web Speech API to transcribe it into text.

    Returns:
    - str: Transcribed text if successful, None otherwise.
    """

    # Initialize the recognizer instance from the `speech_recognition` library.
    r = sr.Recognizer()

    # Use the system's default microphone as the audio source.
    with sr.Microphone() as source:
        # Adjust for ambient noise in the environment, which helps in improving accuracy of speech recognition.
        r.adjust_for_ambient_noise(source)

        # Listen to the audio from the microphone.
        audio = r.listen(source)

        try:
            # Transcribe the audio to text using the Google Web Speech API.
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            # Handle the case where the speech is unintelligible.
            print("Sorry, I couldn't recognize what you said.")
        except sr.RequestError as e:
            # Handle the case where the API request fails.
            print(f"Could not request results; {e}")
