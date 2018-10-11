import pandas as pd

dataFrame = pd.read_csv('clients.txt', sep="|", header=None)
dataFrame.columns = ["Nom", "Adresse", "Sexe", "Email", "Date_naissance"]


#filter les noms: un nom ne doit pas contenir des chiffres
nomFilter=dataFrame['Nom'].str.contains('^([^0-9]*)$', regex=True, na=False)

#filtrer les dates selon le format aaaa-mm-jj
# et tenir compte des cas particuliers par exemple un 30 Fevrier
dateNaissanceFilter = dataFrame['Date_naissance'].str.contains('(((19|20)([2468][048]|[13579][26]|'
                                                          '0[48])|2000)[/-]02[/-]29|((19|20)'
                                                          '[0-9]{2}[/-](0[4678]|1[02])[/-]'
                                                          '(0[1-9]|[12][0-9]|30)|(19|20)'
                                                          '[0-9]{2}[/-](0[1359]|11)[/-]'
                                                          '(0[1-9]|[12][0-9]|3[01])|(19|20)'
                                                          '[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]'
                                                          '|2[0-8])))', regex=True, na=False)

#filtrage du sexe: H ou F
sexeFilter = dataFrame['Sexe'].str.contains('H|F', regex=True, na=False)

#filtrer si le champ email respecte le format hash sha256:
# longueur 64 avec soit des lettres en miniscules ou bien en majuscules
emailFilter=dataFrame['Email'].str.contains('([a-z\d]{64}|[A-Z\d]{64})', regex=True, na=False)

#filtrage du data frame
filteredDataFrame=dataFrame[nomFilter][sexeFilter][emailFilter][dateNaissanceFilter]

#enregistrement du dataframe filtré dans le nouveau fichier texte
filteredDataFrame.to_csv("clients_clean.txt", header=False, index=None, mode='a', sep='|')
