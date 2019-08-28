# -*- coding: utf-8 -*-

from nva.viewlets import _
from Products.Five.browser import BrowserView

class LeichteSprache(BrowserView):

    def leichtesprache(self):
        if hasattr(self.context, 'leichtesprache'):
            if self.context.leichtesprache:
                return self.context.leichtesprache.output
        return u""
