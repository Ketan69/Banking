"""banking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login', views.login),
    path('delete', views.delete), 
    path('_delete', views._delete),
    path('new', views.new), 
    path('_new', views._new),
    path('block', views.block), 
    path('_block', views._block),
    path('send', views.send),
    path('_send', views._send),
    path('transaction', views.transaction),
    path('revert', views.revert),
    path('_revert', views._revert),
    path('__revert', views.__revert),
    path('change', views.change),
    path('_change', views._change),
]
