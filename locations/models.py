import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class Page(models.Model):
    """ Represents a single page. """
    objects = models.Manager()
    slug = models.CharField(max_length=settings.PAGE_TITLE_MAX_LENGTH, blank=True, editable=False, help_text="Unique URL path to access this page. Generated by the system.")
    created = models.DateTimeField(auto_now_add=True, help_text="The date and time this page was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True, help_text="The date and time this page was updated. Automatically generated when the model updates.")
    title = models.CharField(max_length=settings.PAGE_TITLE_MAX_LENGTH, unique=True, default="Title of your page.")
    author = models.ForeignKey(User, on_delete=models.PROTECT, help_text="The user that posted this article.")
    content = models.TextField(default="Write the content of your page here.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-page). """
        path_components = {'slug': self.slug}
        return reverse('details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Page, self).save(*args, **kwargs)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
