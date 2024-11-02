from django.urls import path
from .views import index, about, contact, service, read_more1, read_more2, read_more3

app_name = 'main'

urlpatterns = [
    path('', index, name='index_view'),
    path('home/', index, name='index_view'),
    path('about/', about, name='about_view'),
    path('sevrice/', service, name='service_view'),
    path('contact/', contact, name='contact_view'),
    path('read_more1/', read_more1, name='read_more1_view'),
    path('read_more2/', read_more2, name='read_more2_view'),
    path('read_more3/', read_more3, name='read_more3_view'),

]
