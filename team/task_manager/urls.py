from django.urls import path
from task_manager import views


urlpartterns = [
    path('tasks/', views.TaskListViewset.as_view({'post' : 'create', 'get' : 'list'})),
    path('tasks/<int:pk>/', views.TaskDetaialViewset.as_view( {  
                "get": "retrieve",
                "put": 'update',
                "patch": 'partial_update',
                "delete": "destroy"
            }
        )
    ),
]