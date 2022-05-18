"""
.. Copyright 2012-2014 Cantemo AB. All Rights Reserved
"""

import logging

from portal.generic.plugin_interfaces import IPluginBlock
from portal.pluginbase.core import Plugin
from portal.pluginbase.core import implements

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
        return float(degrees) + float(minutes) / 60

    # Function called by the plugin framework. Returns the rendered template.
    def return_string(self, tagname, *args):
        ret = "maps/google_map.html"
        context = args[1]
        item = context["item"]
        metadata = item.getMetadata()[0]

        coords = error_message = None

        lat_field = metadata.getFieldByName("xmp_exif_GPSLatitude")
        long_field = metadata.getFieldByName("xmp_exif_GPSLongitude")
        if lat_field and long_field:
            lat = lat_field.getFirstFieldValue()
            long = long_field.getFirstFieldValue()
            try:
                lat_in_deg = self.convert_to_degrees(lat)
                long_in_deg = self.convert_to_degrees(long)
                coords = f"{lat_in_deg},{long_in_deg}"
            except Exception as e:
                error_message = f"Failed to convert coordinates ({lat}, {long} to degrees: {repr(e)})"
                log.exception(error_message)
        else:
            error_message = "EXIF values GPSLatitude and GPSLongitude not found on item."
            log.debug(error_message)

        return {
            "guid": self.plugin_guid,
            "template": ret,
            "context": {"coords": coords, "error_message": error_message},
        }


MapsPluginBlock()
