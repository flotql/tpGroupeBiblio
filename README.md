# tpGroupeBiblio

Projet formation DevOPS ADRAR par Gaetan CORIN, Raphael THOMAS et Florent TOMPS

Nomenclature 

STYLE D'ECRITURE

    Class en PascalCase
    Functions, Method, Attributs, Variables,...  en CamelCase

INSTALLATION ART

Dans le terminal:  python -m ensurepip 
                   python -m pip install art

QUOI FAIRE

- Cree les differents dossiers (code,donnees,....)
    - Cree les differents fichiers (class,code,livres,users,functions,main,....)

FONCTIONNALITES DE BASE :
- Enregistrer nouveau utilisateur
- Connecter utilisateur
- Changer mdp utilisateur
- Afficher les livres disponibles par categories/auteur/genre/langue
- Recherche un livre, une categorie, un auteur, un genre
- Emprunter/rendre livre
- Prolonger un emprunt
- D'autres fonctionnalites de votre choix

CLASS : 
- Personne / User (Raph)
    - Personne : Definir ID et changement de mdp
    - User : Gestion Grade et Emprunt
- Livre / BD (Gaetan)
    - Livre : Definir Ref
    - BD : 
- Bibliotheque (Florent)
    Import export utilisateurs et livres / affichage livres 
    
Functions : ()

Main : () 
- il doit etre le plus epure possible


FONCTIONS FUTUR:

User
- Grade : 
    - monte en grade avec un nombre de livre emprunter (garde le meme prix)
    - monte en grade en payant l'abonnement sup
    - désinscription
Regex
- Class : admin (heritage personne)
