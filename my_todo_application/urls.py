from django.urls import path
from .views import (index, 
                    UserTaskDetailView, 
                    userdashboard, 
                    TaskCreateView, 
                    TaskUpdateView,
                    TaskDeleteView
)


urlpatterns = [
     path('', index, name = "index" ),
     path('task/<int:pk>/', UserTaskDetailView.as_view(), name="task-detail"),
     path('task/<int:pk>/update/', TaskUpdateView.as_view(), name="task-update"),
     path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name="task-delete"),
     path('task/new/', TaskCreateView.as_view(), name="task-create"),
     path('user-dashboard/', userdashboard, name="user_dashboard"),
 ]