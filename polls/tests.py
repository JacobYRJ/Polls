from django.test import TestCase

from django.utils import timezone 
from .models import Question

import datetime 

class QuestionMethodTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		# was_published_recently()对未来时间应该返回False
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=30)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently, True)