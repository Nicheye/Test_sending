from django.shortcuts import render
from .models import *
from .serializers import *
from django.utils import timezone
import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from main.tasks import sending_msg

import threading
import time

class ClientView(APIView):
	def get(self,request,*args,**kwargs):
		
		id = kwargs.get("id",None)
		if id is not None:
			client = Client.objects.get(id=id)
			client_ser = Client_Serializer(client)
			return Response({"data":client_ser.data})
		clients= Client.objects.all()
		clients_ser = Client_Serializer(clients,many=True)
		return Response({"data":clients_ser.data})
	def post(self,request,*args,**kwargs):
		data = request.data
		client_cr_ser = Client_Serializer(data=data)
		if client_cr_ser.is_valid(raise_exception=True):
			client_cr_ser.save()
			return Response({"data":client_cr_ser.data})
	def patch(self,request,*args,**kwargs):
		data = request.data
		id = kwargs.get("id",None)
		if id is not None:
			client_obj = Client.objects.get(id=id)
			client_cr_ser = Client_Serializer(client_obj,data=data)
			if client_cr_ser.is_valid(raise_exception=True):
				client_cr_ser.save()
				return Response({"data":client_cr_ser.data})
		else:
			return Response({"INFO":"id is none"})
	def delete(self,request,*args,**kwargs):
		id = kwargs.get("id",None)
		if id is not None:
			client = Client.objects.get(id=id)
			client.delete()
			return Response({"INFO":"client successfully deleted"})

class SenderView(APIView):
	def post(self,request,*args,**kwargs):
		data =request.data
		sender_ser = Sender_Serializer(data=data)
		if sender_ser.is_valid(raise_exception=True):
			sender_ser.save()
			return Response({"data":sender_ser.data})
	def get(self,request,*args,**kwargs):
		id = kwargs.get("id",None)
		if id is not None:
			sender = Sender.objects.get(id=id)
			all_ms =Message.objects.filter(sender=sender)
			count_message = Message.objects.filter(sender=sender).count()
			groups = {

			}
			for ms in all_ms:
				try:
					groups[ms.client.tag] = groups[ms.client.tag]+1
				except:
					groups[ms.client.tag] = 1
				try:
					groups[ms.client.mobile_operator] = groups[ms.client.mobile_operator]+1
				except:
					groups[ms.client.mobile_operator] = 1
			return Response({
				"отправлено":count_message,
				"статистика":groups
				})
		senders_cnt = Sender.objects.all().count()
		msg_cnt = Message.objects.all().count
		all_msg=Message.objects.all()
		groups = {

			}
		for ms in all_msg:
			try:
				groups[ms.client.tag] = groups[ms.client.tag]+1
			except:
				groups[ms.client.tag] = 1
			try:
				groups[ms.client.mobile_operator] = groups[ms.client.mobile_operator]+1
			except:
				groups[ms.client.mobile_operator] = 1
	
		return Response({
			"всего рассылок":senders_cnt,
			"всего сообщенгий":msg_cnt,
			"по группам" :groups
		})

	def patch(self,request,*args,**kwargs):
		id = kwargs.get("id",None)
		if id is not None:
			data = request.data
			sender = Sender.objects.get(id=id)
			sender_ser = Sender_Serializer(sender,data=data)
			if sender_ser.is_valid(raise_exception=True):
				sender_ser.save()
				return Response({"data":sender_ser.data})
				
	def delete(self,request,*args,**kwargs):
		id = kwargs.get("id",None)
		if id is not None:
			sender = Sender.objects.get(id=id)
			sender.delete()
			return Response({"info":"рассылка удалена "})
class Tags(APIView):
	def post(self,request):
		data =request.data
		tag_s = Tag_Serializer(data=data)
		if tag_s.is_valid(raise_exception=True):
			tag_s.save()
			return Response({"data":tag_s.data})



def background_task():
    while True:
        sending_msg()
        # Add your script logic here
        time.sleep(10)  # Sleep for 10 seconds before running again

# Create a thread for the background task
background_thread = threading.Thread(target=background_task)
background_thread.daemon = True  # Daemonize the thread so it exits when the main thread exits

# Start the background thread
background_thread.start()