from django.urls import path,include
from . import views



app_name = 'quotes'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('signup/', views.signup, name='signup'),
    ]
urlpatterns += [
    path('', include('django.contrib.auth.urls')),
]