from django.db import models
from django.contrib.auth.models import User
# Question Model

# mcq_type
class mcq_question(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.CharField(max_length=200)
	op1=models.CharField(max_length=100)
	op2=models.CharField(max_length=100)
	op3=models.CharField(max_length=100)
	op4=models.CharField(max_length=100)
	is_mcq_question=models.BooleanField(default=False)

class mcq_answer(models.Model):
	options = [
    ('A', 'op1'),
    ('B', 'op2'),
    ('C', 'op3'),
    ('D', 'op4'),
    ]		
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.ForeignKey(mcq_question,on_delete=models.CASCADE)
	answer=models.CharField(max_length=1,choices=options)

# bool_type
class true_false(models.Model):	
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.CharField(max_length=200)

class true_false_answer(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.ForeignKey(true_false,on_delete=models.CASCADE)
	answer=models.BooleanField(default=False)