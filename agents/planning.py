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

        # explanation logic
        if state["sleep_pattern"] == "high" and state["activity_pattern"] == "low":
            reason = (
                "Excessive sleep combined with very low activity "
                "suggests disengagement or burnout."
            )

        elif state["sleep_pattern"] == "low" and state["activity_pattern"] == "high":
            reason = (
                "Low sleep combined with unusually high activity "
                "indicates overcompensation and routine instability."
            )

        elif state["sleep_pattern"] == "low":
            reason = (
                "Sustained sleep deficit is affecting routine stability."
            )

        else:
            reason = (
                "Repeated missed actions indicate declining engagement."
            )

        return new_plan, reason
