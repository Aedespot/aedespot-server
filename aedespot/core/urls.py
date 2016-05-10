from django.conf.urls import url, include
from django.contrib import admin

from aedespot.core.api import router


urlpatterns = [
    url(r'^v1/', include(router.urls), name='api'),
]
