from django.urls import include, path
from . import views

app_name = 'announcements'

urlpatterns = [
    path('page1/', views.pagen1, name='first_page'),
    path('page2/', views.pagen2, name='second_page'),
    path('disable/', views.disable_ann, name='disable_ann'),
]