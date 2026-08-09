from typing import TypedDict, List, Dict


class GuardState(TypedDict):
    prompt: str
    intent: str
    reason: str
    security_concern: bool
    plan: List[str]
    selected_tools: List[str]
    tool_results: Dict