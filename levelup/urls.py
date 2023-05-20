"""
URL configuration for levelup project.

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
# ADD THESE Imports
from django.contrib import admin
from django.urls import path
from levelupapi.views import register_user, check_user
from django.conf.urls import include
from rest_framework import routers
from levelupapi.views import GameTypeView, GameView, EventView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'events', EventView, 'event')
router.register(r'games', GameView, 'game')

# ADD THESE LINES TO urlpatterns
urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
