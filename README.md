
# Insurance-Prediction-with-deployment
The main aim of this Machine learning project is to create a machine learning model and deploy it to predict 
the estimated cost the insurance policy with the certain inputs from the user like Age , BMI , No of children ,Smoker or not 
and the Gender.
We are going to create the Model  using sklearn library in the google colab environment and then deplying the model in the web app created using 
Flask in the HTML page.


We are using the Dataset which is available in Kaggle .( https://www.kaggle.com/mirichoi0218/insurance )
The dataset consist of Age , BMI , No of childrens, Gender , Smoker status , region and the insurance charge.
But for this project ,we  are going to negelect the regoin column as this dataset is particularly for the 
certain area but we are building the generalized model for the people across the golbe.

## This project consist of the following steps :
### 1. Creating the Model using python in Google-Colaboratory 

![image](https://user-images.githubusercontent.com/85100877/130967603-45a3a9ff-0653-47ee-bad8-82c4fe24ca23.png)

For this project , we are using the Google colabotary ( Colaboratory, or “Colab” for short, is a product from Google Research. Colab allows anybody to write and execute arbitrary python code through the browser, and is especially well suited to machine learning, data analysis and education.)
Google Colab provides us the virtual environment with automated setup with pre installed all the basic libraries along with 
the web hosted Memory and Disk-Space.
####       a.Importing the Libraries
All the various important libraries are imported like pandas , numpy , etc. 
And also some of the packages from the sklearn library . 

####       b. EDA and Data preprocessing 
This is one of the important part of the model building which helps to understand the data.
At first , we have drawn out some insights from the data using pandas library.
And then ,we install the dataprep library which is used for explotary data analysis and create the report using it. 

The prepared report is  at EDA report/report_from_dataprep.html 

And then, we remove the region column as above mentioned .
we encode the smoker and gender feature by one hot encoding using the get_dummies method of pandas .

And then we , split our whole dataset into 4 parts X_train, X_test ,y_train and y_test.
X part is independent variables and y part is dependent variable which is to be predicted.


#### c. Building the regression model using various algorithms like SVM , Random Forest and regression

And then , we build the different model using sklearn library and fit the training data..
We evaluate the performance of the 3 different algorithms( i.e. Linear Regression , Random Forest regressor and SVM )
Out of them Random forest have the better performance.

#### d. Hyperparameters Tuning and save the best model for us 

We use the GridSearchCV module  for the parameter tuning if the random forest.
By this , we get the model with better parameters and preformance relatively.
We save the model using pickle or joblib library with the .pkl extension


## 2. Depolyment using Flask

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

![image](https://user-images.githubusercontent.com/85100877/130965880-5aa20210-4968-4923-aa81-d481f10f7c6b.png)
We create the web app using flask and run it in our environment .
The web page after deployment looks like :
![deployed page](https://user-images.githubusercontent.com/85100877/131083851-bfc94265-3d53-47e1-ba31-57fcf399f886.PNG)
