# hello.py
from dotenv import load_dotenv
import anthropic

load_dotenv()                   # charge ANTHROPIC_API_KEY depuis le fichier .env
client = anthropic.Anthropic()  # lit la clé automatiquement dans l'environnement

response = client.messages.create(
    model="claude-haiku-5-5",   # le modèle le moins cher, idéal pour tester
    max_tokens=1500,             # longueur maximale de la réponse, en tokens
    system="Tu es MAPAA, le coach de Léo pendant son Winter Arc.",
    messages=[
        {"role": "user", "content": "Salut, aide-moi à planifier mon après-midi."}
    ],
)

for block in response.content:
    print(f"--- bloc de type : {block.type} ---")
    if block.type == "text":
        print(block.text)
    elif block.type == "thinking":
        print(block.thinking)

print(response.usage) # tokens consommés en entrée et en sortie
print(response.stop_reason)      