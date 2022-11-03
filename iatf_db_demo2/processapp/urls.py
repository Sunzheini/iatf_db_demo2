from django.urls import path, include
from iatf_db_demo2.processapp.views import index, processes_description, overview, redirect_to

urlpatterns = (
    # http://127.0.0.1:8000/
    path('', index, name='index'),

    path('processes-description/', include([

        # http://127.0.0.1:8000/processes-description/
        path('', overview, name='overview'),
        # http://127.0.0.1:8000/processes-description/1
        path('<int:process_id>/', processes_description, name='show specific process'),
        # http://127.0.0.1:8000/processes-description/redirect/
        path('redirect/', redirect_to, name='redirect')
    ])),
)
