#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea
from django.db import models

class Tag(models.Model):

	body       = models.CharField(max_length = 64)
	updateDate = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.body

class TagForm(ModelForm):
	class Meta:
		model = Tag

class Message(models.Model):

	body     = models.TextField()
	datetime = models.DateTimeField(u'送信日時', auto_now_add = True)
	ref      = models.OneToOneField('self', null = True, blank = True)
	tag      = models.ForeignKey(Tag, null = True, blank = True, related_name = 'tag')

	def formatedDatetime(self):
		return self.datetime.strftime('%Y-%m-%d %H:%M')

	def __unicode__(self):
		return self.body[0:40]

class MessageForm(ModelForm):

	body       = forms.CharField(label = '', widget = Textarea(attrs = {'cols' : 80, 'rows' : 5}))
	tag_create = forms.CharField(label = '', required = False)
	ref        = forms.ModelChoiceField(queryset = Message.objects.all().order_by('-id'), label = '', required = False)
	tag        = forms.ModelChoiceField(queryset = Tag.objects.all().order_by('updateDate'), label = '', required = False)

	class Meta:
		model = Message
#		widgets = {
#			'body' : Textarea(attrs = {'cols' : 80, 'rows' : 5})
#		}
		exclude = ('tag',)
