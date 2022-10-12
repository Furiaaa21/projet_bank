import streamlit as st
import pandas as pd
import numpy as np


title = "Conclusion"
sidebar_name = "Conclusion"


def run():

    st.title(title)

    st.markdown(
        """

- Les résultats obtenus sont crédibles pour le domaine bancaire et apportent des connaissances précieuses au gestionnaire de campagne de télémarketing. Nous avons eu de bons résultats avec certains modèles et avons ciblé les caractéristiques et/ou attributs susceptibles d'améliorer le résultat.

- L'utilisation des modèles de Machine Learning pour prédire le résultat d'un appel téléphonique de télémarketing pour vendre des dépôts à long terme, est un précieux outil d'aide à la décision de sélection des clients et permet économiser du temps et de l’argent.

- Une meilleure compréhension de l’audience est essentielle. Pour renforcer les modèles rajouter des attributs tels que la géographie, le revenu, l'indicatif régional, ainsi que l'expérience des agents de télémarketing et une trace de leur travail via un ID/historique, le comportement antérieur des clients ou le profil client établie par la banque.
- L'entreprise pourrait accorder un temps précieux et de l'importance à une clientèle ciblée, affectant positivement son activité. Le recours à un tel outil pourrait entraîner d'énormes économies de temps et d'argent pour l'institution concernée si néanmoins les données pour entraîner les modèles de classification étaient plus complètes. C'est pourquoi les institutions ont commencé à accorder une importance croissante à la puissance de l'analyse des données.

        """
    )


