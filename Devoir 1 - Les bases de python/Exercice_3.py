# EXERCICE III : Vérification de mot de passe

MOT_DE_PASSE_CORRECT = "1234567890"

# Demander le mot de passe initial
tentative = input("Veuillez saisir le mot de passe : ")

# Boucler tant que le mot de passe est incorrect
while tentative != MOT_DE_PASSE_CORRECT:
	print("Mot de passe incorrect. Réessayez.")
	tentative = input("Veuillez saisir le mot de passe : ")

# Message de confirmation si correct
print("Mot de passe correct ! Accès autorisé.")