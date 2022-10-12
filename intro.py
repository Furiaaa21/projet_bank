import streamlit as st
import pandas as pd

title = "Prédiction du succès d’une campagne de Marketing d’une banque"
sidebar_name = "Bank Marketing"


def run():

    # TODO: choose between one of these GIFs
    st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/2.gif")
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif")

    st.title(title)

    st.markdown("---")

    st.markdown(
        """
        L’analyse des données marketing est une problématique très classique des sciences des données appliquées dans les entreprises de service. Pour ce jeu de données, nous avons des données personnelles sur des clients d’une banque qui ont été “télémarketés” pour souscrire à un produit que l’on appelle un "dépôt à terme”. Lorsqu’un client souscrit à ce produit, il place une quantité d’argent dans un compte spécifique et ne pourra pas toucher ses fonds avant l’expiration du terme. En échange, le client reçoit des intérêts de la part de la banque à la fin du terme.
        """)
    st.markdown("""**Objectifs** :
- Effectuer de l'exploration de données, du nettoyage des données, de l'extraction des fonctionnalités, de la gestion du déséquilibre des classes et du développement d'un algorithme d'apprentissage automatique robuste pour prédire quels clients potentiels souscriront au dépôt à terme
- Réaliser une analyse visuelle et statistique des facteurs pouvant expliquer le lien entre les données personnelles du client (âge, statut marital, quantité d’argent placé dans la banque, nombre de fois que le client a été contacté, etc.) et la variable cible “Est-ce que le client a souscrit au dépôt à terme ?”.
- Utiliser des techniques d'apprentissage automatique, pour tenter de déterminer à l’avance si un client va souscrire au produit ou non.
- Application des données d'un client dans un test de prédiction, permettant de guider le télémarketeur.
- Etudier l'importance de la Data science dans le domaine bancaire
        """
    )
    df=pd.read_csv('bank-additional-full.csv',sep=';')
    #st.text('Fixed width text')
    #st.caption('Balloons. Hundreds of them...')
    #st.write(['st', 'is <', 3]) # see *
    #st.code('for i in range(8): foo()')
    #st.warning('Warning message')
    #st.info('Info message')
    #st.success('Success message')
    #st.error('Error message')
    #st.button('Hit me')
    #st.checkbox('Check me out')
    #st.radio('Radio', [1,2,3])
    #st.selectbox('Select', [1,2,3])
    #st.multiselect('Multiselect', [1,2,3])
    #st.slider('Slide me', min_value=0, max_value=10)
    #st.select_slider('Slide to select', options=[1,'2'])
    #st.text_input('Enter some text')
    #st.number_input('Enter a number')
    #st.color_picker('Pick a color')
    #st.write("**F1-SCORE**")
 