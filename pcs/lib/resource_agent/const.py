from pcs.common.resource_agent import const

from .types import (
    _FAKE_AGENT_STANDARD,
    FakeAgentName,
    OcfVersion,
)

OCF_1_0 = OcfVersion("1.0")
OCF_1_1 = OcfVersion("1.1")
SUPPORTED_OCF_VERSIONS = [OCF_1_0, OCF_1_1]

FAKE_AGENT_STANDARD = _FAKE_AGENT_STANDARD
PACEMAKER_BASED = FakeAgentName("pacemaker-based")
PACEMAKER_CONTROLD = FakeAgentName("pacemaker-controld")
PACEMAKER_FENCED = FakeAgentName("pacemaker-fenced")
PACEMAKER_SCHEDULERD = FakeAgentName("pacemaker-schedulerd")

STONITH_ACTION_REPLACED_BY = ["pcmk_off_action", "pcmk_reboot_action"]
DEFAULT_UNIQUE_GROUP_PREFIX = const.DEFAULT_UNIQUE_GROUP_PREFIX

# Alert agent instances
SMS_AGENT = FakeAgentName("alert-sms")
SMS_AGENT_METADATA = """<?xml version="1.0" encoding="utf-8"?>
<resource-agent name="alert-sms" version="1.0.0-beta">
  <version>1.1</version>
  <longdesc lang="en">
    This resource agent manages the alert-sms service, which sends SMS notifications.
  </longdesc>
  <shortdesc lang="en">SMS notification service manager</shortdesc>
  <parameters>
    <parameter name="enabled">
      <shortdesc lang="en">Enable or disable the SMS alert agent</shortdesc>
      <content type="boolean" default="1" />
    </parameter>
  </parameters>
  <actions>
    <action name="start" timeout="20" />
    <action name="stop" timeout="20" />
    <action name="meta-data" timeout="5" />
    <action name="monitor" depth="0" timeout="20" interval="10" />
  </actions>
</resource-agent>"""  # noqa: E501

SMTP_AGENT = FakeAgentName("alert-smtp")
SMTP_AGENT_METADATA = """<?xml version="1.0" encoding="utf-8"?>
<resource-agent name="alert-smtp" version="1.0.0-beta">
  <version>1.1</version>
  <longdesc lang="en">
    This resource agent manages the alert-smtp service, which sends email notifications.
  </longdesc>
  <shortdesc lang="en">Email notification service manager</shortdesc>
  <parameters>
    <parameter name="enabled">
      <shortdesc lang="en">Enable or disable the SMTP alert agent</shortdesc>
      <content type="boolean" default="1" />
    </parameter>
    <parameter name="hostname" required="1">
      <shortdesc lang="en">The SMTP server that handles the sending of your emails</shortdesc>
      <content type="string" />
    </parameter>
    <parameter name="port" required="1">
      <shortdesc lang="en">Port number</shortdesc>
      <content type="integer" default="25" />
    </parameter>
    <parameter name="username" required="1">
      <shortdesc lang="en">Email account username</shortdesc>
      <content type="string" />
    </parameter>
    <parameter name="password" required="1">
      <shortdesc lang="en">Email account password or passphrase</shortdesc>
      <content type="string" />
    </parameter>
  </parameters>
  <actions>
    <action name="start" timeout="20" />
    <action name="stop" timeout="20" />
    <action name="meta-data" timeout="5" />
    <action name="monitor" depth="0" timeout="20" interval="10" />
  </actions>
</resource-agent>"""  # noqa: E501

# Alert agent configuration registry
_ALERT_AGENT_CONFIG = {
    SMS_AGENT: SMS_AGENT_METADATA,
    SMTP_AGENT: SMTP_AGENT_METADATA,
}

# Public API - list_resource_agents
ALERT_AGENT = list(_ALERT_AGENT_CONFIG.keys())
ALERT_AGENT_METADATA = _ALERT_AGENT_CONFIG
