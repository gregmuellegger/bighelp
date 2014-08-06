from __future__ import print_function

import sys
from pprint import pprint


class BigHelp(object):
    def __init__(self, stdout=sys.stdout):
        self.stdout = stdout

    def __call__(self, *args, **kwargs):
        for arg in args:
            pprint(arg, stream=self.stdout)
        for arg, value in kwargs.items():
            print('{arg} = '.format(arg=arg), end='', file=self.stdout)
            pprint(value, stream=self.stdout)

    def __or__(self, other):
        '''
        H | other
        '''
        self.__call__(other)

    def __ror__(self, other):
        '''
        other | H
        '''
        self.__call__(other)

#    def __xor__(self, other):
#        '''
#        H ^ other
#
#        Return ``other``.
#        '''
#        self.__call__(other)
#        return other
#
#    def __rxor__(self, other):
#        '''
#        other ^ H
#
#        Return ``other``.
#        '''
#        self.__call__(other)
#        return other

    def __lt__(self, other):
        '''
        H < other
        '''
        self.__call__(other)

    def __rgt__(self, other):
        '''
        other > H
        '''
        self.__call__(other)

    def __lshift__(self, other):
        '''
        H << other

        Returns ``other``.
        '''
        self.__call__(other)
        return other

    def __rrshift__(self, other):
        '''
        other >> H

        Return ``other``.
        '''
        self.__call__(other)
        return other
