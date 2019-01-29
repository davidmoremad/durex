# -*- coding: utf-8 -*-
import re

class EC2(object):

    def ec2_instances_naming_convention(self, regions=None):
        regpat = r'^((?!([a-zA-Z0-9_]*\-){3}).)*$'

        instances = self.ec2.get_instances(regions=regions)

        results = filter(lambda x: re.search(regpat, x['TagName']) ,instances)
        return results

    def __init__(self, client):
        self.ec2 = client.service.ec2