# 🏥 Système de Prédiction Médicale - Gliomes

Ce projet utilise le Machine Learning pour analyser et prédire différents aspects des gliomes cérébraux basé sur les données cliniques.

## 📋 Vue d'ensemble

### 🧠 Prédiction des Gliomes
- **Base de données** : MU-Glioma Clinical Data (335 patients)
- **Objectif** : Prédire la progression, la survie et le grade des tumeurs cérébrales
- **Variables prédites** : Progression, Survie globale, Grade tumoral
- **Modèles** : Random Forest (classification multi-classes)

## 🚀 Installation et Configuration

### Prérequis
```bash
Python 3.8+
```

### Installation des dépendances
```bash
pip install -r requirement.txt
```

### Dépendances principales
- `pandas` - Manipulation des données
- `numpy` - Calculs numériques
- `scikit-learn` - Machine Learning
- `streamlit` - Interface utilisateur
- `openpyxl` - Lecture des fichiers Excel
- `matplotlib` et `seaborn` - Visualisations
- `joblib` - Sauvegarde des modèles

## 📁 Structure du Projet

```
ClinicalDataGlioma/
├── 📊 Données
│   └── BrainClinicalData/
│       └── MU-Glioma-Post_ClinicalData-July2025.xlsx
├── 🧠 Modèles
│   ├── glioma_models.pkl                 # Modèles de gliomes
│   ├── glioma_scalers.pkl                # Standardisation gliomes
│   ├── glioma_feature_encoders.pkl       # Encodeurs features
│   ├── glioma_target_encoders.pkl        # Encodeurs cibles
│   └── glioma_feature_names.pkl          # Noms des features
├── 🔧 Scripts d'analyse
│   ├── glioma_analysis_simple.py         # Analyse gliomes
│   ├── simple_analysis.py                # Analyse exploratoire
│   └── analyze_brain_data.py             # Analyse détaillée
├── 🌐 Applications
│   ├── glioma_prediction_app.py          # App gliomes seule
│   ├── medical_prediction_dashboard.py   # Dashboard complet
│   └── run_apps.py                       # Lanceur d'applications
└── 📚 Documentation
    ├── README.md                         # Documentation principale
    └── README_COMPLET.md                 # Documentation complète
```

## 🎯 Utilisation

### 1. Entraînement des Modèles

#### Gliomes
```bash
python glioma_analysis_simple.py
```
Ce script :
- Charge les données cliniques des gliomes
- Prépare et encode les features
- Entraîne les modèles de prédiction
- Sauvegarde les modèles entraînés

### 2. Applications Web

#### Dashboard Complet
```bash
streamlit run medical_prediction_dashboard.py
```
Interface unifiée avec :
- Navigation intuitive
- Formulaires de saisie interactifs
- Visualisations des résultats
- Prédictions en temps réel

#### Application Gliomes Seule
```bash
streamlit run glioma_prediction_app.py
```
Interface spécialisée pour les gliomes avec :
- Formulaire détaillé
- Prédictions multiples
- Recommandations médicales

#### Lanceur d'Applications
```bash
python run_apps.py
```
Interface de lancement avec :
- Vérification des dépendances
- Vérification des modèles
- Menu de sélection d'application

## 📊 Variables et Features

### Gliomes (MU Clinical Data)
| Variable | Type | Description |
|----------|------|-------------|
| Sex at Birth | Catégoriel | Sexe à la naissance |
| Age at diagnosis | Numérique | Âge au diagnostic |
| Primary Diagnosis | Catégoriel | Type de tumeur |
| Grade of Primary Brain Tumor | Catégoriel | Grade tumoral |
| IDH1 mutation | Catégoriel | Mutation IDH1 |
| IDH2 mutation | Catégoriel | Mutation IDH2 |
| MGMT methylation | Catégoriel | Méthylation MGMT |
| EGFR amplification | Catégoriel | Amplification EGFR |
| Initial Chemo Therapy | Catégoriel | Chimiothérapie |
| Radiation Therapy | Catégoriel | Radiothérapie |

## 🔬 Méthodologie

### Préprocessing des Données
1. **Nettoyage** : Gestion des valeurs manquantes, suppression des doublons
2. **Encodage** : Transformation des variables catégorielles
3. **Standardisation** : Normalisation des variables numériques
4. **Feature Engineering** : Création de nouvelles variables pertinentes

### Modèles Utilisés
1. **Random Forest** : Ensemble d'arbres de décision
2. **Classification Multi-classes** : Pour différents aspects des gliomes
3. **Encodage Cible** : Gestion des variables catégorielles de sortie

### Évaluation
- **Métriques** : Accuracy, Precision, Recall, F1-Score, AUC-ROC
- **Validation** : Train/Test split (80/20)
- **Visualisations** : Matrices de confusion, courbes ROC

## 📈 Résultats et Performance

### Gliomes
- **Modèles** : Random Forest pour chaque variable cible
- **Précision** : Variable selon la cible (60-80%)
- **Variables importantes** : Mutations génétiques, grade tumoral
- **Cibles prédites** : Progression, Survie globale, Grade

## 🎨 Interface Utilisateur

### Fonctionnalités
- **Formulaires interactifs** : Saisie facile des données patient
- **Prédictions en temps réel** : Résultats instantanés
- **Visualisations** : Graphiques et métriques claires
- **Recommandations** : Conseils basés sur les prédictions
- **Navigation intuitive** : Interface multi-pages

### Design
- **Responsive** : Adapté à différents écrans
- **Accessible** : Interface claire et intuitive
- **Professionnel** : Design médical approprié
- **Multilingue** : Interface en français

## ⚠️ Limitations et Avertissements

### Limitations Techniques
- Taille d'échantillon limitée pour les gliomes
- Variables manquantes dans certaines données
- Modèles non validés cliniquement
- Données spécifiques à un centre médical

### Avertissements Médicaux
- **Usage éducatif uniquement** : Ces prédictions ne remplacent pas l'avis médical
- **Validation clinique requise** : Les modèles nécessitent une validation externe
- **Contexte important** : Les résultats doivent être interprétés dans le contexte clinique
- **Évolution des connaissances** : Les modèles peuvent devenir obsolètes

## 🔮 Améliorations Futures

### Techniques
1. **Deep Learning** : Réseaux de neurones pour données complexes
2. **Ensemble Methods** : Combinaison de plusieurs modèles
3. **Feature Engineering** : Création de nouvelles variables
4. **AutoML** : Optimisation automatique des hyperparamètres

### Cliniques
1. **Validation externe** : Tests sur de nouveaux ensembles de données
2. **Études prospectives** : Validation en conditions réelles
3. **Intégration hospitalière** : Connexion aux systèmes d'information
4. **API médicale** : Interface pour applications tierces

### Données
1. **Données multi-modales** : Imagerie, génomique, clinique
2. **Données longitudinales** : Suivi temporel des patients
3. **Données fédérées** : Collaboration multi-centres
4. **Données en temps réel** : Mise à jour continue

## 👥 Contribution

### Développement
1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

### Tests
- Ajouter des tests unitaires
- Valider les performances des modèles
- Tester l'interface utilisateur
- Vérifier la compatibilité des données

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📞 Contact

Pour toute question ou suggestion :
- **Email** : [votre-email@example.com]
- **GitHub** : [votre-username]
- **LinkedIn** : [votre-profil-linkedin]

## 🙏 Remerciements

- **MU Clinical Data** : Pour les données sur les gliomes
- **Communauté Streamlit** : Pour l'outil de développement d'applications
- **Scikit-learn** : Pour les algorithmes de Machine Learning

---

**Note** : Ce projet est destiné à des fins éducatives et de recherche. Toute utilisation clinique nécessite une validation médicale appropriée.
