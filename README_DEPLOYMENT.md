# 🚀 Guide de Déploiement Streamlit Cloud

## Configuration Correcte pour le Déploiement

### 1. URL GitHub Correcte
**❌ Incorrect (actuel):**
```
https://github.com/sennounisara/BrainClinical/blob/master/glioma_prediction_app.py
```

**✅ Correct:**
```
https://github.com/sennounisara/BrainClinical
```

### 2. Fichiers Requis pour le Déploiement

Votre repository doit contenir ces fichiers essentiels :

```
📁 Repository Root
├── 📄 glioma_prediction_app.py     # Application principale
├── 📄 requirement.txt              # Dépendances Python
├── 📁 .streamlit/
│   └── 📄 config.toml             # Configuration Streamlit
├── 📄 glioma_models.pkl           # Modèles entraînés
├── 📄 glioma_scalers.pkl          # Scalers
├── 📄 glioma_feature_encoders.pkl # Encodeurs de features
├── 📄 glioma_target_encoders.pkl  # Encodeurs de targets
└── 📄 glioma_feature_names.pkl    # Noms des features
```

### 3. Configuration Streamlit Cloud

#### Étape 1: Accéder à Streamlit Cloud
1. Allez sur [share.streamlit.io](https://share.streamlit.io)
2. Connectez-vous avec votre compte GitHub

#### Étape 2: Nouveau Déploiement
1. Cliquez sur "New app"
2. Remplissez les champs :

**Repository:** `sennounisara/BrainClinical`
**Branch:** `master` (ou votre branche principale)
**Main file path:** `glioma_prediction_app.py`
**App URL:** `gliomapredictionapp` (ou votre choix)

#### Étape 3: Déployer
1. Cliquez sur "Deploy"
2. Attendez que le déploiement se termine (2-5 minutes)

### 4. Vérifications Post-Déploiement

#### ✅ Vérifiez que :
- [ ] L'application se charge sans erreur
- [ ] Les modèles se chargent correctement
- [ ] L'interface utilisateur s'affiche
- [ ] Les prédictions fonctionnent

#### ❌ Problèmes Courants :
- **Erreur de chargement des modèles** → Vérifiez que tous les fichiers .pkl sont dans le repository
- **Erreur de dépendances** → Vérifiez le requirement.txt
- **Erreur de chemin** → Vérifiez que glioma_prediction_app.py est à la racine

### 5. URL Finale
Votre application sera accessible à :
```
https://gliomapredictionapp.streamlit.app
```

### 6. Mise à Jour
Pour mettre à jour votre application :
1. Poussez vos changements sur GitHub
2. Streamlit Cloud redéploiera automatiquement

### 7. Support
Si vous rencontrez des problèmes :
1. Vérifiez les logs de déploiement dans Streamlit Cloud
2. Assurez-vous que l'application fonctionne localement
3. Vérifiez que tous les fichiers sont commités sur GitHub

---

## 🎯 Résumé de la Configuration Correcte

**URL GitHub:** `https://github.com/sennounisara/BrainClinical`
**Fichier principal:** `glioma_prediction_app.py`
**URL App:** `gliomapredictionapp.streamlit.app`

Cette configuration devrait permettre un déploiement réussi de votre application de prédiction de gliomes !
