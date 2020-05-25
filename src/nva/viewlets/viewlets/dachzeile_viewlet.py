# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class DachzeileViewlet(ViewletBase):

    def update(self):
        self.dachzeile = self.get_dachzeile()

    def get_dachzeile(self):
        if hasattr(self.context.aq_inner, 'dachzeile'):
            if self.context.aq_inner.dachzeile:
                return self.context.aq_inner.dachzeile
        return u""

    def render(self):
        return super(DachzeileViewlet, self).render()
