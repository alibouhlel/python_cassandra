from cassandra.cluster import Cluster

#adresse ip du cluster qui dans mon cas celle du docker
cluster = Cluster(['172.17.0.2'])
"creation de la session"
session = cluster.connect()

KEYSPACE = "test-technique"
session.set_keyspace(KEYSPACE)

#creation de la table Indicateurs
session.execute("""
        CREATE TABLE Indicateurs (
            Sexe text,
            Nombre int,
            AgeMoyen double,
            PRIMARY KEY (Sexe)
        )
        """)

#calcul nombre total des femmes
nombreFemmes= session.execute("SELECT count(Sexe) FROM Clients WHERE Sexe='F' ALLOW FILTERING;")[0]

#calcul age moyen des femmes
ageMoyenFemmes= session.execute("SELECT avg(toUnixTimestamp(Date_naissance)) FROM Clients WHERE Sexe='F' ALLOW FILTERING;")[0]

#calcul nombre totale des hommes
nombreHommes= session.execute("SELECT count(Sexe) FROM Clients WHERE Sexe='H' ALLOW FILTERING;")[0]

#calcul age moyen des hommes
ageMoyenHommes= session.execute("SELECT avg(toUnixTimestamp(Date_naissance)) FROM Clients WHERE Sexe='H' ALLOW FILTERING;")[0]

#preparation de la requete d insertion
query = "INSERT INTO Indicateurs(Sexe,Nombre,AgeMoyen) VALUES (?,?,?)"
prepared = session.prepare(query)

#Ajout des resultats d analyse des femmes dans la table
session.execute(prepared, ('F',nombreFemmes[0],ageMoyenFemmes[0]))

#Ajout des resultats d analyse des hommes dans la table
session.execute(prepared, ('H',nombreHommes[0],ageMoyenHommes[0]))

#affichage de la table Indicateurs
rows = session.execute('SELECT Sexe, Nombre, AgeMoyen  FROM Indicateurs')
for row in rows:
    print (row)



