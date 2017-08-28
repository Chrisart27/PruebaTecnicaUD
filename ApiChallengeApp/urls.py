from django.conf.urls import url
from ApiChallengeApp import views

urlpatterns = [
    url(r'^$', views.index, name='politic'),
    url(r'^candidates$', views.candidates, name='candidates'),
    url(r'^save-selection', views.save_selection, name='selection'),
]
