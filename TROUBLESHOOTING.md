# 🔧 Guide de Dépannage - Erreur d'Installation des Dépendances

## ❌ Erreur : "Error installing requirements"

### 🔍 Diagnostic

Cette erreur indique que Streamlit Cloud ne peut pas installer les dépendances Python. Voici les solutions :

### ✅ Solution 1 : Requirements Minimal (Recommandé)

1. **Utilisez** le `requirement.txt` actuel (déjà corrigé)
2. **Supprimez** `packages.txt` s'il existe
3. **Redéployez** l'application

```bash
# Dans votre repository local
mv requirements_minimal.txt requirement.txt
rm requirement.txt.old  # si existe
git add requirement.txt
git commit -m "fix: use minimal requirements for deployment"
git push
```

### ✅ Solution 2 : Vérifier les Logs

1. Allez dans Streamlit Cloud
2. Cliquez sur "Manage App"
3. Consultez les logs du terminal
4. Identifiez le package problématique

### ✅ Solution 3 : Versions Compatibles

Si Solution 1 ne fonctionne pas, utilisez ce `requirement.txt` :

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.21.0
scikit-learn>=1.1.0
joblib>=1.2.0
openpyxl>=3.0.0
```

### ✅ Solution 4 : Déploiement Étape par Étape

1. **Testez d'abord** avec `test_deployment.py`
2. **Utilisez** `requirements_minimal.txt`
3. **Vérifiez** que tous les fichiers .pkl sont présents
4. **Déployez** progressivement

### 🚨 Problèmes Courants

#### 1. Version Python Incompatible
- Streamlit Cloud utilise Python 3.9-3.11
- Certaines versions de packages peuvent être incompatibles

#### 2. Dépendances Système Manquantes
- **Supprimez** `packages.txt` complètement
- Il causait l'erreur "Unable to locate package"
- Les packages système ne sont pas nécessaires pour cette app

#### 3. Conflit de Versions
- Utilisez des versions flexibles (`>=`) plutôt que fixes (`==`)
- Évitez les versions trop récentes

### 📋 Checklist de Déploiement

- [ ] `requirement.txt` contient seulement les packages essentiels
- [ ] **PAS de `packages.txt`** (supprimé pour éviter les erreurs)
- [ ] Tous les fichiers .pkl sont dans le repository
- [ ] `glioma_prediction_app.py` est à la racine
- [ ] `.streamlit/config.toml` est présent

### 🎯 Configuration Finale Recommandée

**requirement.txt :**
```
streamlit
pandas
numpy
scikit-learn
joblib
openpyxl
```

**Fichiers requis :**
- `glioma_prediction_app.py`
- `glioma_models.pkl`
- `glioma_scalers.pkl`
- `glioma_feature_encoders.pkl`
- `glioma_target_encoders.pkl`
- `glioma_feature_names.pkl`
- `.streamlit/config.toml`

### 📞 Support

Si le problème persiste :
1. Vérifiez les logs dans "Manage App"
2. Testez avec `test_deployment.py`
3. Utilisez la configuration minimale
4. Contactez le support Streamlit si nécessaire
