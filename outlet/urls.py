from django.urls import path
from . import views

urlpatterns = [
    path('', views.newspart,name="newspart"),
    path('index/', views.index,name="index"),
    path('login/',views.signin, name='signin'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('signout/',views.signout, name='signout'),
    path('news/add/',views.news_add, name='news_add'),
    path('news/<int:pk>/edit',views.news_edit, name='news_edit'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='Search'),
    path('newsview/', views.productview, name='ProductView'),
    path('checkout/', views.checkout, name='CheckOut'),
]
