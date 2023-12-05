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

while True:
    password = input("Entrez votre mot de passe : ")

    if len(password) < 8:
        print("Le mot de passe doit avoir au moins 8 caractères.")
        continue
    elif not any(char in symbole for char in password):
        print("Le mot de passe doit contenir au moins un caractère spécial.")
        continue
    elif not any(char in lettre_majuscule for char in password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        continue
    
    # Vérifier les exigences de sécurité
    if not any(char in password for char in symbole):
        print("Mot de passe invalide. Veuillez choisir un nouveau mot de passe.")
        continue
    
    print("Mot de passe valide. Merci!")
    break
hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Mot de passe crypté avec succès :", hashed_password)




