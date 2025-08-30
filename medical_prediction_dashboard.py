import streamlit as st
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

def load_glioma_models():
    """
    Charge les modèles de prédiction des gliomes
    """
    try:
        models = joblib.load('glioma_models.pkl')
        scalers = joblib.load('glioma_scalers.pkl')
        feature_encoders = joblib.load('glioma_feature_encoders.pkl')
        target_encoders = joblib.load('glioma_target_encoders.pkl')
        feature_names = joblib.load('glioma_feature_names.pkl')
        return models, scalers, feature_encoders, target_encoders, feature_names
    except:
        return None, None, None, None, None

def main():
    st.set_page_config(
        page_title="Tableau de Bord Médical - Prédictions Gliomes",
        page_icon="🏥",
        layout="wide"
    )
    
    st.title('🏥 Tableau de Bord Médical - Prédictions Gliomes')
    st.markdown("---")
    
    # Sidebar avec navigation
    st.sidebar.title('🧭 Navigation')
    app_mode = st.sidebar.selectbox(
        "Choisissez l'application:",
        ["🏠 Accueil", "🧠 Gliomes"]
    )
    
    # Sidebar avec informations générales
    st.sidebar.markdown("---")
    st.sidebar.title('ℹ️ Informations')
    st.sidebar.markdown("""
    ### 🎯 Objectif
    Ce tableau de bord fournit un système de prédiction médicale pour les gliomes :
    
    - **Gliomes** : Basé sur les données cliniques MU
    
    ### ⚠️ Avertissement
    Ces prédictions sont destinées à des fins éducatives et de recherche.
    Elles ne remplacent pas l'avis médical professionnel.
    """)
    
    if app_mode == "🏠 Accueil":
        show_home_page()
    elif app_mode == "🧠 Gliomes":
        show_glioma_page()

def show_home_page():
    """
    Page d'accueil
    """
    st.header('🏠 Bienvenue dans le Tableau de Bord Médical')
    
    st.subheader('🧠 Prédiction des Gliomes')
    st.markdown("""
    **Base de données :** MU-Glioma Clinical Data
    
    **Variables prédites :**
    - Progression de la tumeur
    - Survie globale
    - Grade tumoral
    
    **Facteurs pris en compte :**
    - Caractéristiques démographiques
    - Mutations génétiques (IDH1, IDH2, MGMT)
    - Antécédents médicaux
    - Traitements reçus
    
    **Modèles utilisés :**
    - Random Forest
    - Classification multi-classes
    """)
    
    if st.button('🚀 Accéder aux prédictions de gliomes'):
        st.switch_page("🧠 Gliomes")
    
    st.markdown("---")
    st.subheader('📈 Statistiques des Modèles')
    
    # Vérifier la disponibilité des modèles
    glioma_models, glioma_scalers, _, _, _ = load_glioma_models()
    
    if glioma_models is not None:
        st.success('✅ Modèles de gliomes disponibles')
        st.metric("Nombre de modèles", len(glioma_models))
        st.metric("Variables d'entrée", "12")
    else:
        st.error('❌ Modèles de gliomes non disponibles')

def show_glioma_page():
    """
    Page de prédiction des gliomes
    """
    st.header('🧠 Prédiction des Gliomes')
    
    # Charger les modèles
    models, scalers, feature_encoders, target_encoders, feature_names = load_glioma_models()
    
    if models is None:
        st.error("❌ Modèles non disponibles. Veuillez d'abord exécuter l'entraînement.")
        return
    
    # Formulaire de saisie
    with st.form("glioma_form"):
        st.subheader('📋 Données Patient')
        
        col1, col2 = st.columns(2)
        
        with col1:
            sex = st.selectbox('Sexe à la naissance', ['Male', 'Female', 'Unknown'])
            age = st.number_input('Âge au diagnostic', 0, 100, 50)
            primary_diagnosis = st.selectbox('Diagnostic primaire', 
                                           ['Glioblastoma', 'Astrocytoma', 'Oligodendroglioma', 'Unknown'])
            grade = st.selectbox('Grade de la tumeur', 
                               ['Grade I', 'Grade II', 'Grade III', 'Grade IV', 'Unknown'])
        
        with col2:
            idh1 = st.selectbox('Mutation IDH1', ['Positive', 'Negative', 'Unknown'])
            idh2 = st.selectbox('Mutation IDH2', ['Positive', 'Negative', 'Unknown'])
            mgmt = st.selectbox('Méthylation MGMT', ['Methylated', 'Unmethylated', 'Unknown'])
            egfr = st.selectbox('Amplification EGFR', ['Present', 'Absent', 'Unknown'])
            chemo = st.selectbox('Chimiothérapie', ['Yes', 'No', 'Unknown'])
            radiation = st.selectbox('Radiothérapie', ['Yes', 'No', 'Unknown'])
        
        submitted = st.form_submit_button("🔮 Prédire les gliomes")
    
    if submitted:
        st.header('🎯 Résultats de la Prédiction')
        
        # Préparer les données
        input_data = {
            'Sex at Birth': sex,
            'Age at diagnosis': age,
            'Primary Diagnosis': primary_diagnosis,
            'Grade of Primary Brain Tumor': grade,
            'IDH1 mutation': idh1,
            'IDH2 mutation': idh2,
            'MGMT methylation': mgmt,
            'EGFR amplification': egfr,
            'Initial Chemo Therapy': chemo,
            'Radiation Therapy': radiation
        }
        
        # Faire les prédictions
        for target_name, model in models.items():
            if target_name in scalers and target_name in target_encoders:
                st.subheader(f'📊 {target_name}')
                
                # Préparer les features
                input_features = []
                for feature_name in feature_names:
                    if feature_name in input_data:
                        value = input_data[feature_name]
                        
                        # Encoder
                        if feature_name in feature_encoders:
                            encoder = feature_encoders[feature_name]
                            if hasattr(encoder, 'transform'):
                                try:
                                    encoded_value = encoder.transform([str(value)])[0]
                                except:
                                    encoded_value = 0
                            else:
                                encoded_value = encoder.get(str(value), 0)
                        else:
                            encoded_value = value if isinstance(value, (int, float)) else 0
                        
                        input_features.append(encoded_value)
                    else:
                        input_features.append(0)
                
                # Prédire
                input_scaled = scalers[target_name].transform([input_features])
                prediction = model.predict(input_scaled)[0]
                probabilities = model.predict_proba(input_scaled)[0]
                
                # Afficher les résultats
                col_result1, col_result2 = st.columns(2)
                
                with col_result1:
                    if target_name == 'Progression':
                        if prediction == 1:
                            st.error("⚠️ Risque de progression")
                        else:
                            st.success("✅ Faible risque de progression")
                    
                    elif target_name == 'Overall Survival (Death)':
                        if prediction == 1:
                            st.error("💀 Risque de mortalité élevé")
                        else:
                            st.success("✅ Bon pronostic")
                
                with col_result2:
                    max_prob = max(probabilities)
                    st.metric("Confiance", f"{max_prob:.1%}")

if __name__ == "__main__":
    main()
