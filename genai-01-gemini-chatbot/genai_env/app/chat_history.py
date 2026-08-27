class ChatHistory:

    def __init__(self):
        self.messages = []

    def add_question(self, question):

        self.messages.append(
            {
                "role": "USER",
                "content": question
            }
        )

    def add_response(self, response):

        self.messages.append(
            {
                "role": "GEMINI",
                "content": response
            }
        )

    def display(self):

        print("\n")
        print("=" * 50)
        print("CHAT HISTORY")
        print("=" * 50)

        for message in self.messages:

            print(
                f"\n{message['role']}:"
            )

            print(
                message["content"]
            )

        print("\n")