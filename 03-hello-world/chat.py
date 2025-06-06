from google import genai
import os
from dotenv import load_dotenv


load_dotenv()


Genai_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=Genai_api_key)

try:
        # Zero-shot classification example
        # The system prompt is used to set the context for the AI model.
        # You can customize the system prompt to guide the AI's responses.
        SYSTEM_PROMPT = """
            You are an AI expert in coading. you only know python and nothing else.
            you help users in solving there python doughts only and nothing else.
            if user asks you anything other than python, you can just rost them.
            """


        response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
                {"role": "user", "parts": [{"text": SYSTEM_PROMPT}]},
                {"role": "user", "parts": [{"text": "Hey my name is Yash Devani."}]},
        ], 
        )

        print("Response:")
        print(response)
        print("Response text:") 
        print(response.text)
except Exception as e:
        print("Error:")
        print(e)
