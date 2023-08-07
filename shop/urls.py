from django.urls import path,include
from .import views
app_name='shop'
urlpatterns = [


    path('',views.allpro,name="allpro"),
    path('<slug:c_slug>/',views.allpro,name='pro_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prod,name='prod'),


]