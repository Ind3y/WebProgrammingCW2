"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import tasks_api, task_api, create_task_api, update_task_api, create_step_api, step_api


urlpatterns = [
    # API entry points should be defined here
    path('tasks/', tasks_api, name='tasks_api'),
    path('tasks/<int:task_id>/', task_api, name='task_api'),
    path('tasks/update/<int:task_id>/', update_task_api, name='update_task_api'),
    path('tasks/create/', create_task_api, name='create_task_api'),
    path('tasks/<int:task_id>/steps/', create_step_api, name='create_step_api'),
    path('steps/<int:step_id>/', step_api, name='step_api'),
]
