from mcp_client import run_mcp_tool


result = run_mcp_tool(
    "audit_logger",
    {
        "data": {
            "prompt": "I want to commit suicide.",
            "tool_name": "content_moderation",
            "result": {
                "is_unsafe": True,
                "categories": ["self_harm"],
                "severity": "high"
            }
        }
    }
)

print("\n========== AUDIT LOGGER RESULT ==========")
print(result)