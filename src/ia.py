import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

class Ia:

    def __init__(self):
        self.api_key = os.getenv('api_key')

    def get_response(self, prompt, model='gpt-3.5-turbo'):
        client = OpenAI(api_key=self.api_key)
        messages = [{'role': 'user', 'content': prompt}]
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
