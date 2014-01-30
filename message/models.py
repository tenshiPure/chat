#-*- coding: utf-8 -*-

from django.forms import ModelForm
from django.db import models

class Message(models.Model):

	body     = models.TextField(u'本文')
	datetime = models.DateTimeField(u'送信日時', auto_now_add = True)
	ref      = models.OneToOneField('self', null = True, blank = True)

	def formatedDatetime(self):
		return self.datetime.strftime('%Y-%m-%d %H:%M')

	def __unicode__(self):
		return '%s : (%s) %s' % (self.id, self.formatedDatetime(), self.body)

class MessageForm(ModelForm):
	class Meta:
		model = Message
