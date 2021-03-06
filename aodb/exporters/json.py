

import re

from json import dump
from xmljson import gdata
from xml.etree import ElementTree

from .base import BaseExporter


class JSONExporter(BaseExporter):
    def _generate_export(self):
        export_file = self.export_file.format('json')

        clean = re.sub(
            r' xmlns:xsi="http:\/\/www\.w3\.org\/2001\/XMLSchema-instance" xsi:noNamespaceSchemaLocation=".*\.xsd"',
            '',
            self.input
        )

        json = gdata.data(ElementTree.fromstring(clean))

        with open(export_file, 'w') as out_file:
            dump(json, out_file, indent=4)
