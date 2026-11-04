# conversation.py
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

messages = []   # une liste vide : ce sera l'historique

messages.append({"role": "user", "content": "Salut, j'ai boxe à 19h."})

r1 = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1500,
    messages=messages,
)

for block in r1.content:
    if block.type == "text":
        print(block.text)

messages.append({"role": "assistant", "content": r1.content})
messages.append({"role": "user", "content": "A quelle heure ai-je boxe ?"})

r2 = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1500,
    messages=messages,   # 3 messages maintenant
)

for block in r2.content:
    if block.type == "text":
        print(block.text)

print("Tour 1 :", r1.usage.input_tokens, "tokens en entrée")
print("Tour 2 :", r2.usage.input_tokens, "tokens en entrée")