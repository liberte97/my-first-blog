from django.db import models

class Bookmark(models.Model):
	title = title = models.CharField(max_length=100, blank=True, null=True)
	url = models.URLField('url', unique=True)

	class Meta:
		verbose_name = '북마크'
		verbose_name_plural = '북마크 모음'
		ordering = ['title', ]

	def __str__(self):
		return self.title
