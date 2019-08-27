# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class LeichteSpracheViewlet(ViewletBase):

    def update(self):
        self.leichtesprache = self.get_leichtesprache()

    def get_leichtesprache(self):
        if hasattr(self.context, 'leichtesprache'):
            if self.context.leichtesprache:
                return self.context.leichtesprache.output

    def render(self):
        if hasattr(self.context, 'leichtesprache'):
            if self.context.leichtesprache:
                return super(LeichteSpracheViewlet, self).render()
        else:
            return ""
