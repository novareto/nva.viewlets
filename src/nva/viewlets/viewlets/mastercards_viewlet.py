# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api as ploneapi

hide_layouts = ['enhanced_cardview', 'enhanced_cardcolumns', 'zwei_spalten_view', 'zwei_spalten_context_view']

class MastercardsViewlet(ViewletBase):

    def get_cards(self):
        objview = ploneapi.content.get_view(name='enhanced_foldersummary', context=self.context, request=self.request)
        cards = objview.getContextCards(self.context)
        size = 3
        if cards:
            return [cards[i:i+size] for i in range(0, len(cards), size)]
        return []

    def render(self):
        try:
            layout = self.context.layout
        except:
            layout = ''
        if layout:    
            if self.context.layout in hide_layouts:
                return ""
        if hasattr(self.context, 'cards'):
            if self.context.cards:
                return super(MastercardsViewlet, self).render()
            else:
                return ""
        else:
            return ""
