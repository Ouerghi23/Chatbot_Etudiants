import pandas as pd
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Charger la clé
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Charger le dataset
df = pd.read_csv("student-mat.csv", sep=';')

# Créer le chatbot agent
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=api_key)
agent = create_pandas_dataframe_agent(llm, df, verbose=False, allow_dangerous_code=True)

# Configuration de la page
st.set_page_config(page_title="Chatbot Étudiant", layout="wide")
st.title("🎓 Chatbot Analyse Étudiants")

# Message de bienvenue
st.markdown("👋 **Bienvenue !** Je suis votre assistant pour explorer le fichier `student-mat.csv`.")
st.markdown(" Posez-moi des questions !")

# Zone de saisie utilisateur (Chatbot)
query = st.text_input("💬 Votre question")
if query:
    message = query.strip().lower()
    
    if message in ['bonjour', 'hello', 'hi', 'salut']:
        st.warning("👋 Bonjour ! Comment puis-je vous aider ?")
    
    elif message in ['exit', 'quitter', 'bye', 'au revoir']:
        st.warning("👋 Merci pour votre visite. À bientôt !")
    
    else:
        with st.spinner(" Traitement en cours..."):
            try:
                result = agent.run(query)
                st.success(result)
            except Exception as e:
                st.error(f" Erreur : {e}")


# Séparation visuelle
st.markdown("---")

# SECTION VISUALISATION
st.subheader("Visualisation des données")

# Histogramme simple
colonne = st.selectbox(" Choisis une colonne numérique à visualiser :", 
                       options=["G1", "G2", "G3", "absences", "age", "health", "studytime", "goout", "Dalc", "Walc"])

if colonne:
    fig1, ax1 = plt.subplots()
    sns.histplot(df[colonne], kde=True, color="skyblue", ax=ax1)
    ax1.set_title(f"Distribution de {colonne}")
    st.pyplot(fig1)

# Boxplot comparatif par sexe
st.subheader("Comparaison des élèves par sexe")
selected_feature = st.selectbox("Quelle variable comparer selon le sexe ?", ["G1", "G2", "G3", "absences", "studytime"])
fig2, ax2 = plt.subplots()
sns.boxplot(x="sex", y=selected_feature, data=df, ax=ax2, palette="pastel")
ax2.set_title(f"{selected_feature} selon le sexe")
st.pyplot(fig2)
