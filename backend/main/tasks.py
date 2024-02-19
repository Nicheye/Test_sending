
from django.shortcuts import render
from .models import *
from .serializers import *
from django.utils import timezone
import requests

def sending_msg():
	time = timezone.now()
	all_senders = Sender.objects.filter(created_at__lt=time, created_until__gt=time)
	for sender in all_senders:
		filtered_clients = Client.objects.filter(tag=sender.tag,mobile_operator=sender.mobile_operator)
		url = 'https://probe.fbrq.cloud/v1'
		for client in filtered_clients:
			send_obj = {
				'id': sender.id,
				'phone':client.phone_number,
				'text':sender.text
				}
			request = requests.post(url, json = send_obj)
			if request.status_code == 200:
				msg_obj = Message()
				msg_obj.status = Send_Status.objects.get(name='sended')
				msg_obj.sender=client
				msg_obj.save()
			else:
				msg_obj = Message()
				msg_obj.status = Send_Status.objects.get(name='not_sended')
				msg_obj.sender=client
				msg_obj.save()