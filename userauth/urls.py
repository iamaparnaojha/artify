from django.contrib import admin
from django.urls import path
from socialmedia import settings
from userauth import views
from django.conf.urls.static import static
from django.contrib import admin

admin.site.site_header = "Social Media Admin Panel"
admin.site.site_title = "social media Admin"
admin.site.index_title = "Welcome to Social Media Admin Panel"

urlpatterns = [
    path('',views.home),
    path('loginn/',views.loginn),
    path('signup/',views.signup),
    path('logoutt/',views.logoutt),
    path('upload',views.upload),
    path('like-post/<str:id>', views.likes, name='like-post'),
    path('#<str:id>', views.home_post),
    path('explore',views.explore),
    path('profile/<str:id_user>', views.profile),
    path('delete/<str:id>', views.delete),
    path('search-results/', views.search_results, name='search_results'),
    path('follow', views.follow, name='follow'),
    path('upload-story/', views.upload_story, name='upload_story'),
]
