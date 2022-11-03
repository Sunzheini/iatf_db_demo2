from django.urls import path, include
from iatf_db_demo2.processapp.views import index, show_page_2

urlpatterns = (
    # http://127.0.0.1:8000/
    path('', index, name='index'),
    # http://127.0.0.1:8000/page2/
    path('page2/', show_page_2, name='show page 2'),
)
