# -*- coding: utf-8 -*-

from Acquisition import aq_parent

# from collective import dexteritytextindexer
from collective.conference import MessageFactory as _
# from collective.dexteritytextindexer.behavior import IDexterityTextIndexer
from five import grok

# from plone.app.textfield import RichText
# from plone.dexterity.utils import createContentInContainer
from plone.directives import dexterity
from plone.directives import form
# from plone.formwidget.contenttree import ObjPathSourceBinder
# from plone.i18n.normalizer.interfaces import IURLNormalizer
# from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
# from plone.namedfile.field import NamedFile
# from plone.namedfile.field import NamedImage
from plone.namedfile.interfaces import IImageScaleTraversable

# from z3c.form import field
# from z3c.form import group
# from z3c.relationfield.schema import RelationChoice
# from z3c.relationfield.schema import RelationList
from zope import schema
# from zope.component import getUtility
from zope.component.hooks import getSite
# from zope.interface import Invalid
# from zope.interface import invariant
# from zope.schema.interfaces import IContextSourceBinder
# from zope.schema.vocabulary import SimpleTerm
# from zope.schema.vocabulary import SimpleVocabulary

# Interface class; used to define content-type schema.


class IConference(form.Schema, IImageScaleTraversable):
    """
    A conference event
    """

    logo_image = NamedBlobImage(title=_(u'Logo'))

    form.widget(rooms='plone.z3cform.textlines.TextLinesFieldWidget')
    rooms = schema.List(
        title=_(u'Available Rooms'),
        value_type=schema.TextLine()
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.


class Conference(dexterity.Container):
    grok.implements(IConference)
    grok.provides(IConference)

    # Add your class methods and properties here

    def getConference(self):
        site = getSite()
        parent = self
        while parent != site:
            if IConference.providedBy(parent):
                return parent
            parent = aq_parent(parent)
        return None
