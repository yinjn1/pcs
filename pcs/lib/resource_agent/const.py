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

ALERT_AGENT_SMS = FakeAgentName("alert_sms")
ALERT_AGENT_SMS_METADATA = """<?xml version="1.0"?>
<resource-agent name="alert_sms" version="1.0">
  <version>1.0</version>
  <shortdesc lang="en">Alert agent for SMS</shortdesc>
  <longdesc lang="en">alert_sms is an alert agent which can be used to send SMS notifications. This agent calls support software to send SMS messages.</longdesc>
  <parameters>
  </parameters>
  <actions>
  </actions>
</resource-agent>"""

ALERT_AGENT_SMTP = FakeAgentName("alert_smtp")
ALERT_AGENT_SMTP_METADATA = """<?xml version="1.0"?>
<resource-agent name="alert_smtp" version="1.0">
  <version>1.0</version>
  <shortdesc lang="en">Alert agent for SMTP</shortdesc>
  <longdesc lang="en">alert_smtp is an alert agent which can be used to send email notifications via SMTP. This agent calls support software to send email messages.</longdesc>
  <parameters>
    <parameter name="smtp_server_host" required="1">
      <shortdesc lang="en">IP address or hostname of SMTP server</shortdesc>
      <content type="string" />
    </parameter>
    <parameter name="smtp_server_port" required="1">
      <shortdesc lang="en">TCP/UDP port to use for connection with SMTP server</shortdesc>
      <content type="port" default="25" />
    </parameter>
    <parameter name="smtp_auth_username" required="1">
      <shortdesc lang="en">Email account username</shortdesc>
      <content type="string" />
    </parameter>
    <parameter name="smtp_auth_password" required="1">
      <shortdesc lang="en">Email account password or passphrase</shortdesc>
      <content type="string" />
    </parameter>
  </parameters>
  <actions>
  </actions>
</resource-agent>"""

# list_resource_agents
ALERT_AGENT = [
    ALERT_AGENT_SMS,
    ALERT_AGENT_SMTP,
]

ALERT_AGENT_METADATA = {
    ALERT_AGENT_SMS: ALERT_AGENT_SMS_METADATA,
    ALERT_AGENT_SMTP: ALERT_AGENT_SMTP_METADATA,
}
