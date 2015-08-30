# -*- coding: utf-8 -*-

from collective.conference.conference import IConference
from five import grok

grok.templatedir('templates')


class ConferenceView(grok.View):
    grok.context(IConference)
    grok.name('view')
    grok.template('conference_view')
    grok.require('zope2.View')
