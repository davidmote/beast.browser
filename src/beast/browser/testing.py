from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig

class beastBrowserPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import beast.browser
        xmlconfig.file('configure.zcml', beast.browser, context=configurationContext)

BEASTBROWSER_POLICY_FIXTURE = beastBrowserPolicy()
BEASTBROWSER_POLICY_INTEGRATION_TESTING = IntegrationTesting(bases=(BEASTBROWSER_POLICY_FIXTURE,), name="beastbrowser:Integration")
