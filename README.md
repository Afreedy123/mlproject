# Student Mathematics Score Prediction

## About the Project

This project is an end-to-end Machine Learning application that predicts a student's Mathematics score based on demographic and academic information.

The goal of this project was not only to build a prediction model but also to understand the complete Machine Learning workflow—from data preprocessing and model training to deploying the model using Flask.

## Features

* Predicts a student's Mathematics score
* Data preprocessing using Scikit-learn Pipelines
* Model training and evaluation
* Flask-based web application for real-time predictions
* Modular project structure for better code organization

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML
* CSS
* Bootstrap
* Git & GitHub

## Input Features

The model uses the following information to make predictions:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

**Output**

* Predicted Mathematics Score

## Project Structure

```text
Student-Mathematics-Score-Prediction/
│
├── artifacts/
├── notebook/
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/Afreedy123/Student-Mathematics-Score-Prediction.git
```

Move into the project folder:

```bash
cd Student-Mathematics-Score-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

## What I Learned

Building this project helped me gain practical experience in:

* Creating an end-to-end Machine Learning pipeline
* Data preprocessing and feature engineering
* Training and evaluating regression models
* Developing a web application using Flask
* Debugging real-world issues during deployment
* Using Git and GitHub for version control

## Future Improvements

Some improvements I would like to work on in the future:

* Deploy the application online
* Improve the user interface
* Add support for predicting additional exam scores
* Containerize the application using Docker

## Author

**Shahid Afreedy**

GitHub: https://github.com/Afreedy123

Thank you for taking the time to explore this project. Feedback and suggestions are always welcome.
