from django.contrib import admin
from django.urls import path ,include

from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView,TokenVerifyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
	path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken'),
	path('varifytoken/',TokenVerifyView.as_view(),name='varifytoken'),
    path('',include('app1.urls')),
]
