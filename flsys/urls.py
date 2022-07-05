from django.contrib import admin
from django.urls import path
from flsys import views
from django.urls import re_path as url


urlpatterns = [
    url(r'^newlist_url/$', views.NewList, name='newList'),
    url(r'^(\d+)/$', views.ViewList, name='viewList'),
    url(r'^(\d+)/addList/$', views.AddList, name='addList'),
    url(r'^(\d+)/SchedPage/', views.SchedPage, name='SchedPage'),
    url(r'^(\d+)/CheckoutPage/', views.CheckoutPage, name='CheckoutPage'),
    url(r'^(\d+)/Review/', views.Review, name='Review'),
    url(r'^None/Review/', views.Review2, name='Review2'),
    url(r'^(\d+)/edit/', views.edit, name='edit'),
    url(r'^edit/update/(\d+)', views.update, name='update'),
    url(r'^(\d+)/delete/', views.delete, name='delete'),

    # path('delete/<int:id/', views.delete),
    # path('edit/<int:id/', views.edit),
    path('HomePage/', views.Home),
    path('CookingClass/', views.MainPage),
    path('ContactUs/', views.ContactUs),
    path('Recipes/', views.Recipes),
    path('Breakfast/', views.Breakfast),
    path('BreakfastPancakes/', views.BreakfastPancakes),
    path('BreakfastGarlicRice/', views.BreakfastGarlicRice),
    path('BreakfastFrenchToast/', views.BreakfastFrenchToast),
    path('ChickenAdobo/', views.ChickenAdobo),
    path('FilipinoSpringRolls/', views.FilipinoSpringRolls),
    path('ChickenAfritada/', views.ChickenAfritada),
    path('HomemadeDonuts/', views.HomemadeDonuts),
    path('Muffins/', views.Muffins),
    path('Cupcakes/', views.Cupcakes),
    path('Sandwiches/', views.Sandwiches),
    path('Salad/', views.Salad),
    path('Pinakbet/', views.Pinakbet),
    path('Mains/', views.Mains),
    path('Sweets/', views.Sweets),
    path('Healthy/', views.Healthy),
    path('RatePancake/', views.RatePancake),
    url(r'^deleteRating/(?P<id>\d+)$', views.deleteRating, name='deleteRating'),
    url(r'^editRating/(?P<id>\d+)$', views.editRating, name='editRating'),
    url(r'^editRating/updateRating/(?P<id>\d+)$', views.updateRating, name='updateRating'),




    #path('Scheduled_Classes/', views.Scheduled_Classes),

    

    #path('admin/', admin.site.urls),
    # path('', views.MainPage, name='mainpage'),
    #url(r'^viewlist_url/$',views.ViewList, name='viewlist'),

]
