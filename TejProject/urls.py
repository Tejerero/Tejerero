# from django.contrib import admin
# from django.urls import path
from django.contrib import admin
from django.urls import re_path as url
from flsys import views as flsys_views
from flsys import urls as flsys_urls
from django.conf.urls import include

urlpatterns = [
    url(r'^$', flsys_views.MainPage, name='viewlist'),
    url(r'^flsys/', include(flsys_urls)),
    url('admin/', admin.site.urls),

     #path('', views.MainPage, name='mainpage'),
    # url(r'^flsys/viewlist_url/$',views.ViewList, name='viewlist'),
    # url(r'^flsys/newlist_url/$', views.NewList, name='newList'),
    # url(r'^flsys/(\d+)/$', views.ViewList, name='viewList'),
    # url(r'^flsys/(\d+)/addList/$', views.AddList, name='addList'),
    #url('admin/', admin.site.urls),
    # url(r'^flsys/(\d+)/SchedPage/', views.SchedPage),
    # url(r'^flsys/(\d+)/CheckoutPage/', views.CheckoutPage),
    # url(r'^flsys/(\d+)/Scheduled_Classes/', views.Scheduled_Classes),

]
