from app.chatbot import GeminiChatbot
from app.config import GEMINI_API_KEY
from app.chat_history import ChatHistory
from app.file_manager import FileManager
from app.logger import logger


def main():

    chatbot = GeminiChatbot(
        GEMINI_API_KEY
    )

    history = ChatHistory()

    question_count = 0

    print("\n")
    print("=" * 60)
    print("GENAI DAY 01 - GEMINI CHATBOT")
    print("=" * 60)

    print(
        "\nCommands:"
    )

    print("history -> Show Chat History")
    print("exit    -> Exit Application")

    while True:

        question = input(
            "\nYou: "
        )

        if question.lower() == "exit":

            print(
                "\nGoodbye!"
            )
            break

        if question.lower() == "history":

            history.display()
            continue

        if not question.strip():

            print(
                "Please enter a valid question."
            )
            continue

        question_count += 1

        print(
            f"\nQuestion Number: "
            f"{question_count}"
        )

        try:

            logger.info(
                f"Question: {question}"
            )

            result = chatbot.ask(
                question
            )

            answer = result["answer"]

            history.add_question(
                question
            )

            history.add_response(
                answer
            )

            FileManager.save(
                question,
                answer
            )

            logger.info(
                f"Answer: {answer}"
            )

            print(
                "\nGemini:"
            )

            print(answer)

            print(
                f"\nResponse Time: "
                f"{result['response_time']} sec"
            )

        except Exception as ex:

            logger.error(
                str(ex)
            )

            print(
                f"\nError: {ex}"
            )


if __name__ == "__main__":
    main()