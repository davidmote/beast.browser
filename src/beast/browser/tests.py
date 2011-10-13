import unittest2 as unittest
from beast.browser.testing import BEAST_BROWSER_INTEGRATION_TESTING
from plone.app.testing import applyProfile

from Products.CMFCore.utils import getToolByName


class TestSetup(unittest.TestCase):

    layer = BEAST_BROWSER_INTEGRATION_TESTING

    def test_should_fail(self):
        self.fail('Tests not implemented yet.')
