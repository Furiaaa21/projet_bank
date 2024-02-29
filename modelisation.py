import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.metrics import classification_report,accuracy_score,f1_score,roc_curve
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from imblearn.over_sampling import RandomOverSampler,SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier 
from sklearn.svm import SVC
import warnings
warnings.filterwarnings("ignore")
from joblib import dump, load



title = "Modélisation"
sidebar_name = "Modélisation"

df=pd.read_csv('bank-additional-full.csv',sep=';')

def preprocessing(df):
    #REMPLACER UNKNOWN PAR MODE
    x_unknown=st.selectbox("1/ Souhaitez-vous remplacer les valeurs 'Unknown' par le mode de chaque variable ? :",['Oui','Non'])
    if (x_unknown=='Oui'):
        df=pd.read_csv('bank-additional-full.csv',sep=';')
        for col in df.columns:
            df[col]=df[col].replace(['unknown'],[df[col].mode()[0]])
        st.success("L'observation 'Unknown' a été remplacée")    
        
    if (x_unknown=='Non'):
        df=pd.read_csv('bank-additional-full.csv',sep=';')
        st.info("L'observation 'Unknown' ne sera pas remplacée")
        
    x_extreme=st.selectbox("2/ Souhaitez-vous supprimer les valeurs extremes ? :",['Oui','Non'])    
    if (x_extreme=='Oui'):
        x_extreme_var=st.multiselect("------------- Pour quelles variables souhaitez-vous le faire ?    --------------",['age', 'duration', 'campaign','emp.var.rate',
       'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed'])
        for i in x_extreme_var:
            q1=df[i].quantile(q=0.25)
            q3=df[i].quantile(q=0.75)
            IQR=q3-q1
            borne_inf = q1-1.5*IQR
            borne_sup = q3 +1.5*IQR
            df=df[df[i]<borne_sup]
            df=df[df[i]>borne_inf]
        st.write("*Les nouvelles dimensions du dataset sont:*",df.shape)
        
    if (x_extreme=='Non'):
        st.info("Pas de valeurs extremes à supprimer")
        st.write("*Les nouvelles dimensions du dataset sont:*",df.shape)
        x_extreme_var="Pas de valeurs extremes a supprimer"
        
    #SUPPRESSION DE VARIABLES 
    x_drop=st.multiselect("3/ Choix des variables à supprimer :",df.columns[:20])
    df=df.drop(x_drop, axis=1)
    st.write("*Les nouvelles dimensions du dataset sont:*",df.shape)

    #ENCODAGE VARIABLE CIBLE
    lb = LabelEncoder() 
    df['y'] = lb.fit_transform(df['y'])
    #ENCODAGE VARIABLE CAT
    Y=df['y']
    X=df.drop('y',axis=1)
    
    cat_var= X.select_dtypes(include= ["object"]).columns
    X = pd.get_dummies(X, columns = cat_var)
    
    st.markdown("---")
    st.header("Encodage")
    st.markdown("""
    * Séparation de la variable cible des autres variables
    * Encodage grace à la fonction _get_dummies()_
    """)
    if st.checkbox('Aperçu des données encodées'):
        st.write(X.head())
    st.write("*Les nouvelles dimensions du dataset sont:*",X.shape)
    return X,Y,x_unknown,x_extreme,x_extreme_var,x_drop

def train_test_norm(X,Y):
    X_train, X_test, y_train, y_test= train_test_split(X,Y,test_size=0.2,random_state=42)
    sc = StandardScaler()
    X_train_scaled= sc.fit_transform(X_train)
    X_test_scaled= sc.transform(X_test)
    if st.checkbox('Aperçu des données Test'):
        st.write(X_train_scaled)
    return X_train_scaled,X_test_scaled,y_train, y_test

def ros_smote(X_train_scaled,y_train):
    des=st.selectbox("Choix du modèle de ré-équilibrage :",['Oversampling','SMOTE','None'])
    if (des=='Oversampling'):
        ros=RandomOverSampler()
        X_train_scaled,y_train = ros.fit_resample(X_train_scaled,y_train)
        check1=st.checkbox('Vérification')
        if check1:
            st.bar_chart(pd.Series(y_train).value_counts())
    if (des=='SMOTE'):
        sm=SMOTE()
        X_train_scaled,y_train = sm.fit_resample(X_train_scaled,y_train)
        check2=st.checkbox('Vérification')
        if check2:
            st.bar_chart(pd.Series(y_train).value_counts())
    if (des=='None'):
        st.warning("Pas de ré-équilibrage souhaité")
    return X_train_scaled,y_train,des
        

def classifier(model,X_train_scaled,X_test_scaled,y_train,y_test):
    #ENTRAINEMENT MODELE
    model.fit(X_train_scaled,y_train)
    #PREVISION DONNEES SUR L'ENSEMBLE DU TEST
    y_pred_test = model.predict(X_test_scaled)
    #PREVISION DONNEES SUR L'ENSEMBLE DU TRAIN
    y_pred_train = model.predict(X_train_scaled)
     #F1-SCORE
    f1 = round(f1_score(y_test, y_pred_test)*100,2)
    #ACCURACY
    acc_test = round(accuracy_score(y_test,y_pred_test)*100,2)
    acc_train =  round(accuracy_score(y_train,y_pred_train)*100,2)

    #st.write("**F1-SCORE :**",f1,"     **SCORE TEST :**",acc_test,"**SCORE TRAIN :**",acc_train)
    #st.caption("Résultats obtenus en %")
    st.info('F1-SCORE : {}%'.format(f1))
    st.info('SCORE TEST : {}%'.format(acc_test))
    st.info('SCORE TRAIN : {}%'.format(acc_train))
    return f1,acc_test,acc_train,model


def run():

    st.title("Modélisation")
    st.header("Preprocessing")
    
    X,Y,x_unknown,x_extreme,x_extreme_var,x_drop=preprocessing(df)
    st.markdown("---")
    st.header("Séparation et Normalisation")
    X_train_scaled,X_test_scaled,y_train, y_test=train_test_norm(X,Y)

    
    st.markdown("---")
    st.header("Déséquilibre")
    X_train_scaled,y_train,des=ros_smote(X_train_scaled,y_train)
    
    st.markdown("---")
    st.header("Modélisation")
    #st.markdown("""**Récapitulatif :**""")
    #st.write("* Valeurs 'Unknown' remplacées :",x_unknown.upper())
    #st.write("* Valeurs extremes supprimées :",x_extreme.upper())
    #st.warning(x_extreme_var)
    #st.write("* Variables supprimées :")
    #st.warning(x_drop)
    #st.write("* Modèle de ré-équilibrage choisi :",des)
    
    clf=st.selectbox("Choix du modèle de classification:",['Logistic Regression','KNN','SVC','Decision Tree','Random Forest','Gradient Boosting']) 
    
    if (clf=='Logistic Regression'):
        f1_log,acc_test_log,acc_train_log,model_log=classifier(LogisticRegression(),X_train_scaled,X_test_scaled,y_train,y_test)
    if (clf=='KNN'):
        f1_knn,acc_test_knn,acc_train_knn,model_knn=classifier(KNeighborsClassifier(),X_train_scaled,X_test_scaled,y_train,y_test)
    if (clf=='SVC'):
        f1_svc,acc_test_svc,acc_train_svc,model_svc=classifier(SVC(),X_train_scaled,X_test_scaled,y_train,y_test)   
    if (clf=='Decision Tree'):
        f1_dt,acc_test_dt,acc_train_dt,model_dt=classifier(DecisionTreeClassifier(),X_train_scaled,X_test_scaled,y_train,y_test)
    if (clf=='Random Forest'):
        f1_rfc,acc_test_rfc,acc_train_rfc,model_rfc=classifier(RandomForestClassifier(),X_train_scaled,X_test_scaled,y_train,y_test)
    if (clf=='Gradient Boosting'):
        f1_gbc,acc_test_gbc,acc_train_gbc,model_gbc=classifier(GradientBoostingClassifier(),X_train_scaled,X_test_scaled,y_train,y_test)
        dump(model_gbc, 'gbc_best.joblib')

   
