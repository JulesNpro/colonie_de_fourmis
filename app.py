import random

class Fourmi:
    energie_class = 20  # Énergie partagée de la colonie

    ### classe mère Fourmi ###
    def __init__(self, nom, energie, force, vitesse):
        self.nom = nom
        self.energie = energie
        self.force = force
        self.vitesse = vitesse

    @classmethod
    def se_deplacer(cls):
        # Déplacer une fourmi, ce qui consomme de l'énergie partagée par la colonie
        if cls.energie_class > 0:
            cls.energie_class -= 1
            print(f"Une fourmi se déplace. Énergie de la colonie restante : {cls.energie_class}.")
        else:
            print("La colonie n'a plus d'énergie pour se déplacer.")


class Ouvriere(Fourmi):
    def collecter_nourriture(self):
        # Collecter de la nourriture pour la colonie
        nourriture = random.randint(1, 5)
        print(f"{self.nom} a collecté {nourriture} unités de nourriture et la ramène à la colonie.")
        return nourriture


class Soldat(Fourmi):
    def defendre_colonie(self):
        # Défendre la colonie contre une menace
        print(f"{self.nom} se bat pour défendre la colonie avec une force de {self.force}.")


class Reine(Fourmi):
    def produire_fourmis(self):
        # Produire de nouvelles fourmis
        nouvelles_fourmis = random.randint(1, 3)
        print(f"La reine {self.nom} produit {nouvelles_fourmis} nouvelles fourmis pour agrandir la colonie.")
        return nouvelles_fourmis


## Création de la colonie
colonie = []

# Ajout des ouvrières
for i in range(5):
    colonie.append(Ouvriere(f"Ouvrière_{i+1}", energie=random.randint(5, 10), force=2, vitesse=5))

# Ajout des soldats
for i in range(3):
    colonie.append(Soldat(f"Soldat_{i+1}", energie=random.randint(6, 12), force=random.randint(5, 8), vitesse=3))

# Ajout de la reine
colonie.append(Reine(f"Kimera", energie=20, force=10, vitesse=1))

# Simulation de la colonie
nourriture_totale = 0
nouvelles_fourmis_totales = 0

for fourmi in colonie:
    Fourmi.se_deplacer()  # Utilisation de la méthode de classe

    if isinstance(fourmi, Ouvriere):
        nourriture_totale += fourmi.collecter_nourriture()
    elif isinstance(fourmi, Soldat):
        fourmi.defendre_colonie()
    elif isinstance(fourmi, Reine):
        nouvelles_fourmis_totales += fourmi.produire_fourmis()

# Affichage des résultats
print(f"Nourriture totale collectée : {nourriture_totale}")
print(f"Nouvelles fourmis produites : {nouvelles_fourmis_totales}")
