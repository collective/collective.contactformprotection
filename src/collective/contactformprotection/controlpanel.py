from collective.contactformprotection import _
from collective.contactformprotection.interfaces import (
    ICollectiveContactformprotectionLayer,
)
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IContacformprotectionControlPanel(Interface):
    myfield_name = schema.TextLine(
        title=_(
            "This is an example field for this control panel",
        ),
        description=_(
            "",
        ),
        default="",
        required=False,
        readonly=False,
    )


class ContacformprotectionControlPanel(RegistryEditForm):
    schema = IContacformprotectionControlPanel
    schema_prefix = (
        "collective.contactformprotection.contacformprotection_control_panel"
    )
    label = _("Contacformprotection Control Panel")


ContacformprotectionControlPanelView = layout.wrap_form(
    ContacformprotectionControlPanel, ControlPanelFormWrapper
)


@adapter(Interface, ICollectiveContactformprotectionLayer)
class ContacformprotectionControlPanelConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IContacformprotectionControlPanel
    configlet_id = "contacformprotection_control_panel-controlpanel"
    configlet_category_id = "Products"
    title = _("Contacformprotection Control Panel")
    group = ""
    schema_prefix = (
        "collective.contactformprotection.contacformprotection_control_panel"
    )
