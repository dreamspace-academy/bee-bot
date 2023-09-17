# Import necessary libraries and modules.
from dotenv import load_dotenv  # For loading environment variables from a .env file
import bot                      # Custom module to handle bot-related functionalities
# Custom module to handle text to speech conversion
from texttospeech import text_to_speech
# Custom module to handle speech to text conversion
from speechtotext import speech_to_text


def main():
    """
    Main execution function for BeeBot.

    This function initializes the environment, reads company data from a file, 
    processes it, and enters into an infinite loop where it listens for user questions,
    processes them and responds via speech.

    Note:
    Ensure you have a .env file in your project directory with necessary environment variables.
    """

    # Load environment variables from .env file
    load_dotenv()

    # Read the company's data from the info.txt file
    company_info = bot.get_text_from_file("info.txt")

    # If there's no data found, alert the user and exit the program.
    if not company_info:
        print("DreamSpace Academy data is not found")
        return

    # Split the company info into manageable chunks
    text_chunks = bot.get_text_chunks(company_info)
    # Convert the chunks into a vector store for processing
    vectorstore = bot.get_vectorstore(text_chunks)
    # Initialize a conversational chain with the vector store
    conversation = bot.get_conversation_chain(vectorstore)

    # Infinite loop to continuously listen to the user's questions and respond
    while True:
        try:
            # Capture the user's speech and convert it to text
            user_question = speech_to_text()
        except:
            # Handle any exceptions during speech recognition
            text_to_speech("sorry I could not hear you")
            continue

        # Process the user's question and get the bot's response
        response = conversation({'question': user_question})

        # If a valid answer is found, say it out loud. Otherwise, provide an error message.
        if 'answer' in response and response['answer']:
            print("BeeBot:", response['answer'], "\n")
            text_to_speech(response['answer'])
        else:
            print("BeeBot: I'm sorry, I couldn't find an answer to that.")
            text_to_speech("I'm sorry, I couldn't find an answer to that.")
            continue


# Execution starts here if the script is run as the main module.
if __name__ == '__main__':
    main()
