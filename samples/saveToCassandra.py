from cassandra.cluster import Cluster
import pandas as pd

#declaration du keyspace
KEYSPACE = "testtechnique"

#adresse ip du cluster qui dans mon cas celle du docker
cluster = Cluster(['172.17.0.2'])
#creation de la session
session = cluster.connect()


#creation du keyspace testtechnique
session.execute("""
        CREATE KEYSPACE %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
       """ % KEYSPACE)

#on ajoute le keyspace a la session
session.set_keyspace(KEYSPACE)

#chargement du fichier client_clean dans une data frame
data = pd.read_csv('clients_clean.txt', sep="|", header=None)
data.columns = ["Nom", "Adresse", "Sexe", "Email", "Date_naissance"]

#creation de la table Clients
session.execute("""
        CREATE TABLE Clients (
            Nom varchar,
            Prenom varchar,
            Adresse text,
            Sexe text,
            Email text,
            Date_naissance date,
            PRIMARY KEY (Email)
        )
        """)

#preparation de la requete d insertion
query = "INSERT INTO Clients(Nom,Prenom,Adresse,Sexe,Email,Date_naissance) VALUES (?,?,?,?,?,?)"
prepared = session.prepare(query)

#parcours du data frame ligne par ligne pour faire le sauvegarde dans la base
for index, row in data.iterrows():
    nomComplet=row[0].split(' ')
    session.execute(prepared, (nomComplet[0],nomComplet[1],row[1],row[2],row[3],row[4]))

#affichage du contenu de la table Clients
rows = session.execute('SELECT Nom, Prenom, Adresse, Sexe, Email, Date_naissance  FROM Clients')
for row in rows:
    print (row)

