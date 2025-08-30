#!/usr/bin/env python3
"""
Script de lancement pour les applications de prédiction médicale
"""

import subprocess
import sys
import os
from pathlib import Path

def print_banner():
    """Affiche la bannière du projet"""
    print("=" * 60)
    print("🏥 SYSTÈME DE PRÉDICTION MÉDICALE")
    print("   Gliomes")
    print("=" * 60)
    print()

def check_dependencies():
    """Vérifie que les dépendances sont installées"""
    print("🔍 Vérification des dépendances...")
    
    required_packages = [
        'streamlit', 'pandas', 'numpy', 'sklearn', 
        'openpyxl', 'matplotlib', 'seaborn', 'joblib'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - Manquant")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️ Packages manquants : {', '.join(missing_packages)}")
        print("Installez-les avec : pip install -r requirement.txt")
        return False
    
    print("✅ Toutes les dépendances sont installées")
    return True

def check_data_files():
    """Vérifie que les fichiers de données sont présents"""
    print("\n📁 Vérification des fichiers de données...")
    
    required_files = [
        'BrainClinicalData/MU-Glioma-Post_ClinicalData-July2025.xlsx'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - Manquant")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️ Fichiers manquants : {', '.join(missing_files)}")
        return False
    
    print("✅ Tous les fichiers de données sont présents")
    return True

def check_models():
    """Vérifie que les modèles entraînés sont disponibles"""
    print("\n🧠 Vérification des modèles entraînés...")
    
    glioma_models = [
        'glioma_models.pkl', 'glioma_scalers.pkl', 
        'glioma_feature_encoders.pkl', 'glioma_target_encoders.pkl',
        'glioma_feature_names.pkl'
    ]
    
    glioma_available = all(Path(f).exists() for f in glioma_models)
    
    if glioma_available:
        print("✅ Modèles de gliomes disponibles")
    else:
        print("❌ Modèles de gliomes manquants")
    
    return glioma_available

def show_menu():
    """Affiche le menu principal"""
    print("\n🎯 CHOIX D'APPLICATION")
    print("1. 🧠 Gliomes")
    print("2. 🔧 Entraîner les modèles")
    print("3. 📊 Analyse exploratoire")
    print("4. ❌ Quitter")
    print()

def run_streamlit_app(app_file, port=8501):
    """Lance une application Streamlit"""
    try:
        print(f"🚀 Lancement de {app_file}...")
        print(f"📱 Interface disponible sur : http://localhost:{port}")
        print("🛑 Appuyez sur Ctrl+C pour arrêter")
        print()
        
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", app_file,
            "--server.port", str(port),
            "--server.headless", "true"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Application arrêtée")
    except Exception as e:
        print(f"❌ Erreur lors du lancement : {e}")

def train_models():
    """Entraîne les modèles"""
    print("\n🔧 ENTRAÎNEMENT DES MODÈLES")
    print("1. 🧠 Gliomes")
    print("2. 🔙 Retour")
    
    choice = input("\nChoisissez une option (1-2) : ").strip()
    
    if choice == "1":
        print("\n🏃‍♂️ Entraînement des modèles de gliomes...")
        try:
            subprocess.run([sys.executable, "glioma_analysis_simple.py"])
            print("✅ Entraînement terminé")
        except Exception as e:
            print(f"❌ Erreur : {e}")
    
    elif choice == "2":
        return
    
    else:
        print("❌ Option invalide")

def run_analysis():
    """Lance l'analyse exploratoire"""
    print("\n📊 ANALYSE EXPLORATOIRE")
    print("1. 🧠 Analyse des données de gliomes")
    print("2. 🔙 Retour")
    
    choice = input("\nChoisissez une option (1-2) : ").strip()
    
    if choice == "1":
        print("\n🔍 Analyse des données de gliomes...")
        try:
            subprocess.run([sys.executable, "simple_analysis.py"])
        except Exception as e:
            print(f"❌ Erreur : {e}")
    
    elif choice == "2":
        return
    
    else:
        print("❌ Option invalide")

def main():
    """Fonction principale"""
    print_banner()
    
    # Vérifications préliminaires
    if not check_dependencies():
        print("\n❌ Veuillez installer les dépendances manquantes")
        return
    
    if not check_data_files():
        print("\n❌ Veuillez placer les fichiers de données manquants")
        return
    
    glioma_available = check_models()
    
    # Menu principal
    while True:
        show_menu()
        
        choice = input("Choisissez une option (1-4) : ").strip()
        
        if choice == "1":
            # Gliomes
            if glioma_available:
                run_streamlit_app("glioma_prediction_app.py", 8501)
            else:
                print("❌ Modèles de gliomes non disponibles")
                print("Entraînez d'abord les modèles (option 2)")
        
        elif choice == "2":
            # Entraînement
            train_models()
        
        elif choice == "3":
            # Analyse
            run_analysis()
        
        elif choice == "4":
            # Quitter
            print("\n👋 Au revoir !")
            break
        
        else:
            print("❌ Option invalide")
        
        input("\nAppuyez sur Entrée pour continuer...")
        print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
