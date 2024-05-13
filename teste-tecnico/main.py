import requests
import firebase_admin
from firebase_admin import firestore, credentials

########################################################################################
snapshot_version = "663d6233911526d19f7d8d1a"
api_key = "4dc62d17-0e61-11ef-9ad6-a2a378993290"
headers = {"api-key": api_key}

def get_new_chat():
    data = {
        "chatbot": 164,
        "snapshot_version": snapshot_version
    }

    response = requests.post("https://api.verbeux.com.br/dialog-manager-proxy/", json=data, headers=headers)

    if (response.status_code != 200 or "data" not in response.json()):
        return None

    return response.json()["data"]

def send_message(chat_id, message):
    data = {"message": message}

    response = requests.put(f"https://api.verbeux.com.br/dialog-manager-proxy/{chat_id}", json=data, headers=headers)

    if (response.status_code != 200 or "data" not in response.json()):
        return ""
    
    return response.json()["data"]["response"][0]["data"] or ""

########################################################################################
cred = credentials.Certificate("D:\\Documentos\\Programar\\verbeux\\chatbot-avaliacoes-firebase-adminsdk-e8k2s-edbb8c5bea.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_database(message: str, positive: bool):
    review = {"review": message}

    if (positive):
        doc_ref = db.collection("PositiveReviews")
        doc_ref.add(review)
    
    else:
        doc_ref = db.collection("NegativeReviews")
        doc_ref.add(review)

def print_database(collection):
    docs = collection.stream()

    for doc in docs:
        print(doc.id)
        print("Avaliação: " + doc.get("review"))
        print("\n")

########################################################################################
while (True):
    choice = int(input("O que você quer fazer?\n" +
                    "1 - Falar com chatbot\n" +
                    "2 - Ver avaliações\n" +
                    "0 - Sair\n\n" +
                    "Sua escolha: "))
    
    if (choice == 1):
        new_chat_data = get_new_chat()
        chat_id = new_chat_data["id"]

        print(new_chat_data["id"])

        while (True):
            message = input("Digite a mensagem: ")
            response = send_message(chat_id, message)

            print("\nChatBot: " + response + "\n")

            if (response == "Adeus!"):
                break

            elif ("positivo" in response):
                add_database(message, True)

            elif ("negativo" in response):
                add_database(message, False)

        print("| Sistema: Chat finalizado. |")

    elif (choice == 2):
        collections = db.collections()

        for coll in collections:
            print("----- | " + coll.id + " | -----")
            print()
            print_database(coll)

    else:
        print("| Sistema: Saindo... |")
        break
