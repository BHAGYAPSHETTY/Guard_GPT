class ConversationGuard:
    def __init__(self, session_id):
        self.session_id = session_id
        self.history = []
        self.turn_count = 0
        self.is_flagged = False

    def add_turn(self, prompt, action):
        self.turn_count += 1
        self.history.append({
            "turn": self.turn_count,
            "prompt": prompt[:80],
            "action": action
        })
        blocked_count = sum(1 for t in self.history if t["action"] == "BLOCK")
        if len(self.history) >= 3:
            ratio = blocked_count / len(self.history)
            if ratio >= 0.7:
                self.is_flagged = True

    def is_session_blocked(self):
        return self.is_flagged

    def reset(self):
        self.history = []
        self.turn_count = 0
        self.is_flagged = False
        print("Session history cleared.")