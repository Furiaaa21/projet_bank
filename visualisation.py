import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns


title = "Visualisation"
sidebar_name = "Visualisation"
df=pd.read_csv('bank-additional-full.csv',sep=';')
df_yes=df[df['y']=='yes']
df_no=df[df['y']=='no']

def plot_var(df):
        x_axis_val=st.selectbox('Choix de la variable :', df.columns)
        st.subheader('*Répartition de la variable* ' + x_axis_val.upper())
        
        #VARIABLES QUALITATIVES
        
        #JOB
        if x_axis_val=='job':
            
            df_job=df[['job']]
            df_job['job_cat']=df_job['job'].replace(["admin.", "blue-collar","technician","services","management","entrepreneur","self-employed","housemaid","unemployed",    "student","retired"],["EMPLOYED","EMPLOYED","EMPLOYED","EMPLOYED","EMPLOYED","EMPLOYED","EMPLOYED","EMPLOYED","UNEMPLOYED","UNEMPLOYED","UNEMPLOYED"])
            st.bar_chart(df_job['job_cat'].value_counts())
            st.write("Le graphique ci-dessus a été obtenu en séparant les clients ayant un emploi de ceux qui n’en n’ont pas. En toute logique, la campagne cible essentiellement **les clients ayant un emploi**.")
            
            st.bar_chart(df[x_axis_val].value_counts())
            st.write("Les personnes occupant un emploi dans l’**administration** ont été davantage contactées par la banque.")
            st.write("A l'inverse, les clients avec des professions libérales/freelance (entrepreneur), sans emploi et les étudiants sont les personnes les moins contactées et souscrivent moins au compte de dépôts. Cela est sans doute lié aux a priori concernant l'instabilité, la précarité et le manque des revenus de ce type de personnes")
            st.subheader('*Souscriptions par catégorie de* '+ x_axis_val.upper())
            
            hist_y=px.histogram(df, x = x_axis_val, color=df['y'],barmode='group',color_discrete_map={'yes':'green', 'no':'blue'})
            st.plotly_chart(hist_y)

            
            
            select_job=st.selectbox('Choix de JOB',df.job.unique())
            pie_job=px.sunburst(df[df['job']==select_job],path=['job','y'],color='y',color_discrete_map={'yes':'green', 'no':'blue'})
            pie_job.update_traces(textinfo="label+percent parent")
            st.plotly_chart(pie_job)
        
        #EDUCATION
        if x_axis_val=='education':
            df_education=df[['education']]
            df_education['education_cat']=df_education['education'].replace(["university.degree", "high.school","professional.course","basic.9y","basic.6y","basic.4y","illiterate"],
                                        ["Etudes universitaires","Etudes secondaires","Etudes secondaires","Etudes secondaires","Etudes primaires/pas d'études","Etudes primaires/pas d'études","Etudes primaires/pas d'études"])
            st.bar_chart(df_education['education_cat'].value_counts())
            st.write("En regroupant les personnes de niveaux d'études similaires, nous observons que le groupe ayant été jusqu'aux études secondaires (lycée, collègue, formation professionnelle), est supérieur en nombre à ceux disposant d’un diplôme universitaire.")
            st.write(" Néanmoins, la catégorie d’études la plus représentée concerne les personnes ayant fait des études à l’université. En revanche, la catégorie 'illiterate', qui correspond à la catégorie des personnes analphabètes, est très peu représentée, seuls 18 clients de cette catégorie ont été contactés. De nouveau la valeur ‘unknown’ apparaît dans ce graphique. Cela signifie que pour quelques clients, le niveau d’études n’a pas été communiqué. Cette valeur représente 4.2% des personnes contactées")
        
            st.subheader('*Souscriptions par catégorie de* '+ x_axis_val.upper())
            
            hist_y=px.histogram(df, x = x_axis_val, color=df['y'],barmode='group',color_discrete_map={'yes':'green', 'no':'blue'})
            st.plotly_chart(hist_y)
            
            select_education=st.selectbox("Choix du niveau d'études",df.education.unique())
            pie_education=px.sunburst(df[df['education']==select_education],path=['education','y'],color='y',color_discrete_map={'yes':'green', 'no':'blue'})
            pie_education.update_traces(textinfo="label+percent parent")
            st.plotly_chart(pie_education)

        #MARITAL   
        if x_axis_val=='marital':
            st.bar_chart(df[x_axis_val].value_counts())
            st.write("Les personnes mariées sont les clients les plus présents au sein de cette campagne. Les clients mariés sont ciblés car leur situation financière est plus stable, la présence de deux personnes au sein du même ménage semble être un facteur favorable pour une éventuelle souscription à un compte à terme.")

            st.subheader('*Souscriptions par catégorie de* '+ x_axis_val.upper())
            
            hist_y=px.histogram(df, x = x_axis_val, color=df['y'],barmode='group',color_discrete_map={'yes':'green', 'no':'blue'})
            st.plotly_chart(hist_y)
            
            st.write("En revanche, même si les clients mariés sont largement les plus contactés, il n'y a pas une si grande différence entre le nombre de clients célibataires et mariés qui vont souscrire un dépôt. Parmi les clients mariés seuls **10.16%** choisissent de contracter un compte dépôt contre **14%** des clients célibataires. Il y a donc également une bonne opportunité de marché chez les clients célibataires.")
            
            select_marital=st.selectbox('Choix de MARITAL',df.marital.unique())
            pie_marital=px.sunburst(df[df['marital']==select_marital],path=['marital','y'],color='y',color_discrete_map={'yes':'green', 'no':'blue'})
            pie_marital.update_traces(textinfo="label+percent parent")
            st.plotly_chart(pie_marital)
            
        #DEFAULT
        if x_axis_val=='default':
            st.bar_chart(df[x_axis_val].value_counts())
            
            st.write("Seules 3 personnes ayant déjà un crédit en défaut de paiement ont été contactées par la banque. Cela semble évident que la banque ne cible pas cette clientèle étant donné que leur situation financière auprès de la banque est déjà critique.")
            
            st.subheader('*Souscriptions par catégorie de* '+ x_axis_val.upper())
            
            hist_y=px.histogram(df, x = x_axis_val, color=df['y'],barmode='group',color_discrete_map={'yes':'green', 'no':'blue'})
            st.plotly_chart(hist_y)
            
            st.write("En raison de ce nombre extrêmement faible d'observations « yes », remplacer « unknown » par le mode() reviendrait à le remplacer par l'observation « no ». Ce qui reviendrait à avoir pratiquement une seule observation pour une variable, cela peut fortement biaisé notre modèle.")
            
            select_default=st.selectbox('Choix de DEFAULT',df.default.unique())
            pie_default=px.sunburst(df[df['default']==select_default],path=['default','y'],color='y',color_discrete_map={'yes':'green', 'no':'blue'})
            pie_default.update_traces(textinfo="label+percent parent")
            st.plotly_chart(pie_default)
            
        #HOUSING
        if x_axis_val=='housing':
            st.bar_chart(df[x_axis_val].value_counts())
            st.subheader('*Souscriptions par catégorie de* '+ x_axis_val.upper())
            
            hist_y=px.histogram(df, x = x_axis_val, color=df['y'],barmode='group',color_discrete_map={'yes':'green', 'no':'blue'})
            st.plotly_chart(hist_y)
            
            st.write("Opportunité à explorer dans le segment clients qui n'ont pas de crédits immobilier.")
            
            select_housing=st.selectbox('Choix de HOUSING',df.housing.unique())
            pie_housing=px.sunburst(df[df['housing']==select_housing],path=['housing','y'],color='y',color_discrete_map={'yes':'green', 'no':'blue'})
            pie_housing.update_traces(textinfo="label+percent parent")
            st.plotly_chart(pie_housing)
            
        #LOAN
        if x_axis_val=='loan':
            st.bar_chart(df[x_axis_val].value_counts())
            st.subheader('*Souscriptions par catégorie de* '+ x_axis_val.upper())
            
            hist_y=px.histogram(df, x = x_axis_val, color=df['y'],barmode='group',color_discrete_map={'yes':'green', 'no':'blue'})
            st.plotly_chart(hist_y)
            
            st.write("La campagne va se concentrer sur les clients n’ayant pas de prêt personnel auprès de la banque, ce sont des clients qui ont les ressources financières nécessaires pour pouvoir accéder à un compte à terme.")
            
            select_loan=st.selectbox('Choix de LOAN',df.loan.unique())
            pie_loan=px.sunburst(df[df['loan']==select_loan],path=['loan','y'],color='y',color_discrete_map={'yes':'green', 'no':'blue'})
            pie_loan.update_traces(textinfo="label+percent parent")
            st.plotly_chart(pie_loan)
            
        #CONTACT
        if x_axis_val=='contact':
            st.bar_chart(df[x_axis_val].value_counts())
            st.subheader('*Souscriptions par catégorie de* '+ x_axis_val.upper())
            
            hist_y=px.histogram(df, x = x_axis_val, color=df['y'],barmode='group',color_discrete_map={'yes':'green', 'no':'blue'})
            st.plotly_chart(hist_y)
            
            st.write("La plupart des clients sont plus contactés par téléphone mobile que par téléphone fixe. De nos jours, la grande majorité des gens possèdent un téléphone portable et utilisent de moins en moins leur téléphone fixe. Les résultats semblent donc cohérents car les clients sont plus joignables par téléphone mobile.")
            
            select_contact=st.selectbox('Choix de CONTACT',df.contact.unique())
            pie_contact=px.sunburst(df[df['contact']==select_contact],path=['contact','y'],color='y',color_discrete_map={'yes':'green', 'no':'blue'})
            pie_contact.update_traces(textinfo="label+percent parent")
            st.plotly_chart(pie_contact)
            
            
        #DAY_OF_WEEK
        if x_axis_val=='day_of_week':
            st.bar_chart(df[x_axis_val].value_counts())
            st.subheader('*Souscriptions par catégorie de* '+ x_axis_val.upper())
            
            hist_y=px.histogram(df, x = x_axis_val, color=df['y'],barmode='group',color_discrete_map={'yes':'green', 'no':'blue'})
            st.plotly_chart(hist_y)
            
            select_day_of_week=st.selectbox('Choix de DAY_OF_WEEK',df.day_of_week.unique())
            pie_day_of_week=px.sunburst(df[df['day_of_week']==select_day_of_week],path=['day_of_week','y'],color='y',color_discrete_map={'yes':'green', 'no':'blue'})
            pie_day_of_week.update_traces(textinfo="label+percent parent")
            st.plotly_chart(pie_day_of_week)
            
        #POUTCOME
        if x_axis_val=='poutcome':
            st.bar_chart(df[x_axis_val].value_counts())

            
            st.subheader('*Souscriptions par catégorie de* '+ x_axis_val.upper())
            
            hist_y=px.histogram(df, x = x_axis_val, color=df['y'],barmode='group',color_discrete_map={'yes':'green', 'no':'blue'})
            st.plotly_chart(hist_y)
            
            select_poutcome=st.selectbox('Choix de POUTCOME',df.poutcome.unique())
            pie_poutcome=px.sunburst(df[df['poutcome']==select_poutcome],path=['poutcome','y'],color='y',color_discrete_map={'yes':'green', 'no':'blue'})
            pie_poutcome.update_traces(textinfo="label+percent parent")
            st.plotly_chart(pie_poutcome)
        
        #MONTH
        if x_axis_val=='month':
            st.bar_chart(df[x_axis_val].value_counts())
                      
            st.write("La campagne de télémarketing va de mars à décembre. Le mois de décembre est le mois où les clients ont moins été contactés. En effet, cela nous laisse à penser qu’étant donné qu’il s’agit de périodes de festivités ( Vacances, Noël, épiphanie), les clients sont moins joignables. Puis c’est une des périodes de l’année où les personnes dépensent le plus pour ces festivités, donc par conséquent la banque a moins de chances d’obtenir des nouvelles inscriptions au compte à terme.")
            
            st.subheader('*Souscriptions par catégorie de* '+ x_axis_val.upper())
            
            hist_y=px.histogram(df, x = x_axis_val, color=df['y'],barmode='group',color_discrete_map={'yes':'green', 'no':'blue'})
            st.plotly_chart(hist_y)
            
            select_month=st.selectbox('Choix de MONTH',df.month.unique())
            pie_may=px.sunburst(df[df['month']==select_month],path=['month','y'],color='y',color_discrete_map={'yes':'green', 'no':'blue'})
            pie_may.update_traces(textinfo="label+percent parent")
            st.plotly_chart(pie_may)
            
            st.write("Appeler plus de clients ne mène pas forcément un bon taux de conversion comme on peut le voir par exemple pour le mois de mai. En effet, seuls **6.5%** des clients contactés en mai ont souscrit au compte.")
            
            
        
        #VARIABLE QUANTITATIVES
        #AGE
        if x_axis_val=='age':
            #df_cat_age=df[['age']]
            ##df_cat_age['cat_age']=pd.cut(df[x_axis_val],bins=9)
            #st.bar_chart(df_cat_age['cat_age'].value_counts());
    
            #BAR_CHART
            st.bar_chart(df[x_axis_val].value_counts()) 
            
            st.write("Baisse conséquente à partir de 60 ans car il y a peu de personnes contactées **entre 60 et 95 ans** dans le jeu de données.")
        
            #BOXPLOT
            box=px.box(df[x_axis_val])
            st.plotly_chart(box)
            st.write("L’ âge médian des clients de la banque est d'environ **38 ans**. La plupart des clients contactés ont entre **32 et 47 ans**.")
        
            #DISPLOT
            hist_data = [df_yes[x_axis_val],df_no[x_axis_val]]
            group_labels = ['Clients souscrit','Clients non souscrit']
            colors=['green','blue']
            fig = ff.create_distplot(hist_data, group_labels,colors=colors)
            fig.update_layout(title_text='DISTRIBUTION VARIABLE AGE / VARIABLE CIBLE')
            st.plotly_chart(fig)
            
        #DURATION
        if x_axis_val=='duration':
    
            #BAR_CHART
            st.bar_chart(df[x_axis_val].value_counts()) 
        
            #BOXPLOT
            box=px.box(df[x_axis_val])
            st.plotly_chart(box)
            st.write("Présence de valeurs extrêmes à partir d’une durée autour de **700** secondes.")
        
            #DISPLOT
            hist_data = [df_yes[x_axis_val],df_no[x_axis_val]]
            group_labels = ['Clients souscrit','Clients non souscrit']
            colors=['green','blue']
            fig = ff.create_distplot(hist_data, group_labels,colors=colors)
            fig.update_layout(title_text='DISTRIBUTION VARIABLE DURATION / VARIABLE CIBLE')
            st.plotly_chart(fig)

        #CAMPAIGN
        if x_axis_val=='campaign':
    
            #BAR_CHART
            st.bar_chart(df[x_axis_val].value_counts()) 
            
            st.write("La majorité des clients ont été contactés entre 1 et 2 fois. Puis quelques personnes ont été contactées entre 10 et plus de 50 fois au cours d’une seule et même campagne.")
        
            #BOXPLOT
            box=px.box(df[x_axis_val])
            st.plotly_chart(box)
            st.write("")
            
            st.write("Présence de valeurs extremes.")
        
            #DISPLOT
            hist_data = [df_yes[x_axis_val],df_no[x_axis_val]]
            group_labels = ['Clients souscrit','Clients non souscrit']
            colors=['green','blue']
            fig = ff.create_distplot(hist_data, group_labels,colors=colors)
            fig.update_layout(title_text='DISTRIBUTION VARIABLE CAMPAIGN / VARIABLE CIBLE')
            st.plotly_chart(fig)
        #PDAYS
        if x_axis_val=='pdays':
    
            #BAR_CHART
            st.bar_chart(df[x_axis_val].value_counts()) 
        
            #BOXPLOT
            box=px.box(df[x_axis_val])
            st.plotly_chart(box)
            st.write("La valeur '999' signifie que le client n'a pas été contacté auparavant. En observant le displot, nous pouvons en déduire que la majorité des clients ont été contactés pour la première fois lors de cette campagne. La valeur '999' appliquée pour ces clients, n’est pas vraiment bien choisie.")
        
            #DISPLOT
            hist_data = [df_yes[x_axis_val],df_no[x_axis_val]]
            group_labels = ['Clients souscrit','Clients non souscrit']
            colors=['green','blue']
            fig = ff.create_distplot(hist_data, group_labels,colors=colors)
            fig.update_layout(title_text='DISTRIBUTION VARIABLE PDAYS / VARIABLE CIBLE')
            st.plotly_chart(fig)
            
        #PREVIOUS
        if x_axis_val=='previous':
    
            #BAR_CHART
            st.bar_chart(df[x_axis_val].value_counts()) 
        
            #BOXPLOT
            box=px.box(df[x_axis_val])
            st.plotly_chart(box)
            st.write("Lors d’une nouvelle campagne, les télémarketeurs privilégient de contacter des clients jamais contactés dans les précédentes campagnes, cela représente 86% des clients contactés ici.")
        
            #DISPLOT
            hist_data = [df_yes[x_axis_val],df_no[x_axis_val]]
            group_labels = ['Clients souscrit','Clients non souscrit']
            colors=['green','blue']
            fig = ff.create_distplot(hist_data, group_labels,colors=colors)
            fig.update_layout(title_text='DISTRIBUTION VARIABLE PREVIOUS / VARIABLE CIBLE')
            st.plotly_chart(fig)
            
        #EMP.VAR.RATE
        if x_axis_val=='emp.var.rate':
    
            #BAR_CHART
            st.bar_chart(df[x_axis_val].value_counts()) 
        
            #BOXPLOT
            box=px.box(df[x_axis_val])
            st.plotly_chart(box)
        
            #DISPLOT
            hist_data = [df_yes[x_axis_val],df_no[x_axis_val]]
            group_labels = ['Clients souscrit','Clients non souscrit']
            colors=['green','blue']
            fig = ff.create_distplot(hist_data, group_labels,colors=colors)
            fig.update_layout(title_text='DISTRIBUTION VARIABLE EMP.VAR.RATE / VARIABLE CIBLE')
            st.plotly_chart(fig)
            
        #CONS.PRICE.IDX
        if x_axis_val=='cons.price.idx':
    
            #BAR_CHART
            st.bar_chart(df[x_axis_val].value_counts()) 
        
            #BOXPLOT
            box=px.box(df[x_axis_val])
            st.plotly_chart(box)
        
            #DISPLOT
            hist_data = [df_yes[x_axis_val],df_no[x_axis_val]]
            group_labels = ['Clients souscrit','Clients non souscrit']
            colors=['green','blue']
            fig = ff.create_distplot(hist_data, group_labels,colors=colors)
            fig.update_layout(title_text='DISTRIBUTION VARIABLE CONS.PRICE.IDX / VARIABLE CIBLE')
            st.plotly_chart(fig)
            
        #CONS.CONF.IDX
        if x_axis_val=='cons.conf.idx':
    
            #BAR_CHART
            st.bar_chart(df[x_axis_val].value_counts()) 
        
            #BOXPLOT
            box=px.box(df[x_axis_val])
            st.plotly_chart(box)
        
            #DISPLOT
            hist_data = [df_yes[x_axis_val],df_no[x_axis_val]]
            group_labels = ['Clients souscrit','Clients non souscrit']
            colors=['green','blue']
            fig = ff.create_distplot(hist_data, group_labels,colors=colors)
            fig.update_layout(title_text='DISTRIBUTION VARIABLE CONS.CONF.IDX / VARIABLE CIBLE')
            st.plotly_chart(fig)
            
        #EURIBOR3M
        if x_axis_val=='euribor3m':
    
            #BAR_CHART
            st.bar_chart(df[x_axis_val].value_counts()) 
        
            #BOXPLOT
            box=px.box(df[x_axis_val])
            st.plotly_chart(box)
        
            #DISPLOT
            hist_data = [df_yes[x_axis_val],df_no[x_axis_val]]
            group_labels = ['Clients souscrit','Clients non souscrit']
            colors=['green','blue']
            fig = ff.create_distplot(hist_data, group_labels,colors=colors)
            fig.update_layout(title_text='DISTRIBUTION VARIABLE EURIBOR3M / VARIABLE CIBLE')
            st.plotly_chart(fig)
            
        #NR.EMPLOYED
        if x_axis_val=='nr.employed':
    
            #BAR_CHART
            st.bar_chart(df[x_axis_val].value_counts()) 
        
            #BOXPLOT
            box=px.box(df[x_axis_val])
            st.plotly_chart(box)
        
            #DISPLOT
            hist_data = [df_yes[x_axis_val],df_no[x_axis_val]]
            group_labels = ['Clients souscrit','Clients non souscrit']
            colors=['green','blue']
            fig = ff.create_distplot(hist_data, group_labels,colors=colors)
            fig.update_layout(title_text='DISTRIBUTION VARIABLE NR.EMPLOYED / VARIABLE CIBLE')
            st.plotly_chart(fig)

def run():

    st.title(title)
    
    st.header('_Variable Cible_')  
    st.markdown("---")    
        
    pie_y=px.sunburst(df,path=['y'],title='Les clients ont t-il contracté un compte à termes?',color='y',color_discrete_map={'yes':'green','no':'blue'})
    pie_y.update_traces(textinfo="label+percent parent")
    st.plotly_chart(pie_y)
   
    st.markdown("Nous pouvons voir sur le graphique une **forte disparité** entre les deux classes. Nous sommes sur un jeu de données de classification binaire. La distribution de classe indique un ensemble de **données déséquilibrées**. **89%** des clients n'ont pas souscrit à un compte à termes contre **11%** de clients qui l’ont souscrit.")
    
    st.markdown("---")

    plot_var(df)
    
    st.header('_Heatmap_')
    fig= plt.figure(figsize=(10,7))
    heatmap=sns.heatmap(df.corr(method='pearson'), annot=True,cmap='coolwarm')
    st.write(fig)
    st.write("Les variables _emp.var.rate_, _cons.price.index_, _euribor3m_ et _nr.employed_ ont une corrélation très élevée entre elles. Avec _euribor3m_ et _nr.employed_ qui sont les variables ayant la corrélation la plus élevée: **0,97** .")
    st.write("En revanche, ces mêmes variables sont corrélés négativement par rapport à la variable cible.")
    
    st.markdown("---")
    st.header('Observations')
    st.markdown("""
    * Un grand nombre de clients sont mariés
    * La majorité des clients n'ont pas de crédit en défaut de paiement
    * Beaucoup de clients ont un prêt au logement, mais très peu ont des prêts personnels
    * Les téléphones portables semblent être la méthode privilégiée pour joindre les clients
    * Nombre important d'appels ne garantit pas un nombre élevé de souscriptions (exemple du mois de mai)
    * Variable cible déséquilibrée
    * Présence de la valeur “Unknown” ( _job, marital, education, default, housing, loan_)
    * Présence de valeurs extrêmes ( _duration et campaign_ )
    * Décision de supprimer certain variables ( _default,  pdays, previous_)
    * Variables fortement corrélées (_emp.var.rate, cons.price.index, euribor3m et nr.employed_)
        """)
    
    st.markdown("""**Remarque** :
Nous n’avons pas de données géographiques ni temporelles, à savoir, dans quel pays a eu lieu la campagne de télémarketing et en quelle année. L'heure de l'appel est également manquant car il peut etre un facteur déterminant. Toutes ces données permettraient d'affiner l’analyse du comportement des clients.
""")
   
