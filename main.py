from dotenv import load_dotenv
import bot
from texttospeech import text_to_speech


def main():
    load_dotenv()

    # Read data from text file
    company_info = bot.get_text_from_file("info.txt")

    if not company_info:
        print("DreamSpace Academy data is not found")
        return

    text_chunks = bot.get_text_chunks(company_info)
    vectorstore = bot.get_vectorstore(text_chunks)
    conversation = bot.get_conversation_chain(vectorstore)

    while True:
        user_question = input('User: ')

        response = conversation({'question': user_question})

        # Safely access 'answers' key and print response
        if 'answer' in response and response['answer']:
            print("BeeBot:", response['answer'], "\n")
            text_to_speech(response['answer'])
        else:
            print("BeeBot: I'm sorry, I couldn't find an answer to that.")
            text_to_speech("I'm sorry, I couldn't find an answer to that.")
            continue


if __name__ == '__main__':
    main()
