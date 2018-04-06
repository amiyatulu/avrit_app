from django.urls import path, re_path
from tracking import views
from django.contrib.auth import views as auth_views

app_name = "tracking"

urlpatterns = [

    # path('',views.index, name='index'),
    path('home', views.home, name="home"),
    path('submission', views.postSubmission, name="submission"),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    re_path(r'^postview/(?P<pid>\d+)/$', views.postview, name="postview"),
    re_path(r'^ajaxcreatereview/(?P<pid>\d+)$',views.ajaxcreatereview, name="ajaxcreatereview"),
    re_path(r'^reviewpage/(?P<pid>\d+)$', views.reviewPage, name="reviewPage"),
    re_path(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

]
