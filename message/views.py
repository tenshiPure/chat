from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView

from message.models import Message

class MessageListView(ListView):

	template_name = 'message/index.html'

	def get_queryset(self):
		return Message.objects.all()
