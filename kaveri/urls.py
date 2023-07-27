from django.urls import path


from kaveri.views import*
app_name='nothing'

urlpatterns=[
    path('kaveri1/',kaveri1,name='kaveri1'),
    path('kaveri2/',kaveri2,name='kaveri2'),
    path('kaveri3/',kaveri3,name='kaveri3'),
]