# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class LeichteSpracheViewlet(ViewletBase):

    def update(self):
        self.button = self.get_button()

    def get_button(self):
        button = {}
        button['name'] = u'Leichte Sprache'
        button['url'] = self.context.absolute_url() + '/leichte-sprache'
        if self.request.URL.endswith('leichte-sprache'):
            button['name'] = u'Standardsprache'
            button['url'] = self.context.absolute_url()
        return button

    def render(self):
        if hasattr(self.context, 'leichtesprache'):
            if self.context.leichtesprache:
                return super(LeichteSpracheViewlet, self).render()
            else:
                return ""
        else:
            return ""
