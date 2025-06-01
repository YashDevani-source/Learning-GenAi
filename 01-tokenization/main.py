import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, world! This is a test of the tiktoken library."
tokens = enc.encode(text)
print(f"Text: {text}")
print(f"Tokens: {tokens}")
print(f"Number of tokens: {len(tokens)}")
# Decode the tokens back to text
decoded_text = enc.decode(tokens)
print(f"Decoded text: {decoded_text}")
# Check if the decoded text matches the original text
assert decoded_text == text, "Decoded text does not match the original text."
# Tokenize a longer text
long_text = "This is a longer piece of text that we will use to test the tiktoken library. It should be able to handle multiple sentences and various punctuation marks, such as commas, periods, and exclamation points!"
long_tokens = enc.encode(long_text)
print(f"Long text: {long_text}")
print(f"Long tokens: {long_tokens}")
print(f"Number of long tokens: {len(long_tokens)}")
# Decode the long tokens back to text
long_decoded_text = enc.decode(long_tokens)       
print(f"Long decoded text: {long_decoded_text}")       
# Check if the decoded text matches the original text
assert long_decoded_text == long_text, "Long decoded text does not match the original text."    