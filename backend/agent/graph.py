from langgraph.graph import StateGraph, END

from state import GuardState

from nodes import (
    understand_prompt,
    security_check,
    create_plan,
    select_tools,
    execute_tools
)


workflow = StateGraph(GuardState)


workflow.add_node(
    "Understand",
    understand_prompt
)

workflow.add_node(
    "SecurityCheck",
    security_check
)

workflow.add_node(
    "Plan",
    create_plan
)

workflow.add_node(
    "Tools",
    select_tools
)

workflow.add_node(
    "ExecuteTools",
    execute_tools
)


workflow.set_entry_point("Understand")

workflow.add_edge(
    "Understand",
    "SecurityCheck"
)

workflow.add_edge(
    "SecurityCheck",
    "Plan"
)

workflow.add_edge(
    "Plan",
    "Tools"
)

workflow.add_edge(
    "Tools",
    "ExecuteTools"
)

workflow.add_edge(
    "ExecuteTools",
    END
)


agent = workflow.compile()