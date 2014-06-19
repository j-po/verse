from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Request(models.Model):
    src = models.ForeignKey(User, related_name='sent')
    dest = models.ForeignKey(User, related_name='received')
    parent = models.ForeignKey('self', related_name='children',
                               related_query_name='child', null=True, blank=True)
    title = models.CharField(max_length=80)
    body = models.TextField()

    def __unicode__(self):
        if not self.title:
            return unicode(self.src) + u'->' + unicode(self.dest) + u':' + unicode(self.body)[:77] + u'...'
        return unicode(self.src) + u'->' + unicode(self.dest) + u':' + unicode(self.title)

    def get_absolute_url(self):
        return reverse('request-detail', kwargs={'pk': self.id})
