# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.viewlet.interfaces import IViewletManager


class INvaViewletsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IContentCardsViewletManager(IViewletManager):
    """ Eigener Viewlet-Manager fuer Content-Karten """
