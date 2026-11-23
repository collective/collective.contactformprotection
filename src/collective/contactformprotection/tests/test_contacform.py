"""Setup tests for this package."""

from collective.contactformprotection.testing import (
    COLLECTIVE_CONTACTFORMPROTECTION_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.z3cform.interfaces import IPloneFormLayer
from plone.browserlayer.utils import registered_layers
from plone.registry.interfaces import IRegistry
from plone.testing.zope import Browser
from Products.CMFPlone.browser.contact_info import ContactForm
from unittest import mock
from zope.component import getUtility
from zope.interface import alsoProvides

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.contactformprotection is properly installed."""

    layer = COLLECTIVE_CONTACTFORMPROTECTION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.browser = Browser(self.layer["app"])
        self.browser.addHeader(
            "Authorization",
            "Basic {}:{}".format(
                SITE_OWNER_NAME,
                SITE_OWNER_PASSWORD,
            ),
        )

        # The browser tests save the control panel; start every test from
        # the default settings.
        registry = getUtility(IRegistry)
        registry["collective.contactformprotection.disable_form"] = False
        registry["collective.contactformprotection.use_captcha"] = None

    def test_contactform_disabled(self):
        self.browser.open("http://nohost/plone/contact-info")
        self.assertIn("form.widgets.sender_fullname", self.browser.contents)

        # disable via controlpanel
        self.browser.open("http://nohost/plone/@@contactformprotection-controlpanel")
        self.browser.getControl("Disable contactform globally").click()
        self.browser.getControl("Save").click()

        # there should be nomore contactform
        self.browser.open("http://nohost/plone/contact-info")
        self.assertNotIn("form.widgets.sender_fullname", self.browser.contents)
        self.assertIn("Contact form is disabled.", self.browser.contents)

    def test_contactform_captchawidget(self):
        self.browser.open("http://nohost/plone/contact-info")

        # disabled per default
        self.assertNotIn(
            "formfield-form-widgets-IContactFormCaptchaField-captcha",
            self.browser.contents,
        )

        # enable captcha in controlpanel
        self.browser.open("http://nohost/plone/@@contactformprotection-controlpanel")
        self.browser.getControl(name="form.widgets.use_captcha:list").value = "hcaptcha"
        self.browser.getControl("Save").click()

        self.browser.open("http://nohost/plone/contact-info")
        # field should be visible now
        self.assertIn(
            "formfield-form-widgets-IContactFormCaptchaField-captcha",
            self.browser.contents,
        )

    def _post_contactform(self):
        request = self.layer["request"]
        alsoProvides(request, IPloneFormLayer, *registered_layers())
        request.method = "POST"
        request.form.update(
            {
                "form.widgets.sender_fullname": "John Doe",
                "form.widgets.sender_from_address": "john@example.org",
                "form.widgets.subject": "Hello",
                "form.widgets.message": "Just a test",
                "form.buttons.send": "Send",
            }
        )
        view = api.content.get_view("contact-info", self.portal, request)
        with (
            mock.patch.object(ContactForm, "send_message") as send_message,
            mock.patch.object(ContactForm, "send_feedback"),
            mock.patch("plone.protect.authenticator.check"),
        ):
            html = view()
        return send_message, html

    def test_contactform_post_is_sent_when_enabled(self):
        send_message, html = self._post_contactform()
        send_message.assert_called_once()

    def test_contactform_disabled_ignores_post(self):
        api.portal.set_registry_record(
            "collective.contactformprotection.disable_form", True
        )
        send_message, html = self._post_contactform()
        send_message.assert_not_called()
        self.assertIn("Contact form is disabled.", html)
