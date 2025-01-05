from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('conversation/<int:user_id>/', views.conversation, name='conversation'),
    path('get-messages/<int:conversation_id>/', views.get_messages, name='get_messages'),
    path('search-users/', views.search_users, name='search_users'),
]
