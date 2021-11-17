# HR-Attrition using machine learning
This project is about HR department from IBM dataset, to predict the employee's attrition.

**Problem Statement:**

Managing peoples at workplace is one of the most important objective of an organization. Because, that will directly impact on efficiency, performance and most important the revenue of organization. That is why all the organizations strengthen their Human Recourse (HR) department. Any Improvement of HR department will have a positive impact on overall organization. 
The main goal is to predict the requirement of resources and whether the existing employee will resigned or not.

(https://user-images.githubusercontent.com/88028350/141747011-645be726-2ba7-44e5-ae06-6e252559c354.jpg)

**Project Structure**

This project has three major parts :

model.py - This python file has a machine learning model which we build to predict Employee Attrition from 'Hr-Attrition' Dataset .

app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.

templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee will leave the organization OR not.

**Prerequisites : **

Scikit Learn, Pandas, Flask, Heroku For Deployment.

**Run the project :**

1. Ensure that in promt you are connect to the project home directory, To change directory
   use below command-
   
   cd {project directory path} 

2. Run the model using below command(flask must be installed)- 
   
   Python app.py

3. Flask will run on default port 5000.
   
   Copy that link & paste in any browser & hit Enter!

4. Enter valid values in Application widgets & click on Predict button.
   
   You We Get The Result.  

**Application Demo Video on Local Envoriment:**


https://user-images.githubusercontent.com/88028350/138406396-b76bf2e7-9c23-49e8-a0af-af51686ec302.mp4

