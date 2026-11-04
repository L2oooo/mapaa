# conversation.py
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

messages = []   # une liste vide : ce sera l'historique

while True:
    user_input = input("\nToi :")
    messages.append({"role": "user", "content": user_input})
    if user_input.lower() in ("quit", "exit"):
        break   
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=3000,
        system="Tu es MAPAA, le coach de Léo pendant son Winter Arc.",
        messages=messages,
    )
    for block in response.content:
        if block.type == "text":
            print(block.text)
    messages.append({"role": "assistant", "content": response.content})