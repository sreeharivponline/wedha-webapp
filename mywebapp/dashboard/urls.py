from django.urls import path
from . import views
from django.urls import path
from .views import chatbot_api



urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Main dashboard
    path('what-we-do/', views.what_we_do, name='what_we_do'),  # What We Do page
    path('help/', views.help, name='help'),  # Help page
    path('join-us/', views.join_us, name='join_us'),  # Join Us page
    path('issues-we-work-on/', views.issues_we_work_on, name='issues_we_work_on'),  # Issues We Work On page
    path('quiz/', views.quiz, name='quiz'),  # Quiz page
    path('contribute/', views.contribute, name='contribute'),  # Contribute page
    path('login/', views.login_view, name='login'),  # Login page
    path('chatbot/', views.chatbot_api, name='chatbot_api'),

]
