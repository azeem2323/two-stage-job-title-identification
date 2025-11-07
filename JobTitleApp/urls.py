from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('UserLogin.html', views.UserLogin, name="UserLogin"), 
	       path('LoginAction', views.LoginAction, name="LoginAction"),
	       path('Predict.html', views.Predict, name="Predict"),
	       path('PredictAction', views.PredictAction, name="PredictAction"),
	       ]