# -*- coding: utf-8 -*-
from durex.helpers import ThreadPool

class Base(object):

    pool = ThreadPool(30)

    def get_tests(self):
        methods = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith('_')]
        tests = filter(lambda x: hasattr(getattr(self, x), 'severity'), methods)
        return map(lambda x: {'Method': x, 'Description': getattr(self, x).description, 'Severity': getattr(self, x).severity} ,tests)
