from django.urls import path

from . import views
app_name = 'pages'
urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.category_posts, name='category_posts')
]