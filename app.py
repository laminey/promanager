demandes = []
prochain_id = 1
def ajouter_demande():
    global prochain_id
    titre = input("Titre de la demande : ").strip()
    if not titre:
        print("Erreur : le titre est obligatoire.")
        return
categorie = input("Catégorie (Informatique/Maintenance/Logistique) : ").strip()
priorite = input("Priorité (Basse/Normale/Haute) : ").strip().capitalize()
if priorite not in ["Basse", "Normale", "Haute"]:
    print("Priorité invalide : priorité définie à Normale.")
    priorite = "Normale"

demande = {
    "id": prochain_id,
    "titre": titre,
    "categorie": categorie or "Autre",
    "priorite": priorite,
    "statut": "Nouvelle"
}
demandes.append(demande)
print(f"Demande #{prochain_id} créée avec succès.")
prochain_id += 1

def afficher_demandes():
    if not demandes:
        print("Aucune demande enregistrée.")
        return
    for demande in demandes:
        print(f'#{demande["id"]} | {demande["titre"]} | {demande["categorie"]} | {demande["priorite"]} | {demande["statut"]}')

def rechercher_demande():
    valeur = input("Identifiant à rechercher : ").strip()
    if not valeur.isdigit():
        print("Veuillez saisir un identifiant numérique.")
        return
    
    identifiant = int(valeur)
    for demande in demandes:
        if demande["id"] == identifiant:
            print(demande)
            return

print("Demande introuvable.")
def menu():
    while True:
        print("\n=== ProManager — V0 ===")
        print("1. Ajouter une demande")
        print("2. Afficher les demandes")
        print("3. Rechercher par identifiant")
        print("0. Quitter")
        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_demande()
        elif choix == "2":
            afficher_demandes()
        elif choix == "3":
            rechercher_demande()
        elif choix == "0":
            print("Fin de ProManager. À bientôt !")
        break
    else:
        print("Choix invalide. Recommencez.")
if __name__ == "__main__":
    menu()