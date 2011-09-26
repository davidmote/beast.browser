import unittest2 as unittest
from beast.browser.testing import BEASTBROWSER_POLICY_INTEGRATION_TESTING
from plone.app.testing import applyProfile

from Products.CMFCore.utils import getToolByName

class TestSetup(unittest.TestCase):
    
    layer = BEASTBROWSER_POLICY_INTEGRATION_TESTING

    def test_should_fail(self):
        self.fail()