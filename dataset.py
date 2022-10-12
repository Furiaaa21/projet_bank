import streamlit as st
import pandas as pd
import numpy as np

title = "Dataset"
sidebar_name = "Dataset"

df=pd.read_csv('bank-additional-full.csv',sep=';')   

def run():

    st.title(title)
    
    st.dataframe(df.head())
    st.markdown("""
    * Langage utilisée : **Python**
    * Librairies utilisées : **Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn**
    """)
        
    st.header('Définition des variables qualitatives')

    st.markdown(
        """
        * **‘job’** : Type d'emploi du client
        * **‘marital’** : Statut marital du client
        * **‘education’** : Niveau d'études du client
        * **‘default’** : Statut en cours du crédit client
        * **‘housing’** : Prêt Immobilier en cours
        * **‘loan’** : Prêt Personnel en cours
        * **‘contact’** : Type de communication du contact
        * **‘day_of_week’** : Jour de la dernière prise de contact client
        * **‘month’** : Mois de la dernière prise de contact client
        * **‘poutcome’** : Résultat de la précédente campagne marketing 
        * **‘y’** : Le client a souscrit à un compte dépôt à terme? _VARIABLE CIBLE_
        """
    )
    
    st.header('Définition des variables quantitatives')

    st.markdown(
        """
        * **'age'** : Age du client 
        * **‘duration’** : Durée du dernier contact (en secondes)
        * **‘campaign’** : Nombre de contacts effectués au cours de cette campagne et pour ce client (inclut le dernier contact)
        * **‘pdays’** : Nombre de jours qui se sont écoulés depuis que le client a été contacté pour la dernière fois lors d'une campagne précédente
        * **‘previous’** : Nombre de contacts effectués avant cette campagne et pour ce client
        * **‘emp.var.rate’** : Taux de variation de l'emploi - indicateur trimestriel
        * **‘cons.price.idx’** : Indice des prix à la consommation - indicateur mensuel
        * **‘cons.conf.idx’** : Indice de confiance des consommateurs - indicateur mensuel
        * **‘euribor3m’** : Taux euribor 3 mois - indicateur journalier (*)
        * **‘nr.employed’** : Nombre de salariés — indicateur trimestriel
        """
    )
    st.caption('(*) Le taux Euribor à 3 mois est le taux d’intérêts auquel une sélection de banques européennes s’accordent mutuellement des prêts en euros, les prêts ayant alors une durée de 3 mois.')
    st.markdown("---")
    st.header('Exploration des données')
    
    st.write('* Le nombre de lignes du dataset est de :',df.shape[0] )
    st.write('* Le nombre de colonnes du dataset est de :',df.shape[1] )
    st.write('* Pas de valeurs manquantes dites _NaN_')

    if st.checkbox("Afficher plus d'informations"):
        st.write(df.describe())