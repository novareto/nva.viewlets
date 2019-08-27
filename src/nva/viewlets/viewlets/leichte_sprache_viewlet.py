# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class LeichteSpracheViewlet(ViewletBase):

    def update(self):
        self.message = self.get_message()

    def get_message(self):
        return u'My message'

    def render(self):
        return super(LeichteSpracheViewlet, self).render()
