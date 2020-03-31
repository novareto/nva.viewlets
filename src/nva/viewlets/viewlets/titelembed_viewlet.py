# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class TitelembedViewlet(ViewletBase):

    def render(self):
        if hasattr(self.context, 'embedcode'):
            if 'embedcode' in self.context.__dict__:
                if self.context.embedcode and self.context.viewlet == 'video':
                    return super(TitelembedViewlet, self).render()
        return ""
