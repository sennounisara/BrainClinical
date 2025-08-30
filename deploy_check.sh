#!/bin/bash

echo "🔍 Vérification du déploiement Streamlit Cloud"
echo "=============================================="

echo ""
echo "📁 Fichiers dans le répertoire actuel :"
ls -la

echo ""
echo "❌ Vérification que packages.txt n'existe PAS :"
if [ -f "packages.txt" ]; then
    echo "⚠️  packages.txt existe encore ! Supprimez-le."
    exit 1
else
    echo "✅ packages.txt n'existe pas (correct)"
fi

echo ""
echo "❌ Vérification que requirements_minimal.txt n'existe PAS :"
if [ -f "requirements_minimal.txt" ]; then
    echo "⚠️  requirements_minimal.txt existe encore ! Supprimez-le."
    exit 1
else
    echo "✅ requirements_minimal.txt n'existe pas (correct)"
fi

echo ""
echo "✅ Vérification que requirement.txt existe :"
if [ -f "requirement.txt" ]; then
    echo "✅ requirement.txt existe"
    echo "📄 Contenu de requirement.txt :"
    cat requirement.txt
else
    echo "❌ requirement.txt manquant !"
    exit 1
fi

echo ""
echo "✅ Vérification que glioma_prediction_app.py existe :"
if [ -f "glioma_prediction_app.py" ]; then
    echo "✅ glioma_prediction_app.py existe"
else
    echo "❌ glioma_prediction_app.py manquant !"
    exit 1
fi

echo ""
echo "✅ Vérification des fichiers .pkl :"
pkl_files=("glioma_models.pkl" "glioma_scalers.pkl" "glioma_feature_encoders.pkl" "glioma_target_encoders.pkl" "glioma_feature_names.pkl")
for file in "${pkl_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file existe"
    else
        echo "❌ $file manquant !"
        exit 1
    fi
done

echo ""
echo "✅ Vérification de .streamlit/config.toml :"
if [ -f ".streamlit/config.toml" ]; then
    echo "✅ .streamlit/config.toml existe"
else
    echo "❌ .streamlit/config.toml manquant !"
    exit 1
fi

echo ""
echo "🎯 Configuration prête pour le déploiement !"
echo ""
echo "📋 Prochaines étapes :"
echo "1. git add ."
echo "2. git commit -m 'fix: remove packages.txt and simplify requirements'"
echo "3. git push"
echo "4. Redéployez sur Streamlit Cloud"
echo ""
echo "✅ Tous les fichiers sont corrects !"
