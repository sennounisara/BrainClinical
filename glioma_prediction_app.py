import streamlit as st
import joblib
import numpy as np
import openpyxl

def load_models():
    """
    Charge les modèles entraînés
    """
    try:
        models = joblib.load('glioma_models.pkl')
        scalers = joblib.load('glioma_scalers.pkl')
        feature_encoders = joblib.load('glioma_feature_encoders.pkl')
        target_encoders = joblib.load('glioma_target_encoders.pkl')
        feature_names = joblib.load('glioma_feature_names.pkl')
        return models, scalers, feature_encoders, target_encoders, feature_names
    except:
        st.error("❌ Impossible de charger les modèles. Veuillez d'abord exécuter l'entraînement.")
        return None, None, None, None, None

def main():
    st.set_page_config(
        page_title="Prédiction des Gliomes",
        page_icon="🧠",
        layout="wide"
    )
    
    st.title('🧠 Prédiction des Gliomes - Analyse Clinique')
    st.markdown("---")
    
    # Sidebar avec informations
    st.sidebar.title('ℹ️ Informations sur l\'Application')
    st.sidebar.markdown("""
    ### 🎯 Objectif
    Cette application utilise des modèles de Machine Learning pour prédire 
    différents aspects des gliomes basés sur les données cliniques.
    
    ### 📊 Variables prédites:
    - **Progression**: Risque de progression de la tumeur
    - **Survie globale**: Prédiction de survie
    - **Grade de la tumeur**: Classification du grade tumoral
    
    ### 🔬 Facteurs pris en compte:
    - Caractéristiques démographiques (âge, sexe)
    - Mutations génétiques (IDH1, IDH2, MGMT, etc.)
    - Antécédents médicaux
    - Traitements reçus
    
    ### ⚠️ Avertissement
    Cette application est destinée à des fins éducatives et de recherche.
    Les prédictions ne remplacent pas l'avis médical professionnel.
    """)
    
    # Charger les modèles
    models, scalers, feature_encoders, target_encoders, feature_names = load_models()
    
    if models is None:
        st.warning("⚠️ Modèles non disponibles. Veuillez d'abord exécuter l'entraînement.")
        return
    
    # Interface principale
    st.header('📋 Saisie des Données Patient')
    
    # Formulaire de saisie
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("👤 Informations démographiques")
            sex = st.selectbox('Sexe à la naissance', ['Male', 'Female', 'Unknown'])
            age = st.number_input('Âge au diagnostic', min_value=0, max_value=100, value=50)
            
            st.subheader("🏥 Diagnostic")
            primary_diagnosis = st.selectbox('Diagnostic primaire', 
                                           ['Glioblastoma', 'Astrocytoma', 'Oligodendroglioma', 'Unknown'])
            grade = st.selectbox('Grade de la tumeur primaire', 
                               ['Grade I', 'Grade II', 'Grade III', 'Grade IV', 'Unknown'])
        
        with col2:
            st.subheader("🧬 Mutations génétiques")
            idh1 = st.selectbox('Mutation IDH1', ['Positive', 'Negative', 'Unknown'])
            idh2 = st.selectbox('Mutation IDH2', ['Positive', 'Negative', 'Unknown'])
            codeletion = st.selectbox('Codeletion 1p/19q', ['Present', 'Absent', 'Unknown'])
            mgmt = st.selectbox('Méthylation MGMT', ['Methylated', 'Unmethylated', 'Unknown'])
            egfr = st.selectbox('Amplification EGFR', ['Present', 'Absent', 'Unknown'])
        
        # Traitements
        st.subheader('💊 Traitements')
        col3, col4 = st.columns(2)
        
        with col3:
            chemo = st.selectbox('Chimiothérapie initiale', ['Yes', 'No', 'Unknown'])
            radiation = st.selectbox('Radiothérapie', ['Yes', 'No', 'Unknown'])
        
        with col4:
            previous_tumor = st.selectbox('Tumeur cérébrale antérieure', ['Yes', 'No', 'Unknown'])
        
        submitted = st.form_submit_button("🔮 Faire la Prédiction", use_container_width=True)
    
    if submitted:
        st.header('🎯 Résultats de la Prédiction')
        
        # Préparer les données d'entrée
        input_data = {
            'Sex at Birth': sex,
            'Age at diagnosis': age,
            'Primary Diagnosis': primary_diagnosis,
            'Grade of Primary Brain Tumor': grade,
            'IDH1 mutation': idh1,
            'IDH2 mutation': idh2,
            '1p/19q': codeletion,
            'MGMT methylation': mgmt,
            'EGFR amplification': egfr,
            'Previous Brain Tumor': previous_tumor,
            'Initial Chemo Therapy': chemo,
            'Radiation Therapy': radiation
        }
        
        # Faire les prédictions pour chaque modèle
        for target_name, model in models.items():
            if target_name in scalers and target_name in target_encoders:
                st.subheader(f'📊 Prédiction: {target_name}')
                
                # Préparer les données d'entrée
                input_features = []
                for feature_name in feature_names:
                    if feature_name in input_data:
                        value = input_data[feature_name]
                        
                        # Encoder si nécessaire
                        if feature_name in feature_encoders:
                            encoder = feature_encoders[feature_name]
                            if hasattr(encoder, 'transform'):
                                try:
                                    encoded_value = encoder.transform([str(value)])[0]
                                except:
                                    encoded_value = 0
                            else:
                                # C'est un dictionnaire de mapping
                                encoded_value = encoder.get(str(value), 0)
                        else:
                            encoded_value = value if isinstance(value, (int, float)) else 0
                        
                        input_features.append(encoded_value)
                    else:
                        input_features.append(0)
                
                # Standardiser et prédire
                input_scaled = scalers[target_name].transform([input_features])
                prediction = model.predict(input_scaled)[0]
                probabilities = model.predict_proba(input_scaled)[0]
                
                # Afficher les résultats
                col_result1, col_result2 = st.columns(2)
                
                with col_result1:
                    if target_name == 'Progression':
                        if prediction == 1:
                            st.error("⚠️ Risque de progression détecté")
                        else:
                            st.success("✅ Faible risque de progression")
                    
                    elif target_name == 'Overall Survival (Death)':
                        if prediction == 1:
                            st.error("💀 Risque de mortalité élevé")
                        else:
                            st.success("✅ Bon pronostic de survie")
                    
                    elif target_name == 'Grade of Primary Brain Tumor':
                        grade_labels = ['Grade I', 'Grade II', 'Grade III', 'Grade IV']
                        if prediction < len(grade_labels):
                            predicted_grade = grade_labels[prediction]
                            st.info(f"📋 Grade prédit: {predicted_grade}")
                
                with col_result2:
                    # Afficher la confiance
                    max_prob = max(probabilities)
                    st.metric("Confiance du modèle", f"{max_prob:.1%}")
                    
                    # Afficher les probabilités pour chaque classe
                    if target_name in target_encoders:
                        encoder = target_encoders[target_name]
                        if hasattr(encoder, 'classes_'):
                            classes = encoder.classes_
                        else:
                            # C'est un dictionnaire, utiliser les clés
                            classes = list(encoder.keys())
                        
                        st.write("**Probabilités par classe:**")
                        for i, (prob, class_name) in enumerate(zip(probabilities, classes)):
                            st.write(f"- {class_name}: {prob:.1%}")
        
        # Recommandations générales
        st.header('💡 Recommandations')
        st.markdown("""
        ### 📋 Prochaines étapes recommandées:
        1. **Consultation médicale**: Discutez de ces résultats avec votre équipe médicale
        2. **Surveillance rapprochée**: Suivi régulier selon les recommandations
        3. **Tests complémentaires**: Examens supplémentaires si nécessaire
        4. **Plan de traitement**: Adaptation du traitement selon les prédictions
        
        ### 🔬 Facteurs de risque identifiés:
        - Les mutations génétiques (IDH1, MGMT) sont des marqueurs pronostiques importants
        - Le grade tumoral influence significativement le pronostic
        - Les antécédents de tumeur cérébrale peuvent modifier l'approche thérapeutique
        
        ### ⚠️ Limitations:
        - Ces prédictions sont basées sur des données historiques
        - Chaque patient est unique et peut répondre différemment
        - Les avancées thérapeutiques peuvent modifier les pronostics
        """)

if __name__ == "__main__":
    main()
