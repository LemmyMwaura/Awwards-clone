from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit_project/', views.submit_project, name='submit-project'),

    path('login/', views.login_page, name='login'),
    path('register/', views.register_user, name='register'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('project/<str:pk>/', views.project_page, name='project'),
    path('add_rating/<str:pk>/', views.add_ratings, name='add-rating'),

    path('api/all_profiles/', views.ProfilesList.as_view(), name='api-profiles'),
    path('api/all_projects/', views.ProjectList.as_view(), name='api-projects'),
    path('api/all_users/', views.UsersList.as_view(), name='api-users')
]