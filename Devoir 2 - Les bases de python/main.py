# Exercice : TP bases de Python

donnees = [ 
    ("Sara", "Math", 12, "G1"),
    ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"),
    ("Bouchra", "Info", "abc", "G2"),
    ("", "Math", 10, "G1"),
    ("Yassine", "Info", 22, "G2"),
    ("Ahmed", "Info", 13, "G2"),
    ("Adam", "Math", None, "G1"),
    ("Sara", "Chimie", 16, "G1"),
    ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3"),
    ("Hana", "Info", 8, "G1"),
]

# PARTIE 1 : Nettoyage et Validation

def valider(enregistrement):
    nom = enregistrement[0]
    matiere = enregistrement[1]
    note = enregistrement[2]
    groupe = enregistrement[3]
    
    # Vérification si le nom est vide ou non
    if nom == "" or nom is None:
        return False, "Nom vide"
    
    # Vérification si la matière est vide ou non
    if matiere == "" or matiere is None:
        return False, "Matiere vide"
    
    # Vérification si le groupe est vide ou non
    if groupe == "" or groupe is None:
        return False, "Groupe vide"

    # Vérification si la note est numerique
    if note is None or type(note) is str:
        return False, "La note n'est pas numerique"
    
    # Vérification de la note est ds l'intervalle [0, 20]
    if note < 0 or note > 20:
        return False, "La note doit etre entre 0 et 20"
    
    return True, float(note)

valides = []
erreurs = []
doublons_exact = []
vu = []

for entry in donnees:
    # Détection des doublons exacts
    if entry in vu:
        doublons_exact.append(entry)
    else:
        vu.append(entry)
        resultat = valider(entry)
        if resultat[0]:
            # Nouveau tuple avec la note en float
            valides.append((entry[0], entry[1], resultat[1], entry[3]))
        else:
            erreurs.append({"ligne": entry, "raison": resultat[1]})

print("----- PARTIE 1: Nettoyage et Validation -----")
print("Valides:")
for _ in valides:
    print(_, end="\n")
print() 
print("Erreurs:")
for _ in erreurs:
    print(_, end="\n")
print()
print("Doublons:")
for _ in doublons_exact:
    print(_, end="\n")
print("*********************************************\n")

# PARTIE 2 : Structuration

# structure = { "G1": { "Sara": { "Math": 12.0 } } }
structure = {}

for row in valides:
    # On récupère les informations par index [0, 1, 2, 3]
    nom = row[0]
    matiere = row[1]
    note = row[2]
    groupe = row[3]
    
    # 1. Création du groupe s'il n'existe pas
    if groupe not in structure:
        structure[groupe] = {}
    
    # 2. Création de l'élève dans ce groupe s'il n'existe pas
    if nom not in structure[groupe]:
        structure[groupe][nom] = {}
        
    # 3. Ajout de la note pour la matière
    structure[groupe][nom][matiere] = note

# Anomalies : étudiants dans plusieurs groupes
etudiant_groupes = {}
for row in valides:
    nom = row[0]
    groupe = row[3]
    
    if nom not in etudiant_groupes:
        etudiant_groupes[nom] = []
    
    # Eviter d'ajouter le même groupe plusieurs fois pour le même étudiant
    if groupe not in etudiant_groupes[nom]:
        etudiant_groupes[nom].append(groupe)

anomalies = {}
for nom in etudiant_groupes:
    groupes_de_liste = etudiant_groupes[nom]
    if len(groupes_de_liste) > 1:
        anomalies[nom] = groupes_de_liste

print("--------- PARTIE 2 : Structuration ----------")
print("Structure:")
for groupe_ in structure:
    print("Groupe:", groupe_, end="\n")
    for eleve_ in structure[groupe_]:
        print("\tEleve:", eleve_, end="\n")
        for matiere_ in structure[groupe_][eleve_]:
            print("\t\t", matiere_, ":", structure[groupe_][eleve_][matiere_])
print()
print("Anomalies:")
for nom_ in anomalies:
    print(nom_, "\t", anomalies[nom_], end="\n")
print("*********************************************\n")


# PARTIE 3 : Calculs et Statistiques

def somme_recursive(liste):
    if len(liste) == 0:
        return 0
    return liste[0] + somme_recursive(liste[1:])

moyennes_etudiants = {}
moyennes_matieres = {}
compteur_matieres = {}

for groupe in structure:
    for nom in structure[groupe]:
        notes_etudiant = []
        for mat in structure[groupe][nom]:
            note = structure[groupe][nom][mat]
            notes_etudiant.append(note)
            
            # Pour la moyenne par matière
            if mat not in moyennes_matieres:
                moyennes_matieres[mat] = 0
                compteur_matieres[mat] = 0
            moyennes_matieres[mat] = moyennes_matieres[mat] + note
            compteur_matieres[mat] = compteur_matieres[mat] + 1
            
        somme = somme_recursive(notes_etudiant)
        moyennes_etudiants[nom] = somme / len(notes_etudiant)

for mat in moyennes_matieres:
    moyennes_matieres[mat] = moyennes_matieres[mat] / compteur_matieres[mat]

print("---- PARTIE 3 : Calculs et Statistiques -----")
print("Moyennes Etudiants:", moyennes_etudiants)
print("Moyennes Matieres:", moyennes_matieres)
print("*********************************************\n")


# PARTIE 4 : Analyse Avancée

# 1. Multiples notes pour une même matière (Saisie erronée / duplication)
notes_multiples = []
vu_nom_matiere = []
for row in valides:
    nom = row[0]
    matiere = row[1]
    cle = (nom, matiere)
    if cle in vu_nom_matiere:
        if cle not in notes_multiples:
            notes_multiples.append(cle)
    else:
        vu_nom_matiere.append(cle)

# 2. Profils incomplets (matières manquantes dans le groupe)
profils_incomplets = []
for groupe in structure:
    # Trouver toutes les matières enseignées dans ce groupe
    toutes_matieres = []
    for nom in structure[groupe]:
        for mat in structure[groupe][nom]:
            if mat not in toutes_matieres:
                toutes_matieres.append(mat)
    
    # Vérifier si chaque étudiant a toutes les matières
    for nom in structure[groupe]:
        mat_etudiant = []
        for mat in structure[groupe][nom]:
            mat_etudiant.append(mat)
            
        manquantes = []
        for m in toutes_matieres:
            if m not in mat_etudiant:
                manquantes.append(m)
        
        if len(manquantes) > 0:
            profils_incomplets.append((nom, groupe, manquantes))

# 3. Performance de groupe (moyenne générale du groupe < 10)
alertes_groupes = []
for groupe in structure:
    somme_groupe = 0
    nb_notes = 0
    for nom in structure[groupe]:
        for mat in structure[groupe][nom]:
            somme_groupe = somme_groupe + structure[groupe][nom][mat]
            nb_notes = nb_notes + 1
    
    moyenne_g = somme_groupe / nb_notes
    if moyenne_g < 10:
        alertes_groupes.append((groupe, moyenne_g))

# 4. Instabilité (écart > 5 entre min et max)
instables = []
for groupe in structure:
    for nom in structure[groupe]:
        notes = []
        for mat in structure[groupe][nom]:
            notes.append(structure[groupe][nom][mat])
        
        if len(notes) > 1:
            minimum = notes[0]
            maximum = notes[0]
            for n in notes:
                if n < minimum: minimum = n
                if n > maximum: maximum = n
            
            if (maximum - minimum) > 5:
                instables.append((nom, maximum - minimum))

print("-------- PARTIE 4 : Analyse Avancée ---------")
print("Notes multiples:", notes_multiples)
print("Profils incomplets:", profils_incomplets)
print("Alertes groupes:", alertes_groupes)
print("Instabilites:", instables)
print("*********************************************\n")