from oracle_app.views import index
from django.urls import path

app_name = 'oracle_app'
urlpatterns = [
    path('',index, name='index'),
]