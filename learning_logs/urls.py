'''Defines URL patterns for learning_logs'''
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'), 
    # Show all topics
    path('topics/', views.topics, name='topics'),
    # Show topic and all it's entries
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page to add a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page to add a new entry to a topic
    path('new_entry/<int:topic_id>/', views.new_entry, name="new_entry"),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
