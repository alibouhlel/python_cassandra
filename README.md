# test_technique_python_cassandra
* Tout d'abord il faut installer les dépendances nécessaires pour l'application. Tout est indiqué dans le fichier requirements.txt
## Partie 1 : Filtrage du contenu non valide du fichier clients.txt
* Le filtrage a été effectué sur les champs Nom, Sexe, Email et Date de naissance
* un nom est impérativement composé de lettres alphabétiques 
* le sexe est égale H ou F
* le champs email est le hash par la méthode sha256 donc il doit être de longueur 64 et composé de chiffres et de lettres à condition que les lettres soient toutes des majuscules ou bien des minuscules.
*  et pour ce faire j'ai utilisé pandas pour manipuler les data frame et les expressions régulière pour le filtrage
## Partie 2 : Chargement des données valides dans une table Cassandra
* utilisation du cassandra-driver pour faire des requêtes CQL comme la création de la table Clients ensuite l'insertion du contenu du nouveau fichier valide dans la table 
* J'ai utilisé l'image docker officiel de cassandra (comme indiqué dans l'énoncé) et voici les commandes exécutées pour faire le pull de l'image, lancer le serveur cassandra et interroger la base de donnée avec le CQL Shell  
```sh
$ docker pull cassandra
$ docker run --name nom_du_cluster -d cassandra:latest
$ docker run -it --link nom_du_cluster:cassandra --rm cassandra sh -c 'exec cqlsh "$CASSANDRA_PORT_9042_TCP_ADDR"'
```
## Partie 3 : Calcul des indicateurs 
* J'ai créé la table Indicateurs avec les champs Sexe, Nombre et moyenAge
* J'ai eu des problèmes pour manipuler les dates et calculer l’âge étant donné que j'ai la date de naissance, donc normalement je dois faire la différence entre la date d'aujourd'hui et la date de naissance et ensuite calculer la moyenne avec la fonction prédéfinie AVG. 
## Partie 4: Développement d'une api permettant d’exposer les indicateurs
* pour retourner du json, j'ai ajouter le paramétre json dans la requête CQL et par suite le retour de cette requête est converti directement en json
