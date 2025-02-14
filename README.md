# IMDB-Movie-Classifier
## Description
A binary classifier for IMDB movies using various machine learning techniques :
- Logistic Regression
- Support Vector Machine
- Random Forest
- K-Nearest Neighbours

#### Notes 
* Logistic Regression and Support Vector Machine are implemented using both Scikit-learn and from scratch.

* Evaluation metrics, performances for all classifiers are included in the project report.

* This project is done collaboratively with Nazlıcan Aka and Dağlar Eren Tekşen for CMPE462 - Machine Learning course at Bogazici University.


## Execution
- We have provided the code file for fetching the movies data from the OMDB API in the fetch_data.py.

- Note : Please make sure that query.csv (includes the results of the Wikidata SPARQL Query) and film_responses.json (which will include the fetched movies data) are located in the same folder with the fetch_data.py

- This file can be executed by the following command:

> python fetch_data.py

- After these steps, we have uploaded film_responses.json file to the Google Colab environment then run the 2 notebooks within Google Colab,all the feature extraction, data preprocessing, model implementations (task 1 and 2 ) are located in the 462_project.ipynb

- The evaluation metrics for the models and plotting the decision boundary (task 3 ) implementations are located in evaluation_plot.ipynb

- These notebooks can be executed in the Google Colab environment to reproduce the results.

