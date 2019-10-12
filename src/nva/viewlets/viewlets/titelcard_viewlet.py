# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from nva.viewlets.viewlets.titelbild_viewlet import TitelbildViewlet


class TitelcardViewlet(TitelbildViewlet):

    def render(self):
        if hasattr(self.context, 'titleimages'):
            if self.context.titleimages and self.context.viewlet == 'overlay':
                return super(TitelbildViewlet, self).render()
            else:
                return ""
        else:
            return ""
