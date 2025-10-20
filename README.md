

# UK Labour Market Inactivity Analysis

This project analyzes data from the UK Labour Force Survey to investigate trends in economic inactivity. The analysis supports a hypothetical investigation for a new Nesta Mission focused on "A Growing Economy".

  - **Full Analysis Document**: [Google Docs](https://docs.google.com/document/d/12BrwzeASjTUqxsiNHTftcSD7gW4P4OOKcdcvdLcTebY/edit?usp=sharing)
  - **Data Source**: [UK Labour Force Survey (LFS)](https://www.ons.gov.uk/surveys/informationforhouseholdsandindividuals/householdandindividualsurveys/labourforcesurvey)


## Getting Started

To run this project locally, you will need Python 3.8+ installed.

1.  **Clone the repository and place data:**
    Clone this repository to your local machine - LFS data CSVs are in the `data/raw/` directory.

2.  **Create and activate a virtual environment:**

    ```bash
    # Create the virtual environment
    python -m venv .venv

    # Activate it (macOS/Linux)
    source .venv/bin/activate

    # Activate it (Windows)
    # .venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch Jupyter Notebook:**

    ```bash
    jupyter notebook notebooks/01_exploration.ipynb
    ```


##  Open in Google Colab

Alternatively, you can explore the analysis interactively in your browser using Google Colab, no local installation required.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/monkeymoves/nesta/blob/main/notebooks/01_exploration.ipynb)

**Note:** To run the thematic analysis cells yourself, you will need to provide your own OpenAI API key. For convenience, a sample export has already been provided in the notebook and within the main [analysis document](https://docs.google.com/document/d/12BrwzeASjTUqxsiNHTftcSD7gW4P4OOKcdcvdLcTebY/edit?tab=t.0).



## Project Structure

This repository follows industry-standard data science project conventions, promoting reproducibility and maintainability. While not all directories are actively used in this specific implementation, the structure provides a scalable framework for future development.

```
interview_project/
├── data/
│   ├── raw/          # Raw, immutable data (e.g., source CSVs)
│   ├── external/     # Data from third-party sources
│   └── processed/    # Cleaned or transformed data
├── notebooks/
│   └── 01_exploration.ipynb # Main analysis notebook
├── requirements.txt  # Project dependencies
└── README.md         # You are here!
```