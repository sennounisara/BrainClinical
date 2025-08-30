import streamlit as st
import sys
import os

def test_imports():
    """Test if all required packages can be imported"""
    st.title("🧪 Test de Déploiement - Vérification des Dépendances")
    
    st.write("### 📦 Vérification des imports...")
    
    # Test basic imports
    try:
        import joblib
        st.success("✅ joblib importé avec succès")
        st.write(f"Version: {joblib.__version__}")
    except ImportError as e:
        st.error(f"❌ Erreur import joblib: {e}")
    
    try:
        import numpy as np
        st.success("✅ numpy importé avec succès")
        st.write(f"Version: {np.__version__}")
    except ImportError as e:
        st.error(f"❌ Erreur import numpy: {e}")
    
    try:
        import pandas as pd
        st.success("✅ pandas importé avec succès")
        st.write(f"Version: {pd.__version__}")
    except ImportError as e:
        st.error(f"❌ Erreur import pandas: {e}")
    
    try:
        import sklearn
        st.success("✅ scikit-learn importé avec succès")
        st.write(f"Version: {sklearn.__version__}")
    except ImportError as e:
        st.error(f"❌ Erreur import scikit-learn: {e}")
    
    try:
        import openpyxl
        st.success("✅ openpyxl importé avec succès")
        st.write(f"Version: {openpyxl.__version__}")
    except ImportError as e:
        st.error(f"❌ Erreur import openpyxl: {e}")
    
    # Test file existence
    st.write("### 📁 Vérification des fichiers...")
    
    required_files = [
        'glioma_models.pkl',
        'glioma_scalers.pkl', 
        'glioma_feature_encoders.pkl',
        'glioma_target_encoders.pkl',
        'glioma_feature_names.pkl'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            st.success(f"✅ {file} trouvé")
        else:
            st.error(f"❌ {file} manquant")
    
    # System info
    st.write("### 💻 Informations système...")
    st.write(f"Python version: {sys.version}")
    st.write(f"Working directory: {os.getcwd()}")
    st.write(f"Files in directory: {len(os.listdir('.'))}")

if __name__ == "__main__":
    test_imports()
