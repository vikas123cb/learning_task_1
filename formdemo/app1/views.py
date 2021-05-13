from django.shortcuts import render
from rest_framework.serializers import Serializer

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
 # quention and answer

from .models import mcq_question, mcq_answer , true_false, true_false_answer
from .serializers import UserSerialize,mcq_question_serialize,mcq_answer_sserialize,true_false_serialize,true_false_answer_serialize   
from rest_framework import viewsets
from rest_framework import status





# mcq_views
class mcq_question_view(APIView):

 def post(self,request):
		if request.user.is_authenticated:
			question=self.request.data.get('question')
			op1=self.request.data.get('op1')
			op2=self.request.data.get('op2')
			op3=self.request.data.get('op3')
			op4=self.request.data.get('op4')			
			is_mcq_question=False
			try:
				is_mcq_question=self.request.data.get('is_mcq_question')
			except:
				is_mcq_question=False
			data=mcq_question(user=request.user,question=question,op1=op1,op2=op2,op3=op3,op4=op4,is_mcq_question=is_mcq_question)
			data.save()
			serializer_data=mcq_question_serialize(data)
			return Response(serializer_data.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)
 

 def get(self,request):
		if request.user.is_authenticated:
			try:
				creater=self.request.GET.get("creater")
				user=User.objects.get(username=creater)
				q=mcq_question.objects.filter(user=user)
			except:
				return Response({"error":"creater not exits"},status=status.HTTP_400_BAD_REQUEST)
			ser=mcq_question_serialize(q,many=True)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

 def delete(self,request):
		if request.user.is_authenticated:
			all_questions=mcq_question.objects.filter(user=request.user)
			for i in all_questions:
				i.delete()
			return Response({"success":"all question deleted"})
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)       


#  unique_id_question
class single_mcq_question_view(APIView):
	def get(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				data=mcq_question.objects.get(id=id)
			except:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			serializer_data=mcq_question_serialize(data)
			return Response(serializer_data.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:			
				data=mcq_question.objects.get(id=id)				
				data.delete()
				return Response()
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def patch(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				data=mcq_question.objects.get(id=id)
				if "question" in self.request.data:
					data.question=self.request.data.get('question')
				if "op1" in self.request.data:
					data.op1=self.request.data.get('op1')
				if 'op2' in self.request.data:
					data.op2=self.request.data.get('op2')
				if "op3" in self.request.data:
					data.op3=self.request.data.get('op3')
				if 'op4' in self.request.data:
					data.op4=self.request.data.get('op4')
				if 'is_mcq_question' in self.request.data:
					data.is_mcq_question=self.request.data.get('is_mcq_question')
				data.save()
				serializer_data=mcq_question_serialize(data)
				return Response(serializer_data.data)
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)

# ------------- true_false


class true_false_question_view(APIView):
	
	def get(self,request):
		if request.user.is_authenticated:
			try:
				creater=self.request.GET.get("creater")
				user=User.objects.get(username=creater)
				data=true_false.objects.filter(user=user)
			except:
				return Response({"error":"creater not exits"},status=status.HTTP_400_BAD_REQUEST)
			seserializer_data=true_false_serialize(data,many=True)
			return Response(seserializer_data.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def post(self,request):
		if request.user.is_authenticated:
			questions=self.request.data
			if 'question' not in questions:
				return Response({"error":"provide question and all options"},status=status.HTTP_400_BAD_REQUEST)			
			q=true_false(user=request.user,question=questions['question'])
			q.save()
			data=true_false_serialize(q)
			return Response(data.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request):
		if request.user.is_authenticated:
			queston=true_false.objects.filter(user=request.user)
			for i in queston:
				i.delete()
			return Response({"success":"all question deleted"})
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)


# ------------------
class single_tf_question_view(APIView):
	def get(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				p=true_false.objects.get(id=id)
			except:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			ser=true_false_serialize(p)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:			
				q=true_false.objects.get(id=id)
				q.delete()
				return Response()
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def patch(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=true_false.objects.get(id=id)
				if q.user!=request.user:
					return Response({"error":"you are not the crator of this question so you cant do this"},status=status.HTTP_400_BAD_REQUEST)
				questions=request.data
				if "question" in questions:
					q.question=questions['question']
				q.save()
				pq=true_false_serialize(q)
				return Response(pq.data)
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)
				


# -------------------------

class mcq_answer_view(APIView):
	
	def get(self,request):
		if request.user.is_authenticated:
			creater=request.GET.get("creater")
			user=User.objects.get(username=creater)
			q=mcq_question.objects.filter(user=user)
			p=[]
			p=mcq_answer.objects.filter(user=request.user,question__in=q)
			ser=mcq_answer_sserialize(p,many=True)
			return Response(ser.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request):
		if request.user.is_authenticated:
			ans=mcq_answer.objects.filter(user=request.user)
			for i in ans:
				i.delete()
			return Response({"success":"all answeres are deleted"})
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class single_mcq_answer_view(APIView):

	def delete(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=mcq_question.objects.get(id=id)
				ans=mcq_answer.objects.filter(user=request.user,question=q)
				for i in ans:
					i.delete()
				return Response()
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def post(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=mcq_question.objects.get(id=id)
				a=mcq_answer.objects.filter(user=request.user,question=q)
				if len(a)!=0 and q.is_mcq==False:
					return Response({"error":"you already responded try to update or delete response"})
				d=request.data
				if 'ans' in d:
					i=d['ans']
					if i in ['op1','op2','op3','op4']:
						for x in a:
							if x.ans==i:
								return Response({"error":"already responded"})
						ans=mcq_answer(user=request.user,question=q,ans=i)
						ans.save()
					return Response({"success":"saved"})
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)

class true_false_answer_view(APIView):
	
	def get(self,request):
		if request.user.is_authenticated:
			p=true_false_answer.objects.filter(user=request.user)
			ser=true_false_answer_serialize(p,many=True)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request):
		if request.user.is_authenticated:
			q=true_false_answer.objects.filter(user=request.user)
			for i in q:
				i.delete()
			return Response({"success":"all t/f answeres are deleted"})
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class single_true_false_answer_view(APIView):

	def delete(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=true_false.objects.get(id=id)
				ans=true_false_answer.objects.filter(user=request.user,question=q)
				for i in ans:
					i.delete()
				return Response()
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)
	def post(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				print("hello")
				q=true_false.objects.get(id=id)
				a=true_false_answer.objects.filter(user=request.user,question=q)
				print(q)
				for i in a:
					i.delete()
				d=request.data
				if 'ans' in d:
					if bool(d['ans']) in [True,False]:
						ans=true_false_answer(user=request.user,question=q,ans=bool(d['ans']))
						ans.save()
						a=true_false_answer_serialize(ans)
						return Response(a.data)
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)
