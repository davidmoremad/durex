# -*- coding: utf-8 -*-

def low(func, description=None):
    func.severity = 'low'
    func.description = func.__doc__ or str()
    return func

def medium(func):
    func.severity = 'medium'
    func.description = func.__doc__ or str()
    return func

def high(func):
    func.severity = 'high'
    func.description = func.__doc__ or str()
    return func

def critical(func):
    func.severity = 'critical'
    func.description = func.__doc__ or str()
    return func
