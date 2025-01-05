from django.urls import path
from . import views

app_name = 'stories'

urlpatterns = [
    path('create/', views.create_story, name='create_story'),
    path('view/', views.view_stories, name='view_stories'),
    path('my-stories/', views.my_stories, name='my_stories'),
    path('delete/<int:story_id>/', views.delete_story, name='delete_story'),
]
