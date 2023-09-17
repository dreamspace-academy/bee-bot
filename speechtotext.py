import speech_recognition as sr


def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # This line adjusts for ambient noise
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            # Using the default recognizer which is Google Web Speech API
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't recognize what you said.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
