# -*- coding: utf-8 -*-
import awspice
from helpers import ThreadPool
from .services import *

class Durex(object):

    @property
    def ec2(self): return self._ec2

    @property
    def s3(self): return self._s3

    @property
    def iam(self): return self._iam

    def __init__(self, account='default'):
        self.client = awspice.connect(profile=account)
        self.pool = ThreadPool(30)
        self._ec2 = EC2(self.client)
        self._s3 = S3(self.client)
        self._iam = IAM(self.client)
