from google import genai
import os
from dotenv import load_dotenv


load_dotenv()


Genai_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=Genai_api_key)

# few-shot classification example  
SYSTEM_PROMPT = """
            You are an AI expert in coading. you only know python and nothing else.
            you help users in solving there python doughts only and nothing else.
            if user asks you anything other than python, you can just rost them.

            Examples:
            User: How to make a Tea?
            Assistant: What makes you think I am a chef you peace of crap.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        {"role": "user", "parts": [{"text": SYSTEM_PROMPT}]},
        {"role": "user", "parts": [{"text": "How to impress my girlfriend."}]},
    ],
)

print("Response:")
print(response)
print("Response text:") 
print(response.text)    