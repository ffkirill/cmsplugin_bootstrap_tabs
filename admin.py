from django.conf import settings
from django.contrib.admin import StackedInline

from cms.plugins.text.widgets.wymeditor_widget import WYMEditor
from cms.plugins.text.settings import USE_TINYMCE

from .models import BootstrapTabsTab


class TabsInline(StackedInline):
    """
    Inline for bootstrap tabs
    """
    model = BootstrapTabsTab
    admin_preview = False

    def get_editor_widget(self):
        """
        Returns the Django form Widget to be used for
        the text area
        """
        if USE_TINYMCE and "tinymce" in settings.INSTALLED_APPS:
            from cms.plugins.text.widgets.tinymce_widget import TinyMCEEditor
            return TinyMCEEditor(installed_plugins=None)
        else:
            return WYMEditor(installed_plugins=None)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "content_text":
            kwargs['widget'] = self.get_editor_widget()
        return super(TabsInline, self).formfield_for_dbfield(db_field,
                                                             **kwargs)

    class Media:
        js = ('cms/js/libs/jquery.query.js',
              'cms/js/libs/jquery.ui.core.js',
              'cms/js/libs/jquery.ui.sortable.js',
              'js/tab_inline_ordering.js',)

