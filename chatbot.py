import openai
import re
import random

openai.api_key = "Open Api Key"  # Replace with your API key

# Define the prompts and responses
prompts = [
    "What is your name?",
    "What is your favorite color?",
    "What is your favorite food?",
]

responses = [
    "My name is Chatbot. Nice to meet you!",
    "My favorite color is blue. What's yours?",
    "My favorite food is pizza. What about you?",
]

# Define the function to generate responses
def generate_response(prompt):
    prompt = prompt.lower()
    for i in range(len(prompts)):
        if re.search(prompts[i].lower(), prompt):
            return responses[i]
    return "I'm sorry, I didn't understand your question."

# Define the function to start the chat
def start_chat():
    print("Hi, I'm Chatbot. How can I help you?")
    while True:
        prompt = input("> ")
        if prompt.lower() in ["bye", "goodbye", "exit"]:
            print("Goodbye!")
            break
        response = generate_response(prompt)
        print(response)

# Start the chat
start_chat()
