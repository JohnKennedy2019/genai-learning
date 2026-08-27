from datetime import datetime


class FileManager:

    FILE_NAME = "chat_history.txt"

    @staticmethod
    def save(question, answer):

        with open(
            FileManager.FILE_NAME,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"\nTime: {datetime.now()}\n"
            )

            file.write(
                f"USER: {question}\n"
            )

            file.write(
                f"GEMINI: {answer}\n"
            )

            file.write(
                "-" * 50 + "\n"
            )