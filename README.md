# Interview Data Analysis Project

This project is supported by this analysis document [https://docs.google.com/document/d/12BrwzeASjTUqxsiNHTftcSD7gW4P4OOKcdcvdLcTebY/edit?usp=sharing]

UK Labour Force Survey data has been analysed to support a hypothetical investigation into a new Nesta Mission around **"A Growing Economy"**
more informnation here: [https://www.ons.gov.uk/surveys/informationforhouseholdsandindividuals/householdandindividualsurveys/labourforcesurvey]

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/01_exploration.ipynb
```

Place the CSVs in `data/raw/`.

## Optional: Open in Google Colab

If you have a google account you can use the free Colab notebook to interactively explore this analysis

You will need an OpenAI API key to test the themeatic analysis, otherwise a sample export has been provided in the rendered notebook and tab in this document: [https://docs.google.com/document/d/12BrwzeASjTUqxsiNHTftcSD7gW4P4OOKcdcvdLcTebY/edit?tab=t.0]

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
├── requirements.txt
└── README.md
```
