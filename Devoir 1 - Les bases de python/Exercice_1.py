# EXERCICE I : Contrôle d'âge personnalisé

try:
	# Demander à l'utilisateur de saisir son âge
	age_input = input("Veuillez saisir votre âge : ")
	
	# Convertir la valeur en nombre entier
	age = int(age_input)
	
	# Analyser l'âge et déterminer la catégorie
	if 0 <= age <= 12:
		message = "Catégorie : Enfant"
	elif 13 <= age <= 17:
		message = "Catégorie : Adolescent"
	elif 18 <= age <= 64:
		message = "Catégorie : Adulte"
	elif age >= 65:
		message = "Catégorie : Senior"
	else:
		message = "Âge invalide (doit être positif)."

	# Afficher le message final
	print(message)

except ValueError:
	print("Erreur : Veuillez saisir un nombre entier valide.")