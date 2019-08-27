# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import nva.viewlets


class NvaViewletsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=nva.viewlets)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'nva.viewlets:default')


NVA_VIEWLETS_FIXTURE = NvaViewletsLayer()


NVA_VIEWLETS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NVA_VIEWLETS_FIXTURE,),
    name='NvaViewletsLayer:IntegrationTesting',
)


NVA_VIEWLETS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NVA_VIEWLETS_FIXTURE,),
    name='NvaViewletsLayer:FunctionalTesting',
)


NVA_VIEWLETS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NVA_VIEWLETS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='NvaViewletsLayer:AcceptanceTesting',
)
