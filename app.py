import random

class Fourmi:
    energie_class = 0  # Énergie partagée de la colonie, initialisée à 10 pour tester

    def __init__(self, nom, energie, force, vitesse, special):
        self.nom = nom
        self.energie = energie
        self.force = force
        self.vitesse = vitesse
        self.__special = special

    @property
    def pouvoir_special(self):
        return self.__special
    
    @pouvoir_special.setter
    def pouvoir_special(self, bonus):
        if bonus >= 0:
            self.__special = bonus
        else:
            raise ValueError("Le bonus doit être positif ou nul.")
        
    def Kimeraboost(self):
        if self.energie == 0:  # Vérifiez si l'énergie de la fourmi est à zéro
            boost = self.pouvoir_special  # Utiliser le pouvoir spécial comme boost
            if boost > 0:  # S'assurer que le boost est positif
                self.energie += boost
                Fourmi.energie_class += boost  # Restaurer l'énergie de la colonie
                print(f"{self.nom} reçoit un boost d'énergie : +{boost} énergie. Nouvelle énergie : {self.energie}.")
           
           ## SORTIR DE LA BOUCLE DU KIMERA BOOST
            else:
                print(f"{self.nom} n'a pas de pouvoir spécial pour le boost.")

    @classmethod
    def se_deplacer(cls, fourmi):
        # Déplacer une fourmi, ce qui consomme de l'énergie partagée par la colonie
        if cls.energie_class > 0:
            cls.energie_class -= 1
            print(f"Une fourmi se déplace. Énergie de la colonie restante : {cls.energie_class}.")
        else:
            print(f"La colonie n'a plus d'énergie pour se déplacer. Activation du KimeraBoost.")
            fourmi.Kimeraboost()
            print(f"Valeur de l'énergie boostée : {fourmi.energie} (après activation du boost)")


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
    colonie.append(Ouvriere(f"Ouvrière_{i+1}", energie=random.randint(5, 10), force=2, vitesse=5, special=1))

# Ajout des soldats
for i in range(3):
    colonie.append(Soldat(f"Soldat_{i+1}", energie=random.randint(6, 12), force=random.randint(5, 8), vitesse=3, special=1))

# Ajout de la reine avec un pouvoir spécial
reine = Reine(f"Kimera", energie=20, force=10, vitesse=1, special=5)  # Exemple avec pouvoir spécial de 5
colonie.append(reine)

# Simulation de la colonie
nourriture_totale = 0
nouvelles_fourmis_totales = 0

for fourmi in colonie:
    Fourmi.se_deplacer(fourmi)  # Utilisation de la méthode de classe avec l'instance de la fourmi

    if isinstance(fourmi, Ouvriere):
        nourriture_totale += fourmi.collecter_nourriture()
    elif isinstance(fourmi, Soldat):
        fourmi.defendre_colonie()
    elif isinstance(fourmi, Reine):
        nouvelles_fourmis_totales += fourmi.produire_fourmis()

# Affichage des résultats
print(f"Nourriture totale collectée : {nourriture_totale}")
print(f"Nouvelles fourmis produites : {nouvelles_fourmis_totales}")
