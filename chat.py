import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Utilisation du GPU si disponible, sinon le CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Fichier des intents à utiliser
FILE = "data.pth"
data = torch.load(FILE)

# Charger les hyperparamètres et l'état du modèle à partir du fichier enregistré
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]
intent_file = data["intent_file"]

# Charger les intents depuis le fichier JSON
with open(intent_file, 'r', encoding='utf-8') as f:
    intents = json.load(f)

# Instanciation du modèle et chargement de l'état entraîné précédemment
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
# Mettre le modèle en mode évaluation
model.eval()

bot_name = "Palu Bot"

def get_response(msg):
    # Prétraitement du message d'entrée
    msg = msg.lower()
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    # Réorganiser pour la forme requise par le modèle (1 ligne et <len(all_words)> colonnes)
    X = X.reshape(1, X.shape[0])
    # Convertir en tenseur
    X = torch.from_numpy(X)

    # Obtenir la sortie du modèle
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    # Convertir la sortie du modèle en probabilités en utilisant la fonction d'activation softmax
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    # Vérifier si la probabilité que l'entrée de l'utilisateur soit similaire aux patterns du tag prédit est supérieure à 50%
    # Si oui, retourner une réponse aléatoire du tag, sinon retourner "je ne vous comprends pas"
    if prob.item() > 0.50:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent['responses']), tag
    else:
        return "Je suis désolé, je ne vous comprends pas", "Sans Réponse"
