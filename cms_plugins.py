from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import Popup

class CMSPopupPlugin(CMSPluginBase):
    model = Popup
    name = _("Popup Plugin") # name of the plugin in the interface
    render_template = "popup.html"
    #cache = False #This is a property that tells the plugin rendering system in django CMS whether to cache the plugin.s output to speed-up subsequent views of the same plugin

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(CMSPopupPlugin)
