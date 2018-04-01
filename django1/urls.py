"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path
from controller import studentController
from controller import testController

urlpatterns = [
    path('api/test/test1', testController.test1, name='test1'),
    path('api/student/get', studentController.get, name='get'),
    path('api/student/getall', studentController.getall, name='getall'),
    path('api/student/getallpage', studentController.getallpage, name='getallpage'),
    path('api/student/add', studentController.add, name='add'),
    path('api/student/update', studentController.update, name='update'),
    path('api/student/delete', studentController.delete, name='delete'),
]
