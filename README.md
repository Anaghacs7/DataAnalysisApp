# DataAnalysisApp
Data Analysis App is a lightweight, menu-driven desktop tool offering CSV preview, descriptive stats, regression, and clustering via command-line menu or GUI.

## Features
- **Load any CSV** via console or simple GUI  
- **Descriptive statistics**: view count, mean, std, min/max, quartiles  
- **Linear regression**: pick your own target (automatically encodes categorical targets), fit a model, and display coefficients, intercept & R²  
- **K-Means clustering**: choose cluster count and assign labels  
- **Two modes**: terminal menu or Tkinter interface  
- **Standalone binary**: bundle with PyInstaller for easy distribution

## Tech
- **Python 3.10+**  
- **Pandas** for data handling  
- **scikit-learn** for modeling & preprocessing  
- **Tkinter** for GUI  
- **PyInstaller** for packaging

## Install & Run
1. **Clone**  
   ```bash
   git clone https://github.com/Anaghacs7/data_analysis_app.git
   cd data_analysis_app
