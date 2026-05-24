# Import the tiktoken library used for tokenization
import tiktoken

# Load the tokenizer encoding for the GPT-4o model
encoding = tiktoken.encoding_for_model("gpt-4o")

# Input text that we want to convert into tokens
text = "Hello , my name is Harshit , i m from gorakhpur ? "

# Convert the text into token IDs
tokens = encoding.encode(text)

# Print the generated list of tokens
print("Tokens = ", tokens)