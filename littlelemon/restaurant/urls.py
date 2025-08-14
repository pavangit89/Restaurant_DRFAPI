from django.urls import path, include
from . import views

urlpatterns = [
    # static page
    path('', views.index, name='index'),   
    path('about', views.about, name='about'),   
    

    # api

    # show menuitems
    path('api/menu/', views.MenuItemsView.as_view(),name='menu'),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view(),name='menu_item'),

    # bookings
    path('api/book/', views.BookingView.as_view()),
    path('api/book/<int:pk>', views.SingleBookingView.as_view()),

    # user managements
    path('auth/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
]