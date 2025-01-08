__[Link to project repo](https://github.com/M-arcy/deploying-scalable-Pipeline-with-FastAPI)__


Working in a command line environment is recommended for ease of use with git and dvc. If on Windows, WSL1 or 2 is recommended.

# Environment Set up (pip or conda)
* Option 1: use the supplied file `environment.yml` to create a new environment with conda
* Option 2: use the supplied file `requirements.txt` to create a new environment with pip
    
## Repositories
* Create a directory for the project and initialize git.
    * As you work on the code, continually commit changes. Trained models you want to use in production must be committed to GitHub.
* Connect your local git repo to GitHub.
* Setup GitHub Actions on your repo. You can use one of the pre-made GitHub Actions if at a minimum it runs pytest and flake8 on push and requires both to pass without error.
    * Make sure you set up the GitHub Action to have the same version of Python as you used in development.
    
     For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python



# Data
* Download census.csv and commit it to dvc.
* This data is messy, try to open it in pandas and see what you get.
* To clean it, use your favorite text editor to remove all spaces.

# Model
* Using the starter code, write a machine learning model that trains on the clean data and saves the model. Complete any function that has been started.
* Write unit tests for at least 3 functions in the model code.
* Write a function that outputs the performance of the model on slices of the data.
    * Suggestion: for simplicity, the function can just output the performance on slices of just the categorical features.
* Write a model card using the provided template.

# API Creation
*  Create a RESTful API using FastAPI this must implement:
    * GET on the root giving a welcome message.
    * POST that does model inference.




__[Link to project repo](https://github.com/M-arcy/deploying-scalable-Pipeline-with-FastAPI)__

This project builds a machine learning pipeline for predicting income levels based on census data and deploys a RESTful API using FastAPI. The project involves data preprocessing, model training, evaluation, and deployment.

# Environment Setup (pip or conda)
* Option 1: Use `environment.yml` with conda to create a new environment.
* Option 2: Use `requirements.txt` with pip to create a new environment.

# Repositories
* Create a directory for the project and initialize it as a git repository.
* Commit changes regularly, including trained models for production use.
* Connect the local git repository to GitHub.
* Set up GitHub Actions to run continuous integration (CI) tests using pytest and flake8.
    * Ensure the GitHub Actions workflow uses the same Python version as the development environment.
    * For more information, visit: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python.

# Data
* Download `census.csv` and track it with DVC (Data Version Control).
* The dataset may be messy; load it with pandas to inspect its contents.
* Clean the data by removing unnecessary spaces using a text editor or automated script.

# Model Development
* Complete the provided starter code to build a machine learning model:
  * Implement functions for training, inference, and saving/loading the model.
* Write at least three unit tests for the model functions.
* Implement a function that evaluates model performance on slices of categorical data, such as workclass or education.
* Document the model’s details, metrics, and ethical considerations using the provided model card template.

# API Creation
* Build a RESTful API using FastAPI with the following endpoints:
  * **GET** request on the root (`"/"`) that returns a welcome message.
  * **POST** request on the `/data/` path that performs model inference and returns predictions.
