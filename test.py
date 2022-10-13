import streamlit as st
import pandas as pd
from joblib import dump, load
from sklearn.preprocessing import LabelEncoder,StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report,accuracy_score,f1_score

title = "Test de prédiction"
sidebar_name = "Test de prédiction"

    
def prediction(AGE,JOB, MARITAL, EDUCATION,HOUSING, LOAN,DEFAULT,DAY_OF_WEEK,MONTH,CONTACT):   
    df=pd.read_csv('bank-additional-full.csv',sep=';')
    df=df[['age','job','marital','education','housing','loan','default','day_of_week','month','contact','y']]
  
    for col in df.columns:
            df[col]=df[col].replace(['unknown'],[df[col].mode()[0]])
            
          
    
    df['contact']=df['contact'].replace(["telephone","cellular"],[0,1])      
    df['education']=df['education'].replace(["university.degree", "high.school","professional.course","basic.9y","basic.6y","basic.4y","illiterate"],[0,1,2,3,4,5,6])
    df['job']=df['job'].replace(["admin.", "blue-collar","technician","services","management","entrepreneur","self-employed","housemaid","unemployed", "student","retired"],[0,1,2,3,4,5,6,7,8,9,10])
    df['marital']=df['marital'].replace(["single", "married","divorced"],[0,1,2])
    df['housing']=df['housing'].replace(["no","yes"],[0,1])
    df['loan']=df['loan'].replace(["no","yes"],[0,1])
    df['default']=df['default'].replace(["no","yes"],[0,1])
    df['day_of_week']=df['day_of_week'].replace(["fri","mon","thu","tue","wed"],[0,1,2,3,4])
    df['month']=df['month'].replace(["apr","aug","dec","jul","jun","mar","may","nov","oct","sep"],[0,1,2,3,4,5,6,7,8,9])
    df['y']=df['y'].replace(["no","yes"],[0,1])
    
    #st.dataframe(df)  

    Y=df['y']
    X=df.drop('y',1)
    
    X_train, X_test, y_train, y_test= train_test_split(X,Y,test_size=0.2,random_state=42)
    
    sm=SMOTE()
    X_train,y_train = sm.fit_resample(X_train,y_train)

    gbc=GradientBoostingClassifier(learning_rate=0.08,n_estimators=180)
    gbc.fit(X_train,y_train)
    
    y_pred = gbc.predict(X_test)
    #st.write("Score Test:", round(accuracy_score(y_test,y_pred)*100,2))
    #st.write("Score F1:",round(f1_score(y_test, y_pred)*100,2))
    #st.dataframe(X_test)
    #st.dataframe(y_pred)
    
    # Pre-processing user input    
    if JOB == "admin.":
        JOB = 0
    elif JOB=="blue-collar":
        JOB = 1
    elif JOB == "technician":
        JOB = 2
    elif JOB=="services":
        JOB = 3
    elif JOB == "management":
        JOB = 4
    elif JOB=="entrepreneur":
        JOB = 5
    elif JOB == "self-employed":
        JOB = 6
    elif JOB=="housemaid":
        JOB = 7
    elif JOB == "unemployed":
        JOB = 8
    elif JOB=="student":
        JOB = 9
    else:
        JOB==10
   
 
    if MARITAL == "single":
        MARITAL = 0
    elif MARITAL == "married":
        MARITAL = 1
    else:
        MARITAL = 2

    if EDUCATION == "university.degree":
        EDUCATION = 0
    elif EDUCATION == "high.school":
        EDUCATION = 1
    elif EDUCATION == "professional.course":
        EDUCATION = 2
    elif EDUCATION == "basic.9y":
        EDUCATION = 3
    elif EDUCATION == "basic.6y":
        EDUCATION = 4
    elif EDUCATION == "basic.4y":
        EDUCATION = 5
    else:
        EDUCATION = 6
        
    if HOUSING == "no":
        HOUSING = 0
    else:
        HOUSING = 1
    
    if LOAN == "no":
        LOAN = 0
    else:
        LOAN = 1 
    
    if DEFAULT == "no":
        DEFAULT = 0
    else:
        DEFAULT = 1
        
    if DAY_OF_WEEK == "fri":
        DAY_OF_WEEK = 0
    elif DAY_OF_WEEK == "mon":
        DAY_OF_WEEK = 1
    elif DAY_OF_WEEK == "thu":
        DAY_OF_WEEK = 2
    elif DAY_OF_WEEK == "tue":
        DAY_OF_WEEK = 3
    else:
        DAY_OF_WEEK = 4 
    
    if MONTH == "apr":
        MONTH = 0
    elif MONTH=="aug":
        MONTH = 1
    elif MONTH == "dec":
        MONTH = 2
    elif MONTH=="jul":
        MONTH = 3
    elif MONTH == "jun":
        MONTH = 4
    elif MONTH=="mar":
        MONTH = 5
    elif MONTH == "may":
        MONTH = 6
    elif MONTH=="nov":
        MONTH = 7
    elif MONTH == "oct":
        MONTH = 8
    else:
        MONTH==9
    
    if CONTACT == "telephone":
        CONTACT = 0
    else:
        CONTACT = 1

 
    # Making predictions 
    
    pred = gbc.predict( 
        [[AGE,JOB, MARITAL, EDUCATION, HOUSING, LOAN,DEFAULT,DAY_OF_WEEK,MONTH,CONTACT]])
    
    if pred == 0:
        pred_text = 'Client susceptible de ne pas souscrire au compte '
        st.error('Résultat: {}'.format(pred_text))
        st.info("**Testez le client avec les données suivantes :** '33','blue-collar','married','basic.9y','no','no','no','fri','may','cellular'")
    else:
        pred_text = 'Client à Contacter en priorité, client susceptible de souscrire au compte'
        st.success('Résultat: {}'.format(pred_text))
    return


def run():

    st.title(title)
    st.header("_Dans la peau d'un télémarketeur_")
    
    df=pd.read_csv('bank-additional-full.csv',sep=';')
    df=df[['age','job','marital','education','housing','loan','default','day_of_week','month','contact','y']]
    for col in ['age','job','marital','education','housing','loan','default','day_of_week','month','contact']:
            df[col]=df[col].replace(['unknown'],[df[col].mode()[0]])
        
    #st.dataframe(df)
        
    st.markdown(""" **Objectif :**""") 
    st.markdown("A partir des données d'un client, savoir si le modèle prédit son adhésion au compte à termes. Si oui, le test demandera au télémarketeur de contacter ce client.")
    st.markdown("**Merci de rentrer les données du client**")
    
    x_age=st.slider("Quel est l'age du client :", min_value=17, max_value=98)
    x_job=st.selectbox("Type d'emploi du client :", df.job.unique())
    x_marital=st.selectbox("Statut marital du client :", df.marital.unique())
    x_education=st.selectbox("Niveau d'études du client :", df.education.unique())
    x_housing=st.selectbox("Le client a t-il un pret immobilier ? :", df.housing.unique())
    x_loan=st.selectbox("Le client a t-il un pret personnel ? :", df.loan.unique())
    x_default=st.selectbox("Défault de paiement ? :",df.default.unique())
    x_day_of_week=st.selectbox("Jour de la semaine :",df.day_of_week.unique())
    x_month=st.selectbox("Mois de l'année :",df.month.unique())
    x_contact=st.selectbox("Type de contact :",df.contact.unique())
    
    if st.button("Lancer Résultat"):
        prediction(x_age,x_job,x_marital,x_education,x_housing,x_loan,x_default,x_day_of_week,x_month,x_contact)
       

    

