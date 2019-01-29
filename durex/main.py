# -*- coding: utf-8 -*-
import awspice
from .services import *

class Durex(object):

    @property
    def ec2(self): return self._ec2

    def __init__(self, account='default'):
        self.client = awspice.connect(profile=account)
        self._ec2 = EC2(self.client)
