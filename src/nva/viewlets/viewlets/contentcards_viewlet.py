# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api as ploneapi

class ContentCardsViewlet(ViewletBase):

    def get_cards(self):
        objview = ploneapi.content.get_view(name='enhanced_foldersummary', context=self.context, request=self.request)
        cards = objview.getContextCards(self.context, 'contentcards')
        size = self.context.cardcolumns
        if cards:
            return [cards[i:i+size] for i in range(0, len(cards), size)]
        return []

    def render(self):
        if hasattr(self.context, 'contentcards'):
            if self.context.contentcards:
                return super(ContentCardsViewlet, self).render()
            else:
                return ""
        else:
            return ""
