from django.conf.urls import url
from menu import views


app_name = 'menu'

urlpatterns = [
    url(r'^$',views.MenuListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.MenuDetailView.as_view(),name='detail'),
    url(r'^create/$',views.MenuCreateView.as_view(),name='create')    
]
