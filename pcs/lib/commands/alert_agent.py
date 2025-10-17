from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from pcs.lib.commands.resource_agent import (
    _agent_metadata_to_dict,
    _complete_agent_list,
)
from pcs.lib.env import LibraryEnvironment
from pcs.lib.errors import LibraryError
from pcs.lib.resource_agent import (
    InvalidResourceAgentName,
    ResourceAgentError,
    ResourceAgentFacadeFactory,
    ResourceAgentName,
    resource_agent_error_to_report_item,
    types as ra_types,
    const as ra_const,
)


def list_agents(
    lib_env: LibraryEnvironment,
    describe: bool = True,
    search: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    List all alert agents on the local host, optionally filtered and described

    describe -- load and return agents' description as well
    search -- return only agents which name contains this string
    """
    runner = lib_env.cmd_runner()
    agent_names = [
        ResourceAgentName("alert", None, agent_name)
        for agent_name in ra_const.ALERT_AGENT
    ]

    return _complete_agent_list(
        runner,
        lib_env.report_processor,
        sorted(agent_names, key=lambda item: item.full_name),
        describe,
        search,
    )


def describe_agent(
    lib_env: LibraryEnvironment, agent_name: str
) -> Dict[str, Any]:
    """
    Get agent's description (metadata) in a structure

    agent_name -- name of the agent (not containing "alert:" prefix)
    """
    runner = lib_env.cmd_runner()
    agent_factory = ResourceAgentFacadeFactory(runner, lib_env.report_processor)
    try:
        if ":" in agent_name:
            raise InvalidResourceAgentName(agent_name)
        return _agent_metadata_to_dict(
            agent_factory.facade_from_alert_agent_name(
                ra_types.FakeAgentName(agent_name)
            ).metadata,
            describe=True,
        )
    except ResourceAgentError as e:
        lib_env.report_processor.report(
            resource_agent_error_to_report_item(e)
        )
        raise LibraryError() from e
