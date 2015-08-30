# -*- coding: utf-8 -*-

from collective.conference.participant import IParticipant
from five import grok

grok.templatedir('templates')


class ParticipantView(grok.View):
    grok.context(IParticipant)
    grok.template('participant_view')
    grok.name('view')
    grok.require('zope2.View')
