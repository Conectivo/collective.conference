# -*- coding: utf-8 -*-

from Products.CMFPlone.utils import _createObjectByType
from Products.statusmessages.interfaces import IStatusMessage
from collective.conference import MessageFactory as _
from collective.conference.conference import IConference
from collective.conference.session import ISession
from collective.conference.session import Session
from datetime import timedelta
from five import grok
# from plone.dexterity.utils import createContentInContainer
from plone.directives import form
from plone.formwidget.captcha import CaptchaFieldWidget
from plone.formwidget.captcha.validator import CaptchaValidator
from zope import schema
from zope.component.hooks import getSite
from zope.globalrequest import getRequest


class IProposalForm(ISession):
    form.widget(captcha=CaptchaFieldWidget)
    captcha = schema.TextLine(
        title=u'',
        required=False
    )
    form.omitted('conference_rooms', 'color', 'textColor')


@form.validator(field=IProposalForm['captcha'])
def validateCaptca(value):
    site = getSite()
    request = getRequest()

    if request.getURL().endswith('kss_z3cform_inline_validation'):
        return

    captcha = CaptchaValidator(site, request, None,
                               IProposalForm['captcha'], None)
    captcha.validate(value)


class ProposalForm(form.SchemaAddForm):
    grok.name('propose')
    grok.context(IConference)
    grok.require('zope.Public')
    schema = IProposalForm
    label = _(u'Propose a session')

    def create(self, data):
        obj = Session()
        inc = getattr(self.context, 'session_increment', 0) + 1
        data['id'] = 'session-%s' % inc
        data['startDate'] = self.context.startDate
        data['endDate'] = self.context.startDate + timedelta(0, 3600)
        self.context.session_increment = inc
        obj = _createObjectByType('collective.conference.session',
                                  self.context, data['id'])
        del data['captcha']
        for k, v in data.items():
            setattr(obj, k, v)
        IStatusMessage(self.request).addStatusMessage(
            _(u'Thank you for your submission. Your submission is now held for approval and will appear on the site once it is approved')
        )
        obj.reindexObject()
        return obj

    def add(self, obj):
        pass
