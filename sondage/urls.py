from django.urls import path
from django.contrib.auth.views import LoginView
from sondage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_question/', views.add_question, name='add_question'),
    path('question/<str:pk>', views.delete_question, name='delete_question'),
    path('success/<str:pk>', views.succefull, name='success'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views. register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('questionlist/', views.question_list, name='questionlist'),
    path('questionlist/<str:pk>', views.get_question, name='detail'),
    path('result/<str:pk>', views.result, name = 'result'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

