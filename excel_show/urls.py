from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^upload$', views.index, name='index'),
    # url(r'^$', views.handle_uplosd, name='handle_upload'),
    url(r'^$', views.search_post),
]