import asyncio
from typing import Any

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


MCP_SERVER_URL = "http://127.0.0.1:8000/mcp"


async def call_mcp_tool(
    tool_name: str,
    arguments: dict[str, Any],
) -> Any:

    async with streamable_http_client(MCP_SERVER_URL) as (
        read_stream,
        write_stream,
    ):
        async with ClientSession(
            read_stream,
            write_stream,
        ) as session:

            # Initialize the MCP connection
            await session.initialize()

            # Call the selected MCP tool
            result = await session.call_tool(
                tool_name,
                arguments=arguments,
            )

            return result


def run_mcp_tool(
    tool_name: str,
    arguments: dict[str, Any],
) -> Any:

    return asyncio.run(
        call_mcp_tool(
            tool_name,
            arguments,
        )
    )