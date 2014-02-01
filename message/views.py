from django.shortcuts import redirect
from django.views.generic import FormView, CreateView

from message.models import Message, MessageForm, Tag

class MessageFormView(FormView):

	template_name = 'message/form.html'
	form_class = MessageForm

	def get_context_data(self, **kwargs):
		context = super(MessageFormView, self).get_context_data(**kwargs)
		context['message_list'] = Message.objects.all().order_by('-id')
		context['css_list'] = ['css/message.css']
		context['js_list'] = ['js/message.js']

		return context

class MessageCreateView(CreateView):

	form_class = MessageForm
	template_name = 'message/form.html'
	success_url = '/message/'

	def form_valid(self, form):
		body = self.request.POST['body']
		ref  = self.createRef(self.request.POST['ref'])
		tag  = self.createTag(self.request.POST['tag'], self.request.POST['tag_create'])

		object = Message(body = body, tag = tag, ref = ref, user = self.request.user)
		object.save()

		return redirect(self.success_url)

	def createRef(self, ref):
		return Message.objects.get(pk = ref) if ref else None

	def createTag(self, tag, create):
		if tag:
			return Tag.objects.get(pk = tag)
		elif create:
			tag = Tag(body = create)
			tag.save()

			return tag
		else:
			return None

	def get_context_data(self, **kwargs):
		context = super(MessageCreateView, self).get_context_data(**kwargs)
		context['message_list'] = Message.objects.all().order_by('-id')
		context['css_list'] = ['css/message.css']
		context['js_list'] = ['js/message.js']

		return context
