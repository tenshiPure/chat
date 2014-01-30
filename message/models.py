#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.db import models

class Tag(models.Model):

	body       = models.CharField(max_length = 64)
	updateDate = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return '%s : %s' % (self.id, self.body)

class TagForm(ModelForm):
	class Meta:
		model = Tag

class Message(models.Model):

	body     = models.TextField(u'本文')
	datetime = models.DateTimeField(u'送信日時', auto_now_add = True)
	ref      = models.OneToOneField('self', null = True, blank = True)
	tag      = models.ForeignKey(Tag, null = True, blank = True, related_name = 'tag')

	def formatedDatetime(self):
		return self.datetime.strftime('%Y-%m-%d %H:%M')

	def __unicode__(self):
		return '%s : (%s) %s' % (self.id, self.formatedDatetime(), self.body)

class MessageForm(ModelForm):

	tag_create = forms.CharField(required = False)

	class Meta:
		model = Message
