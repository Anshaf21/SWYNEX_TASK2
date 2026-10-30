#=================================#
# Update the code & add Exception #
#=================================#
from google import genai
import os

#---------------------------------------------------
#   1. Configure Gemini
#---------------------------------------------------
GEMINI_API_KEY = ""
client = genai.Client(api_key=GEMINI_API_KEY)

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
- give details line by line(next line)
Eg:
--------------------------------------------------------------------------------------------
  Sigiriya                                                                                  
--------------------------------------------------------------------------------------------
Central Province
Ancient rock fortress and palace ruins, UNESCO World Heritage Site with stunning frescoes and landscaped gardens.
with emojis

description is 50 correctors in oneline
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

try:
    user_msg = input("Ask AI : ")
    response = chat.send_message(user_msg)
    answer = response.text
    
except Exception as e:
    answer = f"Error: Unavailable {e}"

print(answer)
