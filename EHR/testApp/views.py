# from django.http.request import HttpRequest
from django.shortcuts import render
import os
import yaml
import joblib
import numpy as np

params_path = "params.yaml"
webapp_root = "webapp"

def index(request):
    return render(request,'index.html')


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def predict(data):
    config = read_params(params_path)
    model_dir_path = config['webapp_model_dir']
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    # print("tttt")
    # print(prediction[0])
    # print(type(prediction[0]))
    return str(prediction[0])



def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response":response}
        return response
    except Exception as e:
        print(e)
        error= {"error": "something went wrong!!! Try again"}
        return error



# Create your views here

def prediction_page(request):
    response=None
    dict ={}
    if request.method=="POST":
        dict['Age'] = request.POST['Age'] 
        dict['Gender'] = request.POST['Gender']  
        dict['RespiratoryRate_Max'] = request.POST['RespiratoryRate_Max']  
        dict['Temperature_Max'] = request.POST['Temperature_Max']  
        dict['RespiratoryRate_Min'] = request.POST['RespiratoryRate_Min']  
        dict['DiastolicBP_Std'] = request.POST['DiastolicBP_Std']  
        dict['BMI_Mean'] = request.POST['BMI_Mean']  
        dict['RespiratoryRate_Mean'] = request.POST['RespiratoryRate_Mean']  
        dict['Temperature_Mean'] = request.POST['Temperature_Mean']  
        dict['BMI_Change'] = request.POST['BMI_Change']  
        dict['DiastolicBP_Change'] = request.POST['DiastolicBP_Change']  
        dict['Height_Change'] = request.POST['Height_Change']  
        dict['RespiratoryRate_Change'] = request.POST['RespiratoryRate_Change']  
        dict['SystolicBP_Change'] = request.POST['SystolicBP_Change']  
        dict['Temperature_Change'] = request.POST['Temperature_Change']  
        dict['Weight_Change'] = request.POST['Weight_Change']
        data = dict.values()
        data = [list(map(float, data))]
        response = predict(data)
    return render(request,'prediction_page.html',{"response":response})

def Login(request):
    return render(request,'Login.html')

def Signup(request):
    return render(request,'SignUp.html')

def Disease_prediction(request):
    return render(request,'Disease_prediction.html')