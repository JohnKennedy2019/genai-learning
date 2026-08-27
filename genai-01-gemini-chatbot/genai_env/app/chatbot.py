import time
from google import genai


class GeminiChatbot:

    def __init__(self, api_key):

        self.client = genai.Client(
            api_key=api_key
        )

    def ask(self, question):

        start_time = time.time()

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question
        )

        end_time = time.time()

        return {
            "answer": response.text,
            "response_time": round(
                end_time - start_time,
                2
            )
        }