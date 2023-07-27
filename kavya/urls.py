from django.urls import path


from kavya.views import*
app_name='nothing but'

urlpatterns=[
    path('kavya1/',kavya1,name='kavya1'),
    path('kavya2/',kavya2,name='kavya2'),
    path('kavya3/',kavya3,name='kavya3'),
]