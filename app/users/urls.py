from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('predmeti/', views.predmetiPage, name="predmeti"),
    path('korisnik/<int:pk_test>/', views.korisnikPage, name="korisnik"),
    path('',views.homePage,name='home'),
]
