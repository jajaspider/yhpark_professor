from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notice_write/', views.notice_write, name='notice_write'),
    url(r'^notice/', views.notice, name='notice'),
    url(r'^notice_datail/(?P<pk>\d+)/$', views.notice_datail, name='notice_datail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
