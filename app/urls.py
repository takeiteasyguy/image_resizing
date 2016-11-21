from django.conf.urls import url
from django.views.static import serve
from app.views import ImageDetail, ImageList, MainTemplateView
from app import settings


urlpatterns = [
    url(r'^$', MainTemplateView.as_view(), name='main_page'),
    url(r'^api/image/$', ImageList.as_view(), name='image_list'),
    url(r'^api/image/(?P<pk>[0-9]+)/$', ImageDetail.as_view(), name='image_detail'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
