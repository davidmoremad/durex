# -*- coding: utf-8 -*-

def recommendation(func, description=None):
    func.severity = 'recommendation'
    func.description = func.__doc__ or str()
    name = func.__name__.replace('_',' ')
    func.name = name[0].upper() + name[1:]
    return func

def low(func, description=None):
    func.severity = 'low'
    func.description = func.__doc__ or str()
    name = func.__name__.replace('_',' ')
    func.name = name[0].upper() + name[1:]
    return func

def medium(func):
    func.severity = 'medium'
    func.description = func.__doc__ or str()
    name = func.__name__.replace('_',' ')
    func.name = name[0].upper() + name[1:]
    return func

def high(func):
    func.severity = 'high'
    func.description = func.__doc__ or str()
    name = func.__name__.replace('_',' ')
    func.name = name[0].upper() + name[1:]
    return func

def critical(func):
    func.severity = 'critical'
    func.description = func.__doc__ or str()
    name = func.__name__.replace('_',' ')
    func.name = name[0].upper() + name[1:]
    return func
