from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('',views.collectioncatagory,name="collections"),
    path('search',views.search,name="search"),
    path('register',views.registers,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('about',views.about,name="about"),
    path('customerservice',views.customerservice,name="customerservice"),
    path('recommendation',views.recommend,name="recommend"),
    path('recent',views.add_to_recent,name="recent"),
    path('recentview',views.recentview,name="recentview"),
    path('remove_recent/<str:cid>',views.remove_recent,name="remove_recent"),
    path('order',views.add_to_order,name="order"),
    path('orderview',views.orderview,name="orderview"),
    path('remove_order/<str:cid>',views.remove_order,name="remove_order"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('cartview',views.cartview,name="cartview"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('favorite',views.add_to_favorite,name="favorite"),
    path('favoriteview',views.favoriteview,name="favoriteview"),
    path('remove_favorite/<str:cid>',views.remove_favorite,name="remove_favorite"),
    path('<str:name>',views.collectionsview,name="collectionsview"),
    path('<str:cname>/<str:pname>',views.productview,name="productview"),
    

]