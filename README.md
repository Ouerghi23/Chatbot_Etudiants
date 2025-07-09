## 🤖 Chatbot Étudiant

Un projet Streamlit + LangChain + OpenAI qui permet d'analyser un dataset `.csv` d'élèves avec un chatbot intelligent et des visualisations interactives.

## 🎯 Objectif

- Poser des questions naturelles sur le fichier `student-mat.csv`
- Visualiser les notes, absences, santé, etc. sous forme de graphiques interactifs
- Analyser les performances des étudiants grâce à l'intelligence artificielle

## 🛠️ Tech Stack

- **Python** - Langage principal
- **Streamlit** - Interface utilisateur web
- **LangChain** - Framework pour applications LLM
- **OpenAI** - API d'intelligence artificielle
- **Pandas** - Manipulation des données
- **Seaborn** - Visualisations statistiques

## ⚙️ Installation

### 1. Cloner le repository
```bash
git clone https://github.com/Ouerghi23/Chatbot_Etudiants.git
cd Chatbot_Etudiants
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configuration de l'environnement
Créer un fichier `.env` à la racine du projet :
```env
OPENAI_API_KEY=votre_cle_api_openai
```

### 4. Lancer l'application
```bash
streamlit run chatbot.py
```

## 📊 Fonctionnalités

- **💬 Chatbot intelligent** - Connecté aux données CSV pour répondre aux questions
- **📈 Visualisations dynamiques** - Histogrammes et boxplots interactifs
- **🔍 Requêtes en langage naturel** - Exemples : "Quelle est la moyenne des notes ?" ou "Montrez-moi les absences par matière"
- **📱 Interface responsive** - Optimisée pour desktop et mobile

## 📁 Données

- **Dataset** : Student Performance - UCI ML Repository
- **Fichier** : `student-mat.csv` inclus dans ce projet
- **Contenu** : Données sur les performances scolaires des étudiants (notes, absences, informations socio-démographiques)

## 🚀 Utilisation

1. Lancez l'application avec `streamlit run chatbot.py`
2. Téléchargez ou utilisez le fichier `student-mat.csv` fourni
3. Posez des questions sur les données dans le chatbot
4. Explorez les visualisations générées automatiquement

## 📋 Exemples de questions

- "Quelle est la moyenne générale des étudiants ?"
- "Montrez-moi la distribution des notes finales"
- "Y a-t-il une corrélation entre les absences et les notes ?"
- "Quels sont les facteurs qui influencent le plus les performances ?"


## 👨‍💻 Auteur

**Chaima Ouerghi**

---

*Développé avec ❤️ en utilisant Streamlit et OpenAI*
