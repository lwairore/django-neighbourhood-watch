from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^new_profile/$', views.new_profile, name='new_profile'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)