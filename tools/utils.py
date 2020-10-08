'''
    All the utility routines go here
'''
import os


def mksubdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
