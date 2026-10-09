from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('reviews/', views.reviews, name='reviews'),
    path('regions/', views.regions, name='regions'),
    path('water/', views.water_climate, name='water_climate'),
    path('pest/', views.pest_tracker, name='pest_tracker'),
    path('yield/', views.yield_profit, name='yield_profit'),
    path('forum/', views.forum, name='forum'),
    path('upload/', views.upload, name='upload'),
    path('alerts/', views.alerts, name='alerts'),
    path('api/district/<str:district_name>/', views.district_detail, name='district_detail'),
    path('api/upvote/<int:review_id>/', views.upvote_review, name='upvote_review'),
]
