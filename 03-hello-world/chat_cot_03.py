from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

Genai_api_key = os.getenv("GEMINI_API_KEY")         
client = genai.Client(api_key=Genai_api_key)

# chain of thought (CoT) example 
# The system prompt is used to set the context for the AI model.
# You can customize the system prompt to guide the AI's responses.
SYSTEM_PROMPT = """
           you are an helpfull Ai assistant. who is specialized in resolving user queries.
           for the given user input , analyse the input and break down the problem step by step

           the steps are you get a user input, you analyse, you think, you think, and think for several times and then return the output with an explanation.

           follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result"

           Example:
           Input: what is 2 + 2?
           Output: {{"step": "analyse", "content": "Alright, the user is intreaseted in maths query and he is asking a basic arthmetic operation."}}
            Output: {{"step": "think", "content": "to peform this addition , I must go from left to right and add all the operands."}}
            Output: {{"step": "output", "content": "The result of 2 + 2 is 4."}}
            Output: {{"step": "validate", "content": "I have checked the result and it is correct."}}
            Output: {{"step": "result", "content": "The result of 2 + 2 is 4."}}



            """

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        {"role": "user", "parts": [{"text": SYSTEM_PROMPT}]},
        {"role": "user", "parts": [{"text": "What is 5 / 2 * 3 to the power of 4"}]},
    ],
)

print("\n \n ","Response:" , response.candidates[0].content.parts[0] ,"\n \n")