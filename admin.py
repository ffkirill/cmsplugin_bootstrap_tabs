import os.path

from django.conf import settings

from inline_ordering.admin import OrderableStackedInline
from .models import BootstrapTabsTab


class TabsInline(OrderableStackedInline):
    """
    Inline for bootstrap tabs
    """
    model = BootstrapTabsTab
    admin_preview = False

    class Media:
        js = (os.path.join(settings.CMS_MEDIA_URL,
                           'wymeditor/jquery.wymeditor.js'),
              'js/admin_textarea.js',
        )

        css = {
            'all': [os.path.join(settings.CMS_MEDIA_URL, path) for path in (
                'css/jquery/cupertino/jquery-ui.css',
                'css/wymeditor.css',
            )],
        }

