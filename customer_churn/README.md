# Predict Customer Churn

- Project **Predict Customer Churn** of ML DevOps Engineer Nanodegree Udacity

## Project Description
This project aimed to rewrite code provided as a notebook into a high-quality and testable script, following PEP8 standards and coding best practices, the project is structured as follows,

* `churn_library.py` contains the logic corresponding the original notebook, rewritten as appropriate to higher standard
* `churn_script_logging_and_tests.py` contains the accompanying tests for the project files
* `.pylintrc` contains the set of linter rules used to maintain the quality of the written code
* `requirements.txt` Python dependencies required to run project scripts
* Directories `data/`, `images/`, `logs/`, `models/` are as required to successfully run the project files

## Running Files

* Install required dependencies using the provided `requirements.txt` file
* Require data files, which can be found at [this link](https://www.kaggle.com/sakshigoyal7/credit-card-customers), should be saved as `./data/bank_data.csv`
* Run tests using `python churn_script_logging_and_tests.py`, output written to `.logs/churn_library.log/`
* Run main script to replicate original notebook: `python churn_library.py`, will write EDA, various plots, and model files to `./images/eda/`, `./images/results/`, and `./models/` respectively

