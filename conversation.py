# conversation.py
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

with open("context/winter-arc.md", "r", encoding="utf-8") as file:
    plan = file.read()

SYSTEM = f"""Tu es MAPAA, le coach de Léo pendant son Winter Arc.
Voici son plan complet, réfère-toi toujours à lui :

{plan}"""

messages = []   # une liste vide : ce sera l'historique

while True:
    user_input = input("\nToi :")
    messages.append({"role": "user", "content": user_input})
    if user_input.lower() in ("quit", "exit"):
        break   
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=3000,
        system=SYSTEM,
        messages=messages,
    )
    for block in response.content:
        if block.type == "text":
            print(block.text)
    messages.append({"role": "assistant", "content": response.content})

print(response.usage) # tokens consommés en entrée et en sortie
