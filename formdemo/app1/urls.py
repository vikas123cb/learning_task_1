from django.contrib import admin
from django.urls import path , include
# from rest_framework import routers, urlpatterns
# from .views import ListUsers
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response

# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })
# '''
# # question & answer
# from django.urls import path
# from .import views
# urlpatterns = [
# 	path('api_mcq',views.api_mcq_question.as_view(),name='api_mcq'),
# 	path('api_mcq/<int:id>',views.api_mcq_one.as_view(),name='api_mcq_one'),
# 	path('api_tf',views.api_tf_question.as_view(),name='api_tf_one'),
# 	path('api_tf/<int:id>',views.api_tf_one.as_view(),name='api_tf_question'),

# 	path('api_mcq_ans',views.api_mcq_answer.as_view(),name='api_mcq_answer'),
# 	path('api_mcq_ans/<int:id>',views.api_mcq_answer_one.as_view(),name='api_mcq_answer_one'),
# 	path('api_tf_ans',views.api_true_false_answer.as_view(),name='api_true_false_answer'),
# 	path('api_tf_ans/<int:id>',views.api_true_false_answer_one.as_view(),name='api_true_false_answer_one'),

# ]'''

from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('crud',views.mcq_question_ViewSet, basename='mcq_question')
# # router.register('crud',views.msq_question_ViewSet, basename='mcq_question')
# router.register('crud2',views.true_false_ViewSet, basename='tf_question')

urlpatterns=[
    path('mcq_question/',views.mcq_question_view.as_view(),name='mcq'),
    path('mcq_question/<int:id>/',views.single_mcq_question_view.as_view(),name='mcq_id'),
    path('tf_question/',views.true_false_question_view.as_view(),name='tf'),
    path('tf_question/<int:id>/',views.single_tf_question_view.as_view(),name='tf_id'),
   
    path('mcq_answer/',views.mcq_answer_view.as_view(),name='mcq'),
    path('mcq_answer/<int:id>/',views.single_mcq_answer_view.as_view(),name='mcq_id'),
    path('tf_question/',views.true_false_answer_view.as_view(),name='tf'),
    path('tf_question/<int:id>/',views.single_true_false_answer_view.as_view(),name='tf_id'),
   
]
