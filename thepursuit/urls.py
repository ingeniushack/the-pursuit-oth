"""thepursuit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from oth import views as oth_views

urlpatterns = [
    url(r'^$',oth_views.index,name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^finish/',oth_views.finish,name="finish"),
    url(r'^play/',oth_views.play,name="play"),
    url(r'^level/(?P<level>\d+)$',oth_views.display_level,name="display_level"),
    url(r'^leaderboard/',oth_views.display_leaderboard,name="display_leaderboard"),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
