from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [ 
    path('signup',views.signup,name='signup'),
    path('login',views.userlogin,name='login'),
    path('logout',views.userlogout,name='logout'),
    path('profile',views.Profile,name='profile'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('changepassword2',views.changepassword2,name='changepassword2'),
]