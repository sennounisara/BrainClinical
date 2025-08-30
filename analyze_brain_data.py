import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def analyze_brain_clinical_data():
    """
    Analyse les données cliniques du cerveau pour comprendre leur structure
    et identifier les variables pertinentes pour la prédiction
    """
    
    # Charger les données
    file_path = Path('BrainClinicalData/MU-Glioma-Post_ClinicalData-July2025.xlsx')
    
    try:
        df = pd.read_excel(file_path)
        print("✅ Données chargées avec succès!")
        print(f"📊 Forme des données: {df.shape}")
        print(f"📋 Nombre de colonnes: {len(df.columns)}")
        print(f"👥 Nombre de patients: {len(df)}")
        
        # Afficher les colonnes
        print("\n📝 Colonnes disponibles:")
        for i, col in enumerate(df.columns, 1):
            print(f"{i:2d}. {col}")
        
        # Informations générales sur les données
        print("\n🔍 Informations générales:")
        print(df.info())
        
        # Statistiques descriptives
        print("\n📈 Statistiques descriptives:")
        print(df.describe())
        
        # Valeurs manquantes
        print("\n❓ Valeurs manquantes:")
        missing_data = df.isnull().sum()
        missing_percent = (missing_data / len(df)) * 100
        missing_df = pd.DataFrame({
            'Colonne': missing_data.index,
            'Valeurs_manquantes': missing_data.values,
            'Pourcentage': missing_percent.values
        })
        missing_df = missing_df[missing_df['Valeurs_manquantes'] > 0].sort_values('Valeurs_manquantes', ascending=False)
        
        if len(missing_df) > 0:
            print(missing_df)
        else:
            print("✅ Aucune valeur manquante détectée!")
        
        # Types de données
        print("\n🔧 Types de données:")
        print(df.dtypes.value_counts())
        
        # Aperçu des premières lignes
        print("\n👀 Aperçu des données (5 premières lignes):")
        print(df.head())
        
        # Identifier les variables numériques et catégorielles
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        print(f"\n📊 Variables numériques ({len(numeric_cols)}):")
        print(numeric_cols)
        
        print(f"\n🏷️ Variables catégorielles ({len(categorical_cols)}):")
        print(categorical_cols)
        
        # Analyser les variables catégorielles
        if categorical_cols:
            print("\n📋 Analyse des variables catégorielles:")
            for col in categorical_cols:
                print(f"\n{col}:")
                print(f"  Valeurs uniques: {df[col].nunique()}")
                print(f"  Top 5 valeurs: {df[col].value_counts().head().to_dict()}")
        
        # Identifier les variables cibles potentielles
        print("\n🎯 Recherche de variables cibles potentielles:")
        target_keywords = ['survival', 'mortality', 'death', 'outcome', 'status', 'prognosis', 
                          'recurrence', 'progression', 'response', 'grade', 'stage', 'type']
        
        potential_targets = []
        for col in df.columns:
            col_lower = col.lower()
            for keyword in target_keywords:
                if keyword in col_lower:
                    potential_targets.append(col)
                    break
        
        if potential_targets:
            print("Variables cibles potentielles trouvées:")
            for target in potential_targets:
                print(f"  - {target}")
        else:
            print("Aucune variable cible évidente trouvée dans les noms de colonnes.")
        
        return df
        
    except Exception as e:
        print(f"❌ Erreur lors du chargement des données: {e}")
        return None

if __name__ == "__main__":
    print("🧠 Analyse des données cliniques du cerveau")
    print("=" * 50)
    
    df = analyze_brain_clinical_data()
    
    if df is not None:
        print("\n✅ Analyse terminée avec succès!")
        print("📁 Les données sont prêtes pour une analyse plus approfondie.")
    else:
        print("\n❌ Échec de l'analyse des données.")
