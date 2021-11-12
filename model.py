# Importing the libraries and Dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

data = pd.read_csv(r"C:/Users/pavan/OneDrive/Desktop/final deploy/HR-Attrition.csv")
data.columns

# drop the unnecessary columns
data.drop (['EmployeeNumber','Over18','StandardHours','EmployeeCount',
            'DailyRate','Education','EducationField','Gender','YearsInCurrentRole',
            'YearsAtCompany','HourlyRate','MonthlyRate','PerformanceRating','TotalWorkingYears'],axis=1,inplace=True)

# 'Environment Satisfaction', 'JobInvolvement', 'JobSatisfaction', 'RelationshipSatisfaction', 'WorklifeBalance' can
# be clubbed into a single feature 'TotalSatisfaction'
data['Total_Satisfaction'] = (data['EnvironmentSatisfaction'] +
                            data['JobInvolvement'] +
                            data['JobSatisfaction'] +
                            data['RelationshipSatisfaction'] +
                            data['WorkLifeBalance']) / 5

# Drop Columns
data.drop (['EnvironmentSatisfaction','JobInvolvement','JobSatisfaction',
            'RelationshipSatisfaction','WorkLifeBalance'], axis=1, inplace=True)

data.drop(['NumCompaniesWorked'], axis=1,inplace=True)

data=data[['Attrition','Age','Department','JobRole','BusinessTravel','MonthlyIncome','PercentSalaryHike',
           'OverTime','DistanceFromHome','StockOptionLevel','MaritalStatus','TrainingTimesLastYear',
           'YearsSinceLastPromotion','JobLevel','YearsWithCurrManager','Total_Satisfaction']]

data['Attrition'] = data['Attrition'].apply (lambda x: 1 if x == "Yes" else 0)
data['OverTime'] = data['OverTime'].apply (lambda x: 1 if x == "Yes" else 0)

data=pd.get_dummies(data,drop_first=True)

X = data.iloc[:, 1:]
Y = data.iloc[:, 0]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 123)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(5, 30, num = 6)]
# max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10, 15, 100]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 5, 10]

# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf}

print(random_grid)

#Initilized the RandomForestClassifier
rfc = RandomForestClassifier()

# search across 100 different combinations
rfc_random = RandomizedSearchCV(estimator = rfc, param_distributions = random_grid, n_iter = 10, cv = 5, verbose=2, random_state=42, n_jobs = 1)

rfc_random.fit(X_train, Y_train)

rfc_random.best_params_


#Classification accuracy is the ratio of correct predictions to total predictions made.
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


cm = confusion_matrix(Y_test, rfc_random.predict(X_test), labels=rfc_random.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=rfc_random.classes_)
disp.plot()
plt.show()

cm1 = confusion_matrix(Y_test, rfc_random.predict(X_test))
  
TN = cm1[0][0]
TP = cm1[1][1]
FN = cm1[1][0]
FP = cm1[0][1]
  
print(cm1)
print('Model Testing Accuracy = "{}!"'.format(  (TP + TN) / (TP + TN + FN + FP)))


#Training accuracy
cm2 = confusion_matrix(Y_train, rfc_random.predict(X_train))

TN = cm2[0][0]
TP = cm2[1][1]
FN = cm2[1][0]
FP = cm2[0][1]
  
print(cm2)
print('Model Training Accuracy = "{}!"'.format(  (TP + TN) / (TP + TN + FN + FP)))

pickle.dump(rfc_random, open('modell.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('modell.pkl','rb'))



# # Change Factors to Numerics
# df['Attrition'] = df['Attrition'].apply (lambda x: 1 if x == "Yes" else 0)
# df['OverTime'] = df['OverTime'].apply (lambda x: 1 if x == "Yes" else 0)


