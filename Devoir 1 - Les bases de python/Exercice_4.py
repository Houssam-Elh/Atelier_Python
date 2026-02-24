# EXERCICE IV : Calculatrice Arithmétique

try:
	# Demander à l'utilisateur de saisir deux nombres
	nombre1 = float(input("Entrez le premier nombre : "))
	nombre2 = float(input("Entrez le deuxième nombre : "))
	
	# Demander de choisir une opération
	print("\nOpérations disponibles :")
	print("1 : addition")
	print("2 : soustraction")
	print("3 : multiplication")
	print("4 : division")
	
	choix = input("Choisissez une opération (1-4) : ")
	
	# Effectuer le calcul
	if choix == "1":
		resultat = nombre1 + nombre2
		print(f"Résultat : {nombre1} + {nombre2} = {resultat}")
	elif choix == "2":
		resultat = nombre1 - nombre2
		print(f"Résultat : {nombre1} - {nombre2} = {resultat}")
	elif choix == "3":
		resultat = nombre1 * nombre2
		print(f"Résultat : {nombre1} * {nombre2} = {resultat}")
	elif choix == "4":
		if nombre2 == 0:
			print("Erreur : Division par zéro impossible.")
		else:
			resultat = nombre1 / nombre2
			print(f"Résultat : {nombre1} / {nombre2} = {resultat}")
	else:
		print("Option invalide.")

except ValueError:
	print("Erreur : Veuillez saisir des nombres valides.")