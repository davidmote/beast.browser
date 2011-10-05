from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class BeastBrowserPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import beast.browser as package
        xmlconfig.file('configure.zcml', package, context=configurationContext)


BEAST_BROWSER_FIXTURE = BeastBrowserPolicy()

BEAST_BROWSER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BEAST_BROWSER_FIXTURE,),
    name='BeastBrowser:Integration'
    )
