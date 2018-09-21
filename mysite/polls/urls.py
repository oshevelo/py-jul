from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^question/$', views.QuestionsList.as_view(), name='question_list'),
    url(r'^question/(?P<question_pk>\d+)/$', views.QuestionsDetail.as_view(), name='question_list'),

    # ex: /polls/5/
    url(r'^(?P<question_pk>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
