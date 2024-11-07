from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('collections',views.collections,name="collections"),
    path('collections/<str:name>/',views.collectionsview,name='collections'),
    path('collections/<str:cname>/<str:pname>/',views.product_details,name='product_details'),
]


#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