from rest_framework import serializers
from apps.polls.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']
