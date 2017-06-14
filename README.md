# Springboard Data Science Mini-Projects

Welcome! This repository contains my data science mini-projects, ranging from data wrangling and statistical inference to machine learning and data visualization.


### Machine Learning

**[Linear Regression with Boston Housing Dataset](https://github.com/andrewjsiu/Springboard-Coursework/blob/master/Machine_Learning_Exercises/linear_regression/Mini_Project_Linear_Regression.ipynb):** I use `scikit-learn` library to build a linear regression model to predict the housing prices in Boston. The various features include per capita crime rate, average number of rooms per dwelling, and pupil-teacher ratio by town. I also split the data into training and testing sets in order to measure how well the model built with the training set can predict the 'unseen' data in the test set. I show how multiple rounds of cross-validation performed on different partitions help limit the problem of overfitting a particular training subset and thus reduce variability of the model.

**[Classification and Logistic Regression](https://github.com/andrewjsiu/Springboard-Coursework/blob/master/Machine_Learning_Exercises/logistic_regression/Mini_Project_Logistic_Regression.ipynb):** I use cross-validation and grid search to find the best regularization parameter **C** for the logistic regression. Regularization applies a penalty for increasing the coefficient estimates in order to reduce overfitting. The regularization parameter **C** in `scikit-learn` is the inverse of the shrinkage parameter lambda. Larger lambda or smaller **C** increases the shrinkage pentalty and shrinks the coefficient estimates toward zero. By default scikit-learn sets **C**=1 in logistic regression, so some amount of regularization is used even if **C** is not specified. Regularization is good at reducing the variance of the predictions but increasing the bias at the same time. `GridSearchCV` performs a cross-validated grid-search over a parameter grid. We need to specify an estimation method, parameter values for the estimator and a scoring method. The results show the best estimator, the score of the best estimator, and the parameter setting that yields the best score.

### Advance Machine Learning Topics


### Data Wrangling

**[JSON Exercises](https://github.com/andrewjsiu/Springboard-Coursework/blob/master/Data_Wrangling/data_wrangling_json/json_exercise.ipynb):** The dataset on the World Bank projects is available in a JSON file. I first load the data as a Pandas dataframe and find that China, Indonesia and Vietnam have the most projects with the World Bank. Then I load the JSON file as a string, normalize the project themes, and find that environment and natural resources management, rural development and human development are the project themes with the highest frequencies. 

**[XML Exercises](https://github.com/andrewjsiu/Springboard-Coursework/blob/master/Data_Wrangling/data_wrangling_xml/xml_exercise.ipynb):** The Mondial database contains geographical terrains and various physical features in the world. I use `xml.etree.ElementTree` module to parse the data, which are stored as elements in a hierarchical structure. Each element has a tag, a number of attributes, a text string, and a number of child elements. I find that (1) Monaco, Japan and Bermuda have the lowest infant morality rate; (2) Shanghai, Istanbul and Mumbai have the largest city population; (3) Han Chinese, Europeans and Indo-Aryan are ethnic groups with the largest overall population, and (4) the longest river in the world is Amazonas, the largest lake is Caspian Sea, and the airport at the highest elevation is El Alto International. 

### Exploratory Data Analysis

**[Human Body Temperature](https://github.com/andrewjsiu/Springboard-Coursework/blob/master/Exploratory_Data_Analysis/data_human_temperature/inferential_statistics_exercise_1_human_temperatures.ipynb):** 
I analyze a dataset of human body temperatures and test whether the true average temperature is 98.6 degrees F. As women have a higher average temperature than men, I also test whether there is such gender difference in temperature.   

