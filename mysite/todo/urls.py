from django.urls import path, include

from . import views

# appname = 'todo'

urlpatterns = [
    # path('/hello', views.hello, name='hello')
    path('/hello', views.hello, name='hello'),
    path('/bye-bye', views.byeBye, name='bye-bye')
]