from .views import Postlist,PostCrate,Postruda
from django.urls import path
urlpatterns=[
    path('',Postlist.as_view(),name='apilist'),
    path('crate/',PostCrate.as_view(),name='crate'),
    path('ruda<int:pk>/',Postruda.as_view(),name='ruda')
]