from dotenv import load_dotenv
import bot


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

        # if 'hi' in user_question.lower() or 'hello' in user_question.lower() or 'good morning' in user_question.lower() or 'good evning' in user_question.lower() or 'good afternoon' in user_question.lower():
        #     print('hello')
        #     continue

        # if 'who are you' in user_question.lower():
        #     print('I am beebot an artificial intelligence bot')
        #     continue

        # if 'how are you' in user_question.lower():
        #     print('I am doing good')
        #     continue

        response = conversation({'question': user_question})

        # Safely access 'answers' key and print response
        if 'answer' in response and response['answer']:
            print("BeeBot:", response['answer'], "\n")
        else:
            print("BeeBot: I'm sorry, I couldn't find an answer to that.")
            continue


if __name__ == '__main__':
    main()
