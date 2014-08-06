#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bighelp
----------------------------------

Tests for `bighelp` module.
"""

from StringIO import StringIO
import unittest

from mock import Mock

import bighelp


class TestUtilsMixin(object):
    def setUp(self):
        self.stdout = StringIO()
        self.H = bighelp.BigHelp(stdout=self.stdout)


class TestBighelp(TestUtilsMixin, unittest.TestCase):
    def test_H(self):
        from bighelp import H
        self.assertTrue(isinstance(H, bighelp.BigHelp))

    def test_pprint(self):
        data = list(range(5))
        self.H(data)
        self.assertEqual(
            self.stdout.getvalue(),
            '[0, 1, 2, 3, 4]\n')

    def test_pprint_kwargs(self):
        self.H(more=[1, 2, 3])
        self.assertEqual(
            self.stdout.getvalue(),
            'more = [1, 2, 3]\n')


class TestBigHelp(TestUtilsMixin, unittest.TestCase):
    def test_pipe_syntax(self):
        call_mock = Mock()
        self.H.__call__ = call_mock
        obj = object()

        obj | self.H

        call_mock.assert_called_once_with(obj)

    def test_pipe_syntax_with_objects_that_implement_or(self):
        call_mock = Mock()
        self.H.__call__ = call_mock

        False | self.H

        call_mock.assert_called_once_with(False)

    def test_pipe_syntax_returns_other(self):
        self.assertTrue((False | self.H) is False)

    def test_pipe_syntax_with_calling_other_or_directly(self):
        call_mock = Mock()
        self.H.__call__ = call_mock

        False.__or__(self.H)

        self.assertFalse(call_mock.called)

    def test_lshift_syntax(self):
        call_mock = Mock()
        self.H.__call__ = call_mock
        obj = object()

        self.H << obj

        call_mock.assert_called_once_with(obj)

    def test_lshift_syntax_returns_other(self):
        self.assertTrue((self.H << False) is False)

    def test_rrshift_syntax(self):
        call_mock = Mock()
        self.H.__call__ = call_mock
        obj = object()

        obj >> self.H

        call_mock.assert_called_once_with(obj)

    def test_rrshift_syntax_returns_other(self):
        self.assertTrue((False >> self.H) is False)


if __name__ == '__main__':
    unittest.main()
