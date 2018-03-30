from django.urls import path, re_path
from tracking import views

app_name = "tracking"

urlpatterns = [

    # path('',views.index, name='index'),
    path('submission', views.postSubmission, name="submission"),
    re_path(r'^postview/(?P<pid>\d+)/$', views.postview, name="postview"),
    re_path(r'^ajaxcreatereview/(?P<pid>\d+)$',views.ajaxcreatereview, name="ajaxcreatereview"),
    re_path(r'^reviewpage/(?P<pid>\d+)$', views.reviewPage, name="reviewPage")

]
