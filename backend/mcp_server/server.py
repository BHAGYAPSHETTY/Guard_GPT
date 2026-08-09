from mcp.server import MCPServer

from models.schemas import (
    PromptAnalysisInput,
    PromptAnalysisOutput,
    JailbreakDetectionInput,
    JailbreakDetectionOutput,
    ContentModerationInput,
    ContentModerationOutput,
    AuditLoggerInput,
    AuditLoggerOutput,
)

from tools.prompt_analysis import analyze_prompt
from tools.jailbreak_detection import detect_jailbreak
from tools.content_moderation import moderate_content
from tools.audit_logger import log_audit_event


# ============================================================
# Create MCP Server
# ============================================================

mcp = MCPServer(
    name="GuardGPT MCP Server",
    version="1.0.0",
    description=(
        "Security tools for the GuardGPT LangGraph Agent."
    ),
)


# ============================================================
# Tool 1: prompt_analysis
# ============================================================

@mcp.tool(
    name="prompt_analysis",
    description=(
        "Analyze a user's prompt and classify it into "
        "Greeting, Self-Harm, Programming, Cybersecurity, "
        "Suspicious, or General."
    ),
)
def prompt_analysis(
    data: PromptAnalysisInput,
) -> PromptAnalysisOutput:
    return analyze_prompt(data)


# ============================================================
# Tool 2: jailbreak_detection
# ============================================================

@mcp.tool(
    name="jailbreak_detection",
    description=(
        "Detect common jailbreak and prompt-injection "
        "patterns in a user's prompt."
    ),
)
def jailbreak_detection(
    data: JailbreakDetectionInput,
) -> JailbreakDetectionOutput:
    return detect_jailbreak(data)


# ============================================================
# Tool 3: content_moderation
# ============================================================

@mcp.tool(
    name="content_moderation",
    description=(
        "Check a user's prompt for potentially unsafe "
        "content categories."
    ),
)
def content_moderation(
    data: ContentModerationInput,
) -> ContentModerationOutput:
    return moderate_content(data)


# ============================================================
# Tool 4: audit_logger
# ============================================================

@mcp.tool(
    name="audit_logger",
    description=(
        "Record a security-tool execution and its result "
        "in the GuardGPT audit log."
    ),
)
def audit_logger(
    data: AuditLoggerInput,
) -> AuditLoggerOutput:
    return log_audit_event(data)


# ============================================================
# Start Server
# ============================================================

if __name__ == "__main__":
    print("Starting GuardGPT MCP Server...")
    print("Transport: Streamable HTTP")
    print("Endpoint: http://127.0.0.1:8000/mcp")

    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8000,
    )