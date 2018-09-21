from django.shortcuts import render,  get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Question
from rest_framework import generics
from .serializers import QuestionSerializer


class QuestionsList(generics.ListCreateAPIView):
    queryset = Question.objects.order_by('-id')[:5]
    serializer_class = QuestionSerializer


class QuestionsDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionSerializer

    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_pk'))



def index(request):

    latest_question_list = Question.objects.order_by('-id')[:5]

    context = {
        'latest_question_list': latest_question_list,
        'my_var': 4
    }
    
    return render(request, 'polls/index.html', context)

def detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

