from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.views.generic import ListView, FormView, CreateView

from message.models import Message, MessageForm, Tag

def dev_delete(request):
	Tag.objects.all().delete()
	Message.objects.all().delete()
	return redirect('/message/1')


class MessageFormView(FormView):

	template_name = 'message/form.html'
	form_class = MessageForm

	def get_context_data(self, **kwargs):
		group = Group.objects.get(pk = self.args[0])

		context = super(MessageFormView, self).get_context_data(**kwargs)
		message_list = Message.objects.filter(group = group)
		if self.args[1]:
			message_list = message_list.filter(tag_id = self.args[1])

		context['message_list'] = message_list.order_by('-id')
		context['group'] = group
		context['css_list'] = ['css/message.css']
		context['js_list'] = ['js/message.js']
		context['form'] = MessageForm(group = group)

		return context

class MessageCreateView(CreateView):

	form_class = MessageForm
	template_name = 'message/form.html'

	def form_valid(self, form):
		group = self.createGroup(self.request.POST['group'])
		body  = self.request.POST['body']
		ref   = self.createRef(self.request.POST['ref'])
		tag   = self.createTag(self.request.POST['tag'], self.request.POST['tag_create'], group)

		object = Message(body = body, tag = tag, ref = ref, user = self.request.user, group = group)
		object.save()

		return redirect('/message/' + self.request.POST['group'])

	def createRef(self, ref):
		return Message.objects.get(pk = ref) if ref else None

	def createTag(self, tag, create, group):
		if tag:
			result = Tag.objects.get(pk = tag)
			result.save()
			return result
		elif create:
			result = Tag.objects.filter(body = create).filter(group = group)
			if result:
				result[0].save()
				return result[0]
			else:
				result = Tag(body = create, group = group)
				result.save()
				return result
		else:
			return None

	def createGroup(self, group):
		return Group.objects.get(pk = group)

	def get_context_data(self, **kwargs):
		group = Group.objects.get(pk = self.args[0])

		context = super(MessageCreateView, self).get_context_data(**kwargs)
		message_list = Message.objects.filter(group = group)

		context['message_list'] = message_list.order_by('-id')
		context['group'] = group
		context['css_list'] = ['css/message.css']
		context['js_list'] = ['js/message.js']

		return context

class TagListView(ListView):

	model = Tag
	template_name = 'tag/index.html'

	def get_context_data(self, **kwargs):
		group = Group.objects.get(pk = self.args[0])

		context = super(TagListView, self).get_context_data(**kwargs)

		context['tag_list'] = Tag.objects.filter(group = group).order_by('-last_used')
		context['group'] = group
		context['css_list'] = ['css/tag.css']

		return context
