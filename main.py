import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from engine.pipeline import analyze, print_result
from engine.conversation_guard import ConversationGuard

print("="*55)
print("   GUARD GPT - Intelligent Prompt Analysis Engine")
print("="*55)
print("Type your message and press Enter.")
print("Type 'quit' to exit | 'reset' to clear | 'history' to view")
print("="*55)

session = ConversationGuard(session_id="user_session_1")


def run():
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Goodbye! Stay safe!")
            break

        if user_input.lower() == "reset":
            session.reset()
            continue

        if user_input.lower() == "history":
            print("\nConversation History:")
            for turn in session.history:
                print(f"  Turn {turn['turn']}: {turn['action']} | {turn['prompt']}")
            continue

        if session.is_session_blocked():
            print("Session is blocked due to repeated unsafe messages.")
            continue

        result = analyze(user_input)
        session.add_turn(user_input, result["decision"]["action"])
        print_result(result)
        print(f"\nGuard GPT: {result['response']}")


if __name__ == "__main__":
    run()