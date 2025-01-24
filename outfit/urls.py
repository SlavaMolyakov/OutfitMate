from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('choose-item/', views.wardrobe_welcome, name='wardrobe_welcome'),
    path('toggle_item/<int:item_id>/', views.toggle_item, name='toggle_item'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('toggle-favorite/<int:outfit_id>/', views.toggle_favorite, name='toggle-favorite'),
    path('favorite-outfits/', views.favorite_outfits, name='favorite_outfits'),
    path('login/', views.login_page_view, name='login_page_view'),
    path('register/', views.register_page_view, name='register_page_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
