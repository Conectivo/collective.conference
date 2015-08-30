# -*- coding: utf-8 -*-

from collective.conference.conference import IConference
from collective.conference.participant import IParticipant
from collective.conference.session import ISession
from plone.indexer.decorator import indexer


@indexer(IConference)
def c_conference_rooms(obj, **kw):
    return obj.rooms


@indexer(ISession)
def s_conference_rooms(obj, **kw):
    return obj.conference_rooms


@indexer(IParticipant)
def p_emails(obj, **kw):
    return [obj.email]
