class PlanningAgent:
    def initial_plan(self):
        return {
            "activity_level": "moderate",
            "focus": "balanced"
        }

    def adapt_plan(self, state):
        new_plan = {
            "activity_level": "light",
            "focus": "routine_stability"
        }

        # Dynamic reason generation based on today's data
        reasons = []

        # Check today’s sleep
        if state["today_sleep"] < 3:
            reasons.append(f"Severely low sleep today ({state['today_sleep']}h)")
        elif state["today_sleep"] < 6:
            reasons.append(f"Sustained sleep deficit today ({state['today_sleep']}h)")

        # Check today’s activity
        if state["today_steps"] < 2000:
            reasons.append(f"Very low activity today ({state['today_steps']} steps)")

        # Check today’s missed actions
        if state["today_missed"] >= 2:
            reasons.append("Multiple missed actions today")

        # Fallback for trend-based instability
        if state["sleep_pattern"] != "normal" or state["activity_pattern"] != "normal":
            if not reasons:
                reasons.append("Routine instability detected based on recent behavior")

        reason_message = " & ".join(reasons)
        return new_plan, reason_message
