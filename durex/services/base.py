# -*- coding: utf-8 -*-
from durex.helpers import ThreadPool

class Base(object):

    pool = ThreadPool(30)
    