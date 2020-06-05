# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class DocumentActionsViewlet(ViewletBase):

    def update(self):
        self.webcode = self.get_webcode()
        self.actions = self.get_standard_actions()

    def get_standard_actions(self):
        """
        Return the standard plone actions
        """
        context = self.context
        actions = context.portal_actions.listFilteredActionsFor(context)
        document_actions = actions.get('document_actions', [])
        return document_actions

    def get_webcode(self):
        """Holt den Webcode fuer den Inhalt"""
        if hasattr(self.context.aq_inner, 'webcode'):
            return self.context.aq_inner.webcode
        return ''

    def render(self):
        return super(DocumentActionsViewlet, self).render()
