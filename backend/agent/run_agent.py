from graph import agent


prompt = input("Enter Prompt: ")


result = agent.invoke({
    "prompt": prompt,
    "intent": "",
    "reason": "",
    "security_concern": False,
    "plan": [],
    "selected_tools": [],
    "tool_results": {}
})


print("\n========== RESULT ==========")

print("Intent:")
print(result["intent"])

print()

print("Reason:")
print(result["reason"])

print()

print("Security Concern:")
print(result["security_concern"])

print()

print("Plan:")
print(result["plan"])

print()

print("Selected Tools:")
print(result["selected_tools"])