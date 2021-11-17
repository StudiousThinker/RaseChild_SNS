from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, ContributeCreate, ContributeDelete, ContributeUpdate, followfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('create/', ContributeCreate.as_view(), name='create'),
    path('delete/<int:pk>', ContributeDelete.as_view(), name='delete'),
    path('update/<int:pk>', ContributeUpdate.as_view(), name='update'),
    path('mylist/', listfunc, name='mylist'),
    path('follow/<int:pk>', followfunc, name='follow'),
]