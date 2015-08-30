# -*- coding: utf-8 -*-

from collective.conference import MessageFactory as _
from five import grok
from incf.countryutils import data as countrydata
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class TShirtSize(object):

    def __call__(self, context):
        return SimpleVocabulary.fromValues(
            [_(u'S'), _(u'M'), _(u'L'), _(u'XL'), _(u'XXL'), _(u'XXXL')]
        )

grok.global_utility(
    TShirtSize,
    IVocabularyFactory,
    name='collective.conference.vocabulary.tshirtsize'
)


class Countries(object):

    def __call__(self, context):
        return SimpleVocabulary.fromValues(sorted([
            i.decode('utf-8') for i, c in countrydata.cn_to_ccn.items() if c != '248'
        ]))

grok.global_utility(
    Countries,
    IVocabularyFactory,
    name='collective.conference.vocabulary.countries'
)


class SessionTypes(object):

    def __call__(self, context):
        return SimpleVocabulary([
            SimpleTerm(value=u'Talk', title=_(u'Talk')),
            SimpleTerm(value=u'Discussion', title=_(u'Discussion')),
            SimpleTerm(value=u'Hackfest', title=_(u'Hackfest')),
            SimpleTerm(value=u'Meta', title=_(u'Meta')),
            SimpleTerm(value=u'Workshop', title=_(u'Workshop')),
        ])

grok.global_utility(
    SessionTypes,
    IVocabularyFactory,
    name='collective.conference.vocabulary.sessiontype'
)


class SessionLevels(object):

    def __call__(self, context):
        return SimpleVocabulary([
            SimpleTerm(value=u'Beginner', title=_(u'Beginner')),
            SimpleTerm(value=u'Intermediate', title=_(u'Intermediate')),
            SimpleTerm(value=u'Advanced', title=_(u'Advanced'))
        ])

grok.global_utility(
    SessionLevels,
    IVocabularyFactory,
    name='collective.conference.vocabulary.sessionlevel'
)
