
import random
import string
import hashlib
import json
import os

# Caractères
lettre_majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettre_minuscule = "abcdefghijklmnopqrstuvwxyz"
chiffre = "0123456789"
symbole = ['!', '@', '#', '$', '%', '^', '&', '*']
caractere_no_symbole = lettre_majuscule + lettre_minuscule + chiffre

# Saisie du mot de passe
while True:
    password = input("Entrez votre mot de passe : ")

    if len(password) < 8:
        print("Le mot de passe doit avoir au moins 8 caractères.")
    elif not any(char in symbole for char in password):
        print("Le mot de passe doit contenir au moins un caractère spécial.")
    elif not any(char in lettre_majuscule for char in password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
    else:
        print("Mot de passe valide. Merci!")
        break

# Hachage du mot de passe
hashed_password = hashlib.sha256(password.encode()).hexdigest()
print("Mot de passe crypté avec succès :", hashed_password)

# Spécifiez le chemin complet de votre fichier JSON
historique_path = "C:\\Users\\odura\\laplateforme\\Password generator\\password\\historique.json"

# Vérifiez si le fichier existe
if os.path.exists(historique_path):
    # Charger l'historique existant
    with open(historique_path, "r") as f:
        historique = json.load(f)
else:
    # Créer un nouveau fichier d'historique si le fichier n'existe pas
    historique = []

# Ajouter le nouveau mot de passe à l'historique
historique.append({"hashed_password": hashed_password, "original_password": password})

# Sauvegarder l'historique mis à jour dans le fichier JSON
with open(historique_path, "w") as f:
    json.dump(historique, f, indent=2)

print("Mot de passe ajouté à l'historique avec succès.")















