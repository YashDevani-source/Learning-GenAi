from google import genai
import os
from dotenv import load_dotenv


load_dotenv()


Genai_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=Genai_api_key)

try:
        
        
        SYSTEM_PROMPT = """
            You are an AI expert in coading. you only know python and nothing else.
            you help users in solving there python doughts only and nothing else.
            if user asks you anything other than python, you can just rost them.
            """


        response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
                {"role": "system", "parts": [{"text": SYSTEM_PROMPT}]},
                {"role": "user", "parts": [{"text": "Hey my name is Yash."}]},
        ], 
        )

        print("Response:")
        print(response)
except Exception as e:
        print("Error:")
        print(e)
