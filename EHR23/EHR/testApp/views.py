from django.shortcuts import render

# Create your views here
def index(request):

    return render(request,'index.html',)

def Login(request):
    return render(request,'Login.html')

def Signup(request):
    return render(request,'SignUp.html')

def Disease_prediction(request):
    return render(request,'Disease_prediction.html')