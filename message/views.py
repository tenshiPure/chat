from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.models import Group
from django.views.generic import FormView, CreateView

from message.models import Message, MessageForm, Tag

class MessageFormView(FormView):

	template_name = 'message/form.html'
	form_class = MessageForm

	def get_context_data(self, **kwargs):
		group_id = self.args[0]
		tag_id = self.args[1]
		group = Group.objects.get(pk = group_id)

		context = super(MessageFormView, self).get_context_data(**kwargs)

		if tag_id:
			context['message_list'] = Message.objects.filter(Q(group = group) & Q(tag_id = tag_id)).order_by('-id')
		else:
			context['message_list'] = Message.objects.filter(group = group).order_by('-id')

		context['group'] = group
		context['css_list'] = ['css/message.css']
		context['js_list'] = ['js/message.js']

		return context

class MessageCreateView(CreateView):

	form_class = MessageForm
	template_name = 'message/form.html'

	def form_valid(self, form):
		body  = self.request.POST['body']
		ref   = self.createRef(self.request.POST['ref'])
		tag   = self.createTag(self.request.POST['tag'], self.request.POST['tag_create'])
		group = self.createGroup(self.request.POST['group'])

		object = Message(body = body, tag = tag, ref = ref, user = self.request.user, group = group)
		object.save()

		return redirect('/message/' + self.request.POST['group'])

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

	def createGroup(self, group):
		return Group.objects.get(pk = group)

	def get_context_data(self, **kwargs):
		context = super(MessageCreateView, self).get_context_data(**kwargs)
		context['message_list'] = Message.objects.all().order_by('-id')
		context['css_list'] = ['css/message.css']
		context['js_list'] = ['js/message.js']

		return context
