from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import Page
from cms.plugin_rendering import render_placeholder

from .models import BootstrapTabs
from .admin import TabsInline


def rendered(collection, context):
    r = []
    for item in collection:

        if isinstance(item.content, Page):
            content = ''
            for placeholder in item.content.placeholders.all():
                content += render_placeholder(placeholder, context)
        else:
            content = item.content

        r.append({'instance': item,
                  'content': content})
    return r


class CMSPluginBootstrapTabs(CMSPluginBase):
    """
    CMS Plugin Bootstrap tabs
    """
    model = BootstrapTabs
    inlines = [TabsInline, ]
    name = _('Bootstrap tabs')
    admin_preview = False
    render_template = 'plugin_bootstrap_tabs/tabs.html'

    def render(self, context, instance, placeholder):
        context.update({'tabs': rendered(instance.tabs.all(), context),
                        })
        return context


plugin_pool.register_plugin(CMSPluginBootstrapTabs)