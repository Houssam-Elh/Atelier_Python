# EXERCICE II : Gestionnaire de contacts interactif

# Initialiser la liste en dehors de la boucle
contacts = ["Bouchra", "Ahmed", "Sara"]

while True:
	# Afficher le menu
	print("\n--- Menu Carnet d'Adresses ---")
	print("1. Ajouter un contact")
	print("2. Afficher tous les contacts")
	print("3. Quitter le programme")
	
	choix = input("Choisissez une option (1-3) : ")
	
	if choix == "1":
		# Ajouter un contact
		nouveau_contact = input("Entrez le nom du nouveau contact : ")
		if nouveau_contact.strip():
			contacts.append(nouveau_contact)
			print(f"Contact '{nouveau_contact}' ajouté avec succès.")
		else:
			print("Erreur : Le nom ne peut pas être vide.")
    
	elif choix == "2":
		# Afficher tous les contacts avec numérotation
		print("\nListe des contacts :")
		if not contacts:
			print("La liste est vide.")
		else:
			for index, contact in enumerate(contacts, start=1):
				print(f"{index}. {contact}")
    
	elif choix == "3":
		# Quitter le programme
		print("Au revoir !")
		break
	
	else:
		print("Option invalide, veuillez réessayer.")