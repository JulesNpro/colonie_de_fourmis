import random

class Fourmi:
    energie = 0 
    ### classe mère Fourmi ###
    def __init__(self, nom, energie, force, vitesse):
        self.nom = nom
        self.energie = energie
        self.force = force
        self.vitesse = vitesse
        @classmethod
        def se_deplacer(cls) : 
        # deplacer la fourmi, ce qui consmme de l'énergie
            if cls.energie_class > 0:
                cls.energie_class -= 1
                print(f"Une fourmi se déplace. Énergie de la colonie restante : {cls.energie_class}.")
            else : 
                print("la colonie n'a plus d'énegie pour se déplacer")


        
class Ouvriere(Fourmi):
    def collecter_nourriture(self):
        #Collecter de la nourriture pour la colonie
        nourriture = random.randint(1,5)
        print(f"{self.nom} a collecté de la nourriture et la ramène à la colonie.")
        return nourriture

class Soldat(Fourmi):
    def defendre_colonie(self):
        #Défendre la colonie contre une menace
        print(f"{self.nom} se bat pour défendre la colonie avec une force de {self.force}.")

class Reine(Fourmi):
    def produire_fourmis(self):
        #Produire de nouvelles fourmis
        nouvelles_fourmis = random.randint(1,3)
        print(f"La reine {self.nom} produit de nouvelles fourmis pour agrandir la colonie.")
        return nouvelles_fourmis
    
    
    ##Création de la colonie
    colonie = []
    Reine = []
    #ajout des ouvrieres : 
    for i in range(5): 
        colonie.append(Ouvriere(f"ouvrière_{i+1}", energie=random.randint(5,10), force = 2, vitesse=5))
    
    #ajout des soldat : 
    for i in range(3): 
        colonie.append(Soldat(f"Soldat_{i+1}", energie=random.randint(6,12), force = random.randint(5,8), vitesse=3))
    
    #ajout de la reine 
    colonie.append(Reine("Reine", energie=20, force=10, vitesse=1))   
    
    #------
    nourriture_totale = 0
    nouvelles_fourmis_totales = 0
    
    for fourmi in colonie : 
        if isinstance(fourmi, Ouvriere): 
            nourriture_totale += fourmi.collecter_nourriture()
        elif isinstance(fourmi, Soldat) : 
            fourmi.defendre_colonie()
        elif isinstance(fourmi,Reine):
            nouvelles_fourmis_totales += fourmi.produire_fourmis()