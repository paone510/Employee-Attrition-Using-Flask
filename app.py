from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('modell.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    BusinessTravel_Travel_Rarely=0
    Department_Sales=0
    MaritalStatus_Single=0
    JobRole_Laboratory_Technician=0
    JobRole_Manager=0
    if request.method == 'POST':

        #Age
        Age=float(request.form['Age'])

        #Department
        Department_Research_Development=request.form['Department_Research_Development']
        if(Department_Research_Development=='Research & Development'):
                Department_Research_Development=1
                Department_Sales=0
        elif(Department_Research_Development=='Sales'):
            Department_Research_Development=0
            Department_Sales=1
        else:
            Department_Research_Development=0
            Department_Sales=0

        #JobRole
        JobRole_Human_Resources=request.form['JobRole_Human_Resources']
        if(JobRole_Human_Resources=='Human_Resources'):
                JobRole_Human_Resources=1
                JobRole_Laboratory_Technician=0
                JobRole_Manager=0
                JobRole_Manufacturing_Director=0
                JobRole_Research_Director=0
                JobRole_Research_Scientist=0
                JobRole_Sales_Executive=0
                JobRole_Sales_Representative=0
        elif(JobRole_Human_Resources=='Laboratory_Technician'):
            JobRole_Human_Resources=0
            JobRole_Laboratory_Technician=1
            JobRole_Manager=0
            JobRole_Manufacturing_Director=0
            JobRole_Research_Director=0
            JobRole_Research_Scientist=0
            JobRole_Sales_Executive=0
            JobRole_Sales_Representative=0
        elif(JobRole_Human_Resources=='Manager'):
            JobRole_Human_Resources=0
            JobRole_Laboratory_Technician=0
            JobRole_Manager=1
            JobRole_Manufacturing_Director=0
            JobRole_Research_Director=0
            JobRole_Research_Scientist=0
            JobRole_Sales_Executive=0
            JobRole_Sales_Representative=0
        elif(JobRole_Human_Resources=='Manufacturing_Director'):
            JobRole_Human_Resources=0
            JobRole_Laboratory_Technician=0
            JobRole_Manager=0
            JobRole_Manufacturing_Director=1
            JobRole_Research_Director=0
            JobRole_Research_Scientist=0
            JobRole_Sales_Executive=0
            JobRole_Sales_Representative=0
        elif(JobRole_Human_Resources=='Research_Director'):
            JobRole_Human_Resources=0
            JobRole_Laboratory_Technician=0
            JobRole_Manager=0
            JobRole_Manufacturing_Director=0
            JobRole_Research_Director=1
            JobRole_Research_Scientist=0
            JobRole_Sales_Executive=0
            JobRole_Sales_Representative=0
        elif(JobRole_Human_Resources=='Research_Scientist'):
            JobRole_Human_Resources=0
            JobRole_Laboratory_Technician=0
            JobRole_Manager=0
            JobRole_Manufacturing_Director=0
            JobRole_Research_Director=0
            JobRole_Research_Scientist=1
            JobRole_Sales_Executive=0
            JobRole_Sales_Representative=0
        elif(JobRole_Human_Resources=='Sales_Executive'):
            JobRole_Human_Resources=0
            JobRole_Laboratory_Technician=0
            JobRole_Manager=0
            JobRole_Manufacturing_Director=0
            JobRole_Research_Director=0
            JobRole_Research_Scientist=0
            JobRole_Sales_Executive=1
            JobRole_Sales_Representative=0
        elif(JobRole_Human_Resources=='Sales_Representative'):
            JobRole_Human_Resources=0
            JobRole_Laboratory_Technician=0
            JobRole_Manager=0
            JobRole_Manufacturing_Director=0
            JobRole_Research_Director=0
            JobRole_Research_Scientist=0
            JobRole_Sales_Executive=0
            JobRole_Sales_Representative=1

        else:
            JobRole_Human_Resources=0
            JobRole_Laboratory_Technician=0
            JobRole_Manager=0
            JobRole_Manufacturing_Director=0
            JobRole_Research_Director=0
            JobRole_Research_Scientist=0
            JobRole_Sales_Executive=0
            JobRole_Sales_Representative=0

        #BusinessTravel
        BusinessTravel_Travel_Frequently=request.form['BusinessTravel_Travel_Frequently']
        if(BusinessTravel_Travel_Frequently=='Travel_Frequently'):
                BusinessTravel_Travel_Frequently=1
                BusinessTravel_Travel_Rarely=0
        elif(BusinessTravel_Travel_Frequently=='Travel_Rarely'):
            BusinessTravel_Travel_Frequently=0
            BusinessTravel_Travel_Rarely=1
        else:
            BusinessTravel_Travel_Frequently=0
            BusinessTravel_Travel_Rarely=0

        #MonthlyIncome
        MonthlyIncome=int(request.form['MonthlyIncome'])

        #PercentSalaryHike
        PercentSalaryHike=float(request.form['PercentSalaryHike'])

        #OverTime
        OverTime=request.form['OverTime']
        if(OverTime=='Yes'):
            OverTime=1
        else:
            OverTime=0

        #DistanceFromHome
        DistanceFromHome=float(request.form['DistanceFromHome'])

        #StockOptionLevel
        StockOptionLevel=int(request.form['StockOptionLevel'])

        #MaritalStatus
        MaritalStatus_Married=request.form['MaritalStatus_Married']
        if(MaritalStatus_Married=='Married'):
                MaritalStatus_Married=1
                MaritalStatus_Single=0
        elif(MaritalStatus_Married=='Single'):
            MaritalStatus_Married=0
            MaritalStatus_Single=1
        else:
            MaritalStatus_Married=0
            MaritalStatus_Single=0


        #TrainingTimesLastYear
        TrainingTimesLastYear=float(request.form['TrainingTimesLastYear'])

        #YearsSinceLastPromotion
        YearsSinceLastPromotion=float(request.form['YearsSinceLastPromotion'])

        #JobLevel
        JobLevel=float(request.form['JobLevel'])

        #YearsWithCurrManager
        YearsWithCurrManager=float(request.form['YearsWithCurrManager'])

        #Total_Satisfaction
        Total_Satisfaction=float(request.form['Total_Satisfaction'])

        prediction=model.predict([[Age,
                                    Department_Research_Development,
                                    Department_Sales,
                                    JobRole_Human_Resources,
                                    JobRole_Laboratory_Technician,
                                    JobRole_Manager,
                                    JobRole_Manufacturing_Director,
                                    JobRole_Research_Director,
                                    JobRole_Research_Scientist,
                                    JobRole_Sales_Executive,
                                    JobRole_Sales_Representative,
                                    BusinessTravel_Travel_Rarely,
                                    BusinessTravel_Travel_Frequently,
                                    MonthlyIncome,
                                    PercentSalaryHike,
                                    OverTime,
                                    DistanceFromHome,
                                    StockOptionLevel,
                                    MaritalStatus_Married,
                                    MaritalStatus_Single,
                                    TrainingTimesLastYear,
                                    YearsSinceLastPromotion,
                                    JobLevel,
                                    YearsWithCurrManager,
                                    Total_Satisfaction]])

        #output=prediction
        if prediction==1:
            return render_template('index.html',prediction_text="This employee likely to leave Company")
        else:
            return render_template('index.html',prediction_text="This employee will not leave the Company")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


#<center><b>Over Time</b> : <input type="radio" name="OverTime" id="Yes" value="Yes">Yes  <input type="radio" name="Over Time" id="No" value="No">No </center><br><br>
