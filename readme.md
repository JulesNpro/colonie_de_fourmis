#### Projet colonie de fourmis
#### Groupe poulpe : Saadia, Yann, Jules

# Fourmis Simulation App
## Description

##### Cette application simule une colonie de fourmis composée de différentes classes : ouvrières, soldats et une reine. Chaque fourmi effectue des actions comme collecter de la nourriture, défendre la colonie ou produire de nouvelles fourmis. L'énergie de la colonie est partagée et est consommée lorsque les fourmis se déplacent.
Prérequis

    Python 3.x doit être installé sur votre machine.
    Pour vérifier que Python est installé, vous pouvez exécuter la commande suivante dans un terminal :

    bash

    python --version

    Modules supplémentaires : Aucun module externe n'est requis pour cette application, vous pouvez utiliser les bibliothèques standard de Python.

Installation

    Clonez ce dépôt ou copiez le code source dans votre projet local :

    bash

git clone <URL_du_dépôt>

Accédez au répertoire du projet :

bash

    cd <nom_du_répertoire>

Lancement de l'application

    Exécutez le script principal fourmis.py dans un terminal pour démarrer la simulation :

    bash

    python app.py

    L'application simule les actions des fourmis dans la colonie, et affiche les résultats tels que la nourriture collectée, les nouvelles fourmis produites, et l'énergie restante de la colonie.

Best Practices
1. Structure du code

    Organisation des classes : Le code est organisé en trois classes principales qui héritent de la classe mère Fourmi. Cela permet une modularité et facilite les évolutions futures de l'application.
        Ouvriere : Responsable de la collecte de nourriture.
        Soldat : Défend la colonie.
        Reine : Produit de nouvelles fourmis.

    Méthodes de classe (@classmethod) : La méthode se_deplacer est utilisée avec le décorateur @classmethod pour représenter une action globale qui affecte l'énergie partagée par la colonie.

2. Ajout de fonctionnalités

    Facilité d'ajout de nouvelles actions : Si vous souhaitez ajouter de nouvelles actions pour une fourmi (par exemple, exploration), vous pouvez simplement définir une nouvelle méthode dans les sous-classes concernées.

    Attributs partagés : L'attribut energie_class est un bon exemple d'attribut partagé au niveau de la classe, garantissant que toutes les instances accèdent à la même ressource énergétique.

3. Gestion de l'énergie

L'énergie est un élément clé dans cette simulation. Chaque action de déplacement réduit l'énergie de la colonie entière. Assurez-vous de suivre l'état de l'énergie via la méthode se_deplacer.

4. Modularité et réutilisabilité

    Si vous voulez réutiliser ce projet ou l'étendre à d'autres types d'insectes, vous pouvez facilement le faire en ajoutant de nouvelles sous-classes à la classe mère Fourmi.
    La gestion de la nourriture et des nouvelles fourmis est conçue pour être flexible et adaptable à des scénarios plus complexes.

Débogage

Si vous rencontrez des erreurs lors de l'exécution du script, assurez-vous que vous utilisez la bonne version de Python et que le code source est correctement copié.