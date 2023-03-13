from django.shortcuts import render

# Create your views here.
from rest_framework import views,response
from . import tasks

class TestRabiitMQAPIView(views.APIView):
    
    def post(self,request):
        
        tasks.create_random_user_accounts.delay(int(request.data['total']))
        return response.Response({"message":"task started"})
    