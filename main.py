import openai
import os

# Set your OpenAI API key
openai.api_key = "API KEY"

# Define the prompt for the chatbot
prompt = "Hello, how can I assist you today?"

# Set the chatbot model and parameters
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 50

# Define a function to generate a response from the chatbot
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    message = response.choices[0].text.strip()
    return message

# Start the chatbot loop
while True:
    # Get user input
    user_input = input("User: ")

    # Exit loop if user says "bye"
    if user_input.lower() == "bye":
        break

    # Generate and print the chatbot's response
    chatbot_response = generate_response(prompt + "\nUser: " + user_input + "\nBot:")
    print("Bot: " + chatbot_response)
