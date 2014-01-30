from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import FormView

from message.models import Message, MessageForm

class MessageFormView(FormView):

	template_name = 'message/form.html'
	form_class = MessageForm

	def get_context_data(self, **kwargs):
		context = super(MessageFormView, self).get_context_data(**kwargs)
		context['message_list'] = Message.objects.all().order_by('-id')

		return context
