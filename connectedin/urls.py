"""connectedin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from perfil import views as views_perfil
from usuario.views import RegistrarUsuarioView
from django.contrib.auth import views as views_user
from timeline import views as views_timeline

urlpatterns = [
    # Perfil.views
    path('admin/', admin.site.urls),
    path('', views_perfil.index, name='index'),
    path('perfil/<int:perfil_id>',
    				views_perfil.exibir, name='exibir'),
    path('perfil/<int:perfil_id>/convidar',
    				views_perfil.convidar, name='convidar'),
    path('perfil/<int:convite_id>/aceitar',
                    views_perfil.aceitar, name='aceitar'),
    path('perfil/<int:convite_id>/rejeitar',
                    views_perfil.rejeitar, name='rejeitar'),

    # Usuario.views
    path('registrar/', RegistrarUsuarioView.as_view(),
                    name='registrar'),
    path('login/', views_user.LoginView.as_view(template_name='usuario/login.html'),
                    name='login'),
    path('logout/', views_user.LogoutView.as_view(template_name='usuario/login.html'),
                    name='logout'),

    # Timeline.views
    path('timeline/add_post', views_timeline.add_post, name='add_post'),
]
