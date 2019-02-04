# -*- coding: utf-8 -*-
import awspice
from helpers import ThreadPool
from .services import *

class Durex(object):

    def __init__(self, account='default'):
        self.client = awspice.connect(profile=account)
        self._ec2 = EC2(self.client)
        self._s3 = S3(self.client)
        self._iam = IAM(self.client)

    @property
    def ec2(self): return self._ec2

    @property
    def s3(self): return self._s3

    @property
    def iam(self): return self._iam


    def get_profiles(self): return self.client.service.ec2.get_profiles()
    def set_profile(self, profile): self.client.service.ec2.change_profile(profile)

    def get_regions(self): return self.client.service.ec2.get_regions()
    def set_region(self, region): self.client.service.ec2.change_region(region)