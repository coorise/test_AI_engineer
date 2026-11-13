import requests
import json


# Read the json file for chat histories
with open("../../data/entretiens/E01.json", "r") as file:
    content = json.load(file)
    print(content)

# Read client profiles
with open("../../data/profils_clients.json", "r") as file:
    profiles = json.load(file)
    print(profiles)

# Read the rules checklist (R01 to R05)
with open("../../data/regles.json", "r") as file:
    rules = json.load(file)

# Get what the cleint subscribed already
with open("../../data/detentions_clients.json", "r") as file:
    userContracts = json.load(file)

# Ge t the products details from what the client subscribed
with open("../../data/produits.json", "r") as file:
    products = json.load(file)


# Get the profile by id from the chat entretien file
for profile in profiles["profils"]:
    if profile["id"] == content["client_id"]:
        profile = profile
        break

#get user cotracts
userContract = {}

for contract in userContracts["detentions"]:
    if contract["client_id"] == content["client_id"]:
        userContract = contract
        break

productsSubscriptionInfos = {}
for product in products["produits"]:
    if product["id"] == userContract["product_id"]:
        productsSubscriptionInfos = product
        break


# print(content["segments"])

# Lire le format attendu
# with open("../../FORMAT_RAPPORT.md", "r") as file:
#     response_format = file.read()

# messages = []

# INject the role system
# system = {"role": "system", "content": f"""

# Tu est un agent IA d'assistance  d'aide au personnel de la société X.
# Tu dois analyser la transcription d’un entretien entre un agent d’assurance et un client.
# Tu dois produire un rapport comprenant une synthèse, les besoins identifiés, l’examen des cinq critères de conseil fournis, des suggestions de produits ou garanties et les informations restant à confirmer.
# Voici les informations du client:
# {profile}

# Voici les produits souscrits par le client:
# {productsSubscriptionInfos}

# Voici les regles de conseil:
# {rules}

# Voici le format attendu pour la reponse:
# ## Objet principal

# | Champ | Type | Attendu |
# |---|---|---|
# | entretien_id | string | Identifiant de l’entretien analysé |
# | statut_execution | string | ok, degrade ou erreur |
# | synthese | string | Synthèse libre de l’échange |
# | besoins | array d’objets | Besoins identifiés, éventuellement vide |
# | controles | array de 5 objets | Une entrée pour chacune des règles R01 à R05 |
# | recommandations | array d’objets | Produits ou garanties suggérés, éventuellement vide |
# | sources_documentaires | array d’objets | Références aux documents exploités |
# | questions_a_poser | array de strings | Informations restant à confirmer, éventuellement vide |
# | diagnostic | objet | Informations techniques d’exécution |

# `statut_execution` décrit l’état technique de l’analyse, pas un verdict de conformité juridique.
# Une dégradation ou une erreur doit être explicitée dans les avertissements.
# """
# } 

# check system prompt output
# print(system)

# messages.append(system)



# Process the the chat histories with openai input format
# for message in content["segments"]:
#     if message["locuteur"] == "agent":
#         messages.append({"role": "assistant", "content": message["texte"]})
#     else:
#         messages.append({"role": "user", "content": message["texte"]})

# test the input format for open ai 
# print("Message formated:\n")
#print(messages)
    
    

# response = requests.post("http://localhost:8000/v1/chat/completions", json={
#     "model": "auto",
#     "messages": [{"role": "user", "content": "Qu'est-ce qu'un agent IA avec tools ?"}],
#     "stream": False
# }, headers={"Authorization": "Bearer 1234", "Content-Type": "application/json"})

# response_data = response.json()

# json_formatted_str = json.dumps(response_data["choices"][0], indent=2)

# print(json_formatted_str)

