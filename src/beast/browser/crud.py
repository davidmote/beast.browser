from zope import schema
from zope.app.pagetemplate import viewpagetemplatefile

from z3c.form import field
from z3c.form.interfaces import INPUT_MODE
from z3c.batching import batch

from plone.z3cform.layout import FormWrapper
from plone.z3cform.widget import singlecheckboxwidget_factory
from plone.z3cform.crud import crud

from beast.browser import MessageFactory as _

class NestedFormView(FormWrapper):
    """
    Subclass FormWrapper so that we can use custom frame template.
    """
    index = viewpagetemplatefile.ViewPageTemplateFile("templates/nestedform.pt")


class PreselectedEditSubForm(crud.EditSubForm):

    def _select_field(self):
        select_field = field.Field(
            schema.Bool(__name__='select',
                             required=False,
                             title=_(u'select'),
                             default=True))
        select_field.widgetFactory[INPUT_MODE] = singlecheckboxwidget_factory
        return select_field


class wrappableAddForm(crud.AddForm):
    """
    Needed to make crud play with plone.app.z3cform (which provides kss)
    """
    template = viewpagetemplatefile.ViewPageTemplateFile('templates/crud-add.pt')


from z3c.batching.batch import first_neighbours_last as f_n_l
class BatchNavigation(crud.BatchNavigation):
    template = viewpagetemplatefile.ViewPageTemplateFile('templates/batch.pt')
    
    def __call__(self):
        pages = []
        batch = self.context
        number_pages = batch.total
        
        if batch.total <= 1:
            return u""
        else:
            for i in f_n_l(range(batch.total), batch.index, 5, 5):
                if i is None:
                    pages.append(dict(label=unicode('...'), link=None))
                elif i == batch.index:
                    pages.append(dict(label=unicode(i+1), link=None))
                else:
                    link = self.make_link(page=i)           
                    pages.append(dict(label=unicode(i+1), link=link))

            return self.template(batch=batch, pages=pages)

