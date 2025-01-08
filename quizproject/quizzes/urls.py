from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_quiz_questions, name='quiz_list'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
]
