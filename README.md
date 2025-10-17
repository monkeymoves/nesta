# Interview Data Analysis Project

This project analyses the provided CSV files:

- nh_monthly_variables.csv
- ifs_quarterly_variables.csv
- qual_survey_responses.csv
- variable_names.csv

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/01_exploration.ipynb
```

Place the CSVs in `data/raw/`.

## Optional: Open in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/monkeymoves/nesta/blob/master/notebooks/01_exploration.ipynb)
## Project Layout

```
interview_project/
├── data/
│   ├── raw/
│   ├── external/
│   └── processed/
├── notebooks/
│   └── 01_exploration.ipynb
├── reports/
│   └── figures/
├── src/
│   └── data_io.py
├── requirements.txt
└── README.md
```
