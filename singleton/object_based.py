# coding: utf-8

u"""
The most right way to create singleton is import.
Import does singleton
"""

class A():
    u"""Single object"""
    pass

a = A()
# every import of 'a' is the same object
