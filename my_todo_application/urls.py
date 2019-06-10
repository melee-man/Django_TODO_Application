from django.urls import path
from .views import index, UserTaskDetailView, userdashboard


urlpatterns = [
     path('', index, name = "index" ),
     path('task/<int:pk>/', UserTaskDetailView.as_view(), name="task-detail"),
     path('user-dashboard/', userdashboard, name="user_dashboard"),
 ]