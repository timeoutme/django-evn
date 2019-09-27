"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from todo.views import to_do_lists, completed_lists, line,delete, edit, cexiao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',to_do_lists, name='待完成事项'),
    path('completed/>', completed_lists, name='已完成事项'),
    path('line/<item_id>',line,name='划掉'),
    path('delete/<item_id>',delete,name='删除'),
    path('edit/<item_id>',edit,name='修改'),
    path('cexiao/<item_id>',cexiao,name='撤销'),
]
