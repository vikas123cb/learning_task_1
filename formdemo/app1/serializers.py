from rest_framework import serializers
from .models import mcq_question,mcq_answer,true_false,true_false_answer
from django.contrib.auth.models import User

class UserSerialize(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['username','email']

# mcq
class mcq_question_serialize(serializers.ModelSerializer):
	class Meta:
		model=mcq_question
		fields=['id','question','op1','op2','op3','op4','is_mcq_question']

class mcq_answer_sserialize(serializers.ModelSerializer):
	class Meta:
		model=mcq_answer
		fields='__all__'


# bool
class true_false_serialize(serializers.ModelSerializer):
	class Meta:
		model=true_false
		fields='__all__'

class true_false_answer_serialize(serializers.ModelSerializer):
	class Meta:
		model=true_false_answer
		fields='__all__'


