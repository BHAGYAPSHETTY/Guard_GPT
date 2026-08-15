from graph import agent


prompt = input("Enter Prompt: ")


result = agent.invoke({

    "prompt": prompt,

    "intent": "",

    "confidence": 0.0,

    "reason": "",

    "security_concern": False,

    "plan": [],

    "selected_tools": [],

    "tool_results": {},

    "engine_result": {}
})


print("\n========== RESULT ==========")

print("Prompt:")
print(prompt)

print()

print("Intent:")
print(result["intent"])

print()

print("Confidence:")
print(result["confidence"])

print()

print("Reason:")
print(result["reason"])

print()

print("Security Concern:")
print(result["security_concern"])

print()

print("Plan:")
for item in result["plan"]:
    print("-", item)

print()

print("Selected Tools:")
for tool in result["selected_tools"]:
    print("-", tool)

print()

print("Tool Results:")
print(result["tool_results"])