from django.contrib import admin
from django.urls import path
from tasks.views import get_tasks, create_task, update_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', get_tasks),
    path('api/tasks/create/', create_task),
    path('api/tasks/<int:task_id>/update/', update_task),  #
]
