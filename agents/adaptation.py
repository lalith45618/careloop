class AdaptationAgent:
    def should_adapt(self, state):
        # check today's missed actions, not max in window
        today_missed = state.get("today_missed", 0)
        if today_missed >= 2:
            return True, "missed_actions"

        if state["sleep_pattern"] != "normal":
            return True, "sleep_instability"

        if state["activity_pattern"] != "normal":
            return True, "activity_instability"

        return False, None
