# Aria: Plant Nutrition Prediction with Supervised Machine Learning
This project aims to built a Webapps to predict plant nutrition with 8 variable

# File Explanation on Github

Folder deployment = Contains files used for deployment to HuggingFace (contains models, python applications etc.)

aria.ipynb = This file is the main notebook used to explore dataset and built model

# Brief Summary of Project
The flow of this project, first EDA (Exploratory Data Analysis) to find out the basic picture of the dataset. Second, cleaning and preprocessing of the dataset. From preprocessing I dicided the data into 2 lab : lab 1 and lab 2 . Third, built and compare evaluation of 5 Model (Linear Regression, SVR ,  Random Forest Regresor, Elasticnet & Gausian Regresor) 

# Project Conclusion

## Data Analysis Summary:

The data obtained shows a diverse distribution, especially for v1 to v5, which is divided into two clusters.

Interesting differences exist between data from labs 1 and 2. Both data have the same target average value of around 4.7, but lab 1 has a lower standard deviation of 0.186, indicating less target variation compared to lab 2 with a standard deviation of 0.253.

The average values of the features between the two labs are quite different.

Model Performance Summary:

The model trained on the overall data has an error value of 0.16.
Separate models for data from Lab 1 and Lab 2 show improved performance with errors of 0.15 and 0.14, respectively.



Cannot predict outside the data range, because it uses a random forest algorithm
Time for testing and training is quite long because it uses bagging algorithm
Difficult to interpret why the model can predict plant nutrients to that number (different from linear regression which is easy to interpret)
