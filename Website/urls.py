from django.urls import path
from . import views

app_name = 'Website'

urlpatterns = [
    path('',views.index,name="index"),
    path('reg/',views.reg,name="reg"),
    path('callforpaper/',views.callforpaper,name="callforpaper"),
    path('papersub/',views.papersub,name="papersub"),  
    path('acceptedpub/',views.acceptedpub,name="acceptedpub"),
    path('faqpost/', views.faq, name= "faqpost"),
    path('committee/', views.committee, name= "committee"),
    # path('update/', views.update, name= "update"),
    # path('<str:name>/',views.greet,name="greet"),  
]