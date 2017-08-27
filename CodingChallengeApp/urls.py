from django.conf.urls import url
from CodingChallengeApp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^check-str-count$', views.check_str_count, name='check-str'),
]
