from dotenv import load_dotenv
from google import genai
import os 

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


text = "The quick brown fox jumps over the lazy dog."
result = client.models.embed_content(
    model="gemini-embedding-exp-03-07",
    contents=text,
)

print(f"Text: {text}")
print(f"Result: {result.embeddings[0]}")
print("Len:", len(result.embeddings))
