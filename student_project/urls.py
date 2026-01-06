"""
URL configuration for student_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from src.Lib.site-packages.pip._vendor.distro.distro import name
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.shortcuts import redirect


from student_project.settings import MEDIA_ROOT
from students.views import add_guardian, add_student, student_list, student_update, student_delete, register,student_detail
def home(request):
    return redirect('login')

urlpatterns = [
    path('',home,name='home')
    path('admin/', admin.site.urls),
    path('add/',add_student,name='add_student'),
 
    path('list/',student_list,name='student_list'),
    path('edit/<int:pk>/',student_update,name='update_student'),
    path('student/delete/<int:pk>/', student_delete, name='delete_student'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',register,name='register'),
    path('guardian/add/<int:student_id>/', add_guardian, name='add_guardian'),
    path('student/<int:pk>/', student_detail, name='student_detail'),
]

urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
