from flask import Flask
from flask import jsonify

from cassandra.cluster import Cluster

#adresse ip du cluster qui dans mon cas celle du docker
cluster = Cluster(['172.17.0.2'])
#creation de la session
session = cluster.connect()

KEYSPACE = "testtechnique"
#ajout du keyspace à la session
session.set_keyspace(KEYSPACE)

app = Flask(__name__)

@app.route("/kpis")
def kpis():
    rows = session.execute('SELECT json Sexe, Nombre, AgeMoyen  FROM Indicateurs ')
    lst = []
    for row in rows:
        print(row[0])
        lst.append(row[0])
    return jsonify(lst)


@app.route("/clients")
def clients():
    rows = session.execute('SELECT json Nom, Prenom, Adresse, Sexe, Email, Date_naissance  FROM Clients limit 500')
    lst = []
    for row in rows:
        print(row[0])
        lst.append(row[0])
    return jsonify(lst)


@app.route("/version")
def version():
    return jsonify({"version": "1.0"})



if __name__ == '__main__':
    app.run()
