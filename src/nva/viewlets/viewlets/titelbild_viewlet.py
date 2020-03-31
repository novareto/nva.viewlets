# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class TitelbildViewlet(ViewletBase):

    def get_titelbilder(self):
        titelbilder = []
        for index, titelbild in enumerate(self.context.titleimages):
            entry = {}
            obj = titelbild.to_object
            entry['imgsrc'] = "%s/@@images/image" % obj.absolute_url()
            entry['title'] = obj.title
            entry['description'] = obj.description
            entry['reference'] = "#"
            entry['reftitle'] = ''
            if obj.relatedItems:
                entry['reference'] = obj.relatedItems[0].to_object.absolute_url()
                entry['reftitle'] = obj.relatedItems[0].to_object.title
            if 'newsurl' in obj.__dict__:
                if obj.newsurl:
                    entry['reference'] = obj.newsurl.to_object.absolute_url()
                    entry['reftitle'] = obj.newsurl.to_object.title
            if 'extnews' in obj.__dict__:
                if obj.extnews:
                    entry['reference'] = obj.extnews
                    entry['reftitle'] = obj.extnewstitle
            entry['slide'] = index
            titelbilder.append(entry)
        return titelbilder
            
    def render(self):
        if hasattr(self.context, 'titleimages'):
            if 'titleimages' in self.context.__dict__:
                if self.context.titleimages and self.context.viewlet == 'header':
                    return super(TitelbildViewlet, self).render()
        return u""
