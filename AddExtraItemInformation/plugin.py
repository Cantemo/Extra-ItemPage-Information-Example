"""
This is your new plugin handler code.

Put your plugin handling code in here. remember to update the __init__.py file with 
you app version number. We have automatically generated a GUID for you, namespace, and a url 
that serves up index.html file
"""
import logging

from portal.pluginbase.core import Plugin, implements
from portal.generic.plugin_interfaces import (IPluginURL, IPluginBlock, IAppRegister)

log = logging.getLogger(__name__)


class ExtraItemInformationRegister(Plugin):
    # This adds it to the list of installed Apps
    # Please update the information below with the author etc..
    implements(IAppRegister)

    def __init__(self):
        self.name = "ExtraItemInfo"
        self.plugin_guid = '00957193-BFE2-4171-99E8-F3E9876E9FC8'
        log.debug('Register the App')

    def __call__(self):
        from .__init__ import __version__ as versionnumber
        _app_dict = {
                'name': 'ExtraItemInfo',
                'version': versionnumber,
                'author': '',
                'author_url': '',
                'notes': 'This App is example code and not supported by Cantemo AB.'}
        return _app_dict


ExtraItemInformationRegister()


class FrameRateItemPage(Plugin):
    """
    This adds information to the item page.
    """
    implements(IPluginBlock)

    def __init__(self):
        self.name = "ItemTechMetadataPlugin"
        self.plugin_guid = "B56D051D-93BB-40E0-8DE2-3F80E219BD2A"

    def return_string(self, tagname, *args):
        extra_info = " "
        valid_item_types = ('sequence', 'video',)
        context = args[1]
        item = context.get('item', None)
        if item is not None:
            if item.getItemType() in valid_item_types:
                extra_info += "<dl><dt>Framerate</dt><dd>"
                extra_info += item.getFramesPerSecond() + "fps"
                extra_info += "</dd></dl>"

        return {'guid': self.plugin_guid, 'template': extra_info}


FrameRateItemPage()
