This is an example app which implements a Google Maps plugin on the item page, populated from EXIF GPS information.

## Installation

To install this plugin, just place the entire directory under `/opt/cantemo/portal/portal/plugins`.

Make sure the directory is readable by the Portal web-workers (default `www-data`).

For example, on a Portal system:

```
curl -L https://github.com/Cantemo/PortalGoogleMapsPlugin/archive/master.zip > PortalGoogleMapsPlugin-master.zip 
unzip PortalGoogleMapsPlugin-master.zip 
mv PortalGoogleMapsPlugin-master /opt/cantemo/portal/portal/plugins/PortalGoogleMapsPlugin/
chown -R www-data:www-data /opt/cantemo/portal/portal/plugins/PortalGoogleMapsPlugin
sudo service portal-web restart
```

## What's in the plugin

The app consists of a single plugin in `plugins.py`

This plugin hooks into the MediaViewLeftContentBottom plugin block and
displays a google map in an iframe in the lower left hand corner of
the item page, based on the EXIF GPS coordinates embedded in a photo.

