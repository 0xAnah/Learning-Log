"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_log'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics
    path("topics/", views.topics, name="topics"),
    # Page that shows the individual topic entry
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry 
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
]