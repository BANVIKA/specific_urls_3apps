from django.urls import path





from kamakshi.views import* 
app_name='something'


urlpatterns=[
    path('kamakshi1/',kamakshi1,name='kamakshi1'),
    path('kamakshi2/',kamakshi2,name='kamakshi2'),
    path('kamakshi3/',kamakshi3,name='kamakshi3'),
]