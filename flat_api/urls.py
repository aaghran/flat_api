from django.conf.urls import include, url, patterns
from django.contrib import admin
from rest_framework import routers
from flat_api.views import UserDetail,UserAll,UserLoginView,logoutView,UserSignup

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/login/$',UserLoginView.as_view()),
    url(r'^user/logout/$',logoutView),
    url(r'^user/signup/$',UserSignup.as_view()),
    url(r'^user/$', UserAll.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
)