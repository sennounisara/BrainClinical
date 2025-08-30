# Glioma Prediction System

This project predicts glioma progression and survival using machine learning models trained on clinical data. It includes data preprocessing, model training and evaluation, and a user-friendly web application for making predictions.

## Features

- **Data Cleaning:** Handles missing values, removes duplicates, and manages outliers.
- **Feature Engineering:** Encodes categorical variables and scales numerical features.
- **Exploratory Data Analysis:** Visualizes data distributions and correlations.
- **Model Training:** Trains and evaluates multiple classifiers for different prediction targets:
  - Progression prediction
  - Overall survival prediction
  - Grade prediction
- **Model Selection:** Selects the best models for each target and saves them for deployment.
- **Web Application:** Streamlit app for interactive glioma prediction.

## Requirements

Install dependencies with:

```bash
pip install -r requirement.txt
```

## Usage

### 1. Data Preparation & Model Training

The main script (`glioma_analysis_simple.py`) performs:

- Data loading and cleaning
- Feature engineering
- Model training and evaluation
- Model selection and saving

Run the script:

```bash
python glioma_analysis_simple.py
```

### 2. Web Application

After training, launch the Streamlit app:

```bash
streamlit run glioma_prediction_app.py
```

#### App Features

- User input form for patient data (age, sex, diagnosis, grade, genetic mutations, treatments)
- Real-time prediction of glioma progression and survival
- Probability scores and risk assessment

## Files

- `glioma_analysis_simple.py` — Main script for data processing and model training
- `glioma_prediction_app.py` — Streamlit application for predictions
- `medical_prediction_dashboard.py` — Comprehensive dashboard
- `run_apps.py` — Application launcher
- `BrainClinicalData/` — Clinical data directory
- `glioma_models.pkl` — Saved models
- `glioma_scalers.pkl` — Saved scalers
- `glioma_feature_encoders.pkl` — Feature encoders
- `glioma_target_encoders.pkl` — Target encoders
- `glioma_feature_names.pkl` — Feature names
- `requirement.txt` — Python dependencies

## Data

The system uses clinical data including:
- Patient demographics (age, sex)
- Tumor characteristics (diagnosis, grade)
- Genetic mutations (IDH1, IDH2, MGMT, EGFR)
- Treatment history (chemotherapy, radiation)

## Models

The system trains separate models for different prediction targets:
- **Progression:** Binary classification for tumor progression
- **Overall Survival:** Binary classification for survival prediction
- **Grade:** Multi-class classification for tumor grading

## Notes

- The project handles categorical variables through encoding
- Multiple models are saved for different prediction targets
- The Streamlit app provides an interactive interface for predictions

---

## License

[MIT License](LICENSE) (or your preferred license)
