from django.urls import path
from team_manager import views
from rest_framework.routers import SimpleRouter, DefaultRouter

# router = DefaultRouter()
# router.register('projects', views.pr)

urlpartterns = [
    path('teams/', views.TeamListViewset.as_view({'post' : 'create', 'get' : 'list'})),
    path('teams/<int:pk>/', views.TeamDetaialViewset.as_view( {  
                "get": "retrieve",
                "put": 'update',
                "patch": 'partial_update',
                "delete": "destroy"
            }
        )
    ),
    path('projects/', views.ProjectListViewset.as_view({'post' : 'create', 'get' : 'list'})),
    path('projects/<int:pk>/', views.ProjectDetailstViewset.as_view( {  
                "get": "retrieve",
                "put": 'update',
                "patch": 'partial_update',
                "delete": "destroy"
            }
        )
    ),

]


# urlpartterns =  router.urls