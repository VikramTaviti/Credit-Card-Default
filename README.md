heroku app link :
[click here](https://credit-card-default11.herokuapp.com/)

dataset link:
[click here](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)


This dataset contains information on default payments, demographic factors, credit data, history of payment and bill statements of credit card clients in Taiwan from April 2005 to September 2005.

Attribute Information:

This research employed a binary variable, default payment (Yes = 1, No = 0), as the response variable. This study reviewed the literature and used the following 23 variables as explanatory variables:

X1: Amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit.

X2: Gender (1 = male; 2 = female).

X3: Education (1 = graduate school; 2 = university; 3 = high school; 4 = others).

X4: Marital status (1 = married; 2 = single; 3 = others).

X5: Age (year).

X6 - X11: History of past payment. We tracked the past monthly payment records (from April to September, 2005) as follows: X6 = the repayment status in September, 2005; X7 = the repayment status in August, 2005; . . .;X11 = the repayment status in April, 2005. The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above.

X12-X17: Amount of bill statement (NT dollar). X12 = amount of bill statement in September, 2005; X13 = amount of bill statement in August, 2005; . . .; X17 = amount of bill statement in April, 2005.

X18-X23: Amount of previous payment (NT dollar). X18 = amount paid in September, 2005; X19 = amount paid in August, 2005; . . .;X23 = amount paid in April, 2005.

Approach : Applying machine learing tasks like Data Exploration, Data Cleaning, Feature Engineering, Model Building and model testing to build a solution that be should able to predict whether the customer will be defaulter in the next month.

Data Exploration : Exploring the dataset using pandas, numpy, matplotlib and seaborn.

Exploratory Data Analysis : Plotted different graphs to get more insights about dependent and independent variables/features.

Feature Engineering : Numerical features scaled down and Categorical features encoded.

Model Building : In this step, first dataset Splitting is done. After that model is trained on different Machine Learning Algorithms such as:

Logistic Regression

Decision Tree Classifier

Gradient Boosting Classifier

Random Forest Classifier

Model Selection : Tested all the models to check the precision, recall and Cross Validation accuracy Score.

Pickle File : Selected model as per best precision, recall and Cross Validation accuracy Score and created pickle file using pickle library.

Webpage and Deployment : Created a web application that takes all the necessary inputs from the user & shows the output. Then deployed project on the Heroku Platform.
