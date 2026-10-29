from google import genai
import os
#---------------------------------------------------
#   1. configure Gemini
#---------------------------------------------------

GEMINI_API_KEY = "SECRET-KEY"
client = genai.Client(api_key = GEMINI_API_KEY)

#---------------------------------------------------
#    2. Load places from txt
#---------------------------------------------------
with open("places.txt", "r", encoding="utf-8") as f:
    kb = f.read()

#---------------------------------------------------
#   3. Prompt
#---------------------------------------------------
prompt = f"""You are a friendly Sri Lanka Tourist Guide chatbot.
Your job:
- Answer tourists' questions about places, history, and travel tips.
- Recommend nearby attractions when asked.
- Mention entry fees and visiting hours when relevant.
- Be friendly and concise. Reply in 3-5 points form max, each with the
  place name, distance if available, and a one-line reason to visit.

All places data:
{kb}
"""
# ----------------------------
# Initialize Chat
# ----------------------------
model = "gemini-2.5-flash"

chat = client.chats.create(
    model=model,
    config={
        'system_instruction': prompt
    }
)

user_msg = input("Ask AI : ")
response = chat.send_message(user_msg)
print(response.text)
