from rest_framework import serializers
from .models import *
class Tag_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Tags
		fields = ['tag_name']
class Sender_Serializer(serializers.ModelSerializer):
	mobile_operator = serializers.SerializerMethodField()
	tag =serializers.SerializerMethodField()
	class Meta:
		model =  Sender
		fields = ['created_at','text','mobile_operator','tag','created_until']
	def get_mobile_operator(self,obj):
		return self.mobile_operator.name
	def get_tag(self,obj):
		return self.tag.tag_name


class Client_Serializer(serializers.ModelSerializer):
	mobile_operator = serializers.SerializerMethodField()
	tag =serializers.SerializerMethodField()
	class Meta:
		model =  Client
		fields = ['phone_number','mobile_operator','tag','timezone']
	def get_mobile_operator(self,obj):
		return self.mobile_operator.name
	def get_tag(self,obj):
		return self.tag.tag_name
	

class Message_Serializer(serializers.ModelSerializer):
	sender = serializers.SerializerMethodField()
	client = serializers.SerializerMethodField()
	status = serializers.SerializerMethodField()
	class Meta:
		model =  Message
		fields = ['send_at','status','sender','client']
	def get_sender(self,obj):
		return self.sender.id
	def get_client(self,obj):
		return self.client.phone_number
	def get_status(self,obj):
		return self.status.name

