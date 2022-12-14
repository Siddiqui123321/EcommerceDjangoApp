from django.urls import path
from security import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.handleLogin,name='handleLogin'),
    path('logout/',views.handleLogout,name='handleLogout'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    #path('activate/<uib64>/<token>/',views.ActivateAccountView.as_view(),name='activate'),
    
]
