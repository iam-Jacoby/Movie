"""Movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work.views import RegisterView,SignIn,GenreList,GenreView,GenreDelete,GenreUpdate,MovieView,MovieList,MovieDelete,MovieUpdate,Signout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regist/',RegisterView.as_view(),name="regist"),
    path('',SignIn.as_view(),name="login"),
    path('addg/',GenreView.as_view(),name="addg"),
    path('addm/',MovieView.as_view(),name="addm"),
    path('Glist/',GenreList.as_view(),name="genrelist"),
    path('Glist/<int:pk>/remove',GenreDelete.as_view(),name="delgenre"),
    path('Glist/<int:pk>/update',GenreUpdate.as_view(),name="updtgenre"),
    path('Mlist/',MovieList.as_view(),name="movielist"),
    path('Mlist/<int:pk>/remove',MovieDelete.as_view(),name="delmovie"),
    path('Mlist/<int:pk>/update',MovieUpdate.as_view(),name="updtmovie"),
    path('logout/',Signout.as_view(),name="signout"),
    
]
