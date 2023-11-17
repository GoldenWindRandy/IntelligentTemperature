from django.urls import path,include
from Login import views



urlpatterns = [
    path('userlist/', views.user_list.as_view()),
    path('login/', views.login_view),
    path('register/', views.Register),
    # path('userinfo/<int:pk>/', views.UserView.as_view()),
    path('user/<int:pk>/', views.user_detail.as_view()),
]