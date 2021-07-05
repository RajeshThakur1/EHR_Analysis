
from django.contrib import admin
from django.urls import path
from testApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='Home_Page'),
    path('prediction_page/',prediction_page,name='prediction_page'),
    path('login',Login,name='login'),
    path('signup',Signup,name='signup'),
    path('Disease_prediction',Disease_prediction,name='Disease_prediction')
]
