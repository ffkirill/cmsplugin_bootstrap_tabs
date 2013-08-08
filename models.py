from django.utils.translation import ugettext as _
from django.db import models
from django.template.base import Context

from cms.models import Page
from cms.models import Placeholder
from cms.models import CMSPlugin


from inline_ordering.models import Orderable


class BootstrapTabs(CMSPlugin):
    """
    Bootstrap tabs plugin
    """
    title = models.CharField(verbose_name=_('Tabs plugin title'),
                             max_length=128)

    # placeholder_to_render = models.ForeignKey(Placeholder,
    #                                           verbose_name=_('Placeholder to render'),
    #                                           null=True,
    #                                           blank=True)

    def __unicode__(self):
        return self.title


class BootstrapTabsTab(Orderable):
    """
    Bootstrap tabs plugin tab
    """
    title = models.CharField(verbose_name=_('Tab title'),
                             max_length=128,
                             blank=True)

    content_page = models.ForeignKey(Page,
                                     verbose_name=_('Content (page)'),
                                     null=True,
                                     blank=True)

    content_text = models.TextField(verbose_name=_('Content (text)'),
                                    blank=True)

    active = models.BooleanField(verbose_name=_('Active'),
                                 default=True)

    tabs_plugin = models.ForeignKey(BootstrapTabs, related_name='tabs')

    def __unicode__(self):
        return self.title or self.pk

    @property
    def content(self):
        """
        Returns rendered page content or tab text content
        """
        return self.content_page or self.content_text or _('Empty')