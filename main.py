import google.generativeai as genai
import os
from dotenv import load_dotenv
from context_data import *
from utils import detect_intent

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

current_topic = None
step = 0

def get_context(topic):
    if topic == "admissions":
        return ADMISSIONS_CONTEXT
    elif topic == "philosophy":
        return PHILOSOPHY_CONTEXT
    elif topic == "fees":
        return FEES_CONTEXT
    elif topic == "visit":
        return VISIT_CONTEXT
    elif topic == "contact":
        return CONTACT_CONTEXT
    else:
        return ""

def process_user_input(user_input):
    global current_topic, step
    intent = detect_intent(user_input)

    if current_topic is None:
        if intent:
            current_topic = intent
            step = 1
        else:
            return "I'm sorry, I couldn't understand. Can you please clarify your question?"

    if current_topic:
        prompt = f"{get_context(current_topic)}\nUser: {user_input}\nBot:"
        response = model.generate_content(prompt)
        step += 1
        if step >= 3:  # reset after 3 turns
            current_topic = None
            step = 0
        return response.text
    else:
        return "I'm not sure how to help with that."

# Run the chatbot
if __name__ == "__main__":
    print("Welcome to Prakriti School Chatbot! (Type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Thank you! Have a great day!")
            break
        response = process_user_input(user_input)
        print("Bot:", response)
