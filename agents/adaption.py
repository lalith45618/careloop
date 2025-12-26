class AdaptationAgent:
    def should_adapt(self, state):
        # repeated disengagement
        if state["max_missed"] >= 2:
            return True

        # instability in core routines
        if state["sleep_pattern"] != "normal":
            return True

        if state["activity_pattern"] != "normal":
            return True

        return False
