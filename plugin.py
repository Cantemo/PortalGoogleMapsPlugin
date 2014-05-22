"""
.. Copyright 2012-2014 Cantemo AB. All Rights Reserved
"""

from portal.pluginbase.core import *
from portal.generic.plugin_interfaces import IPluginBlock
import logging
log = logging.getLogger(__name__)


# Add the google snippet to each page, via the header_css_js plugin block
class MapsPluginBlock(Plugin):
    
    implements(IPluginBlock)

    def __init__(self):
        # This is the plugin block we add the plugin output to
        self.name = "MediaViewLeftContentBottom"
        self.plugin_guid = "3586BD21-DD4D-4BB7-803E-198AC1FDC3A2"
        log.debug("Initiated MapsPluginBlock")


    def convert_to_degrees(self, coord):
        s = coord.split(",")
        degrees = s[0]
        minutes = s[1][:-1]
        direction = s[1][-1]
        return float(degrees)+float(minutes)/60

    # Function called by the plugin framework. Returns the rendered template.
    def return_string(self, tagname, *args):
        ret = 'maps/google_map.html'
        context = args[1]
        item = context['item']
        metadata = item.getMetadata()[0]
        lat = metadata.getFieldByName('xmp_exif_GPSLatitude').getFirstFieldValue()
        long = metadata.getFieldByName('xmp_exif_GPSLongitude').getFirstFieldValue()
        lat_in_deg = self.convert_to_degrees(lat)
        long_in_deg = self.convert_to_degrees(long)
        coords = "%s,%s" %(lat_in_deg, long_in_deg)

        return {'guid':self.plugin_guid, 'template': ret, 'context' : { 'coords' : coords } }

pluginblock = MapsPluginBlock() 



