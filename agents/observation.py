class ObservationAgent:
    def __init__(self):
        self.history = []

    def observe(self, row):
        self.history.append(row)

        # keep last 3 days
        if len(self.history) > 3:
            self.history.pop(0)

        avg_sleep = sum(d["sleep_hours"] for d in self.history) / len(self.history)
        avg_steps = sum(d["steps"] for d in self.history) / len(self.history)
        max_missed = max(d["missed_actions"] for d in self.history)

        # pattern classification
        if avg_sleep < 6:
            sleep_pattern = "low"
        elif avg_sleep > 7.5:
            sleep_pattern = "high"
        else:
            sleep_pattern = "normal"

        if avg_steps < 2000:
            activity_pattern = "low"
        elif avg_steps > 8000:
            activity_pattern = "high"
        else:
            activity_pattern = "normal"

        state = {
            "avg_sleep": avg_sleep,
            "avg_steps": avg_steps,
            "max_missed": max_missed,
            "sleep_pattern": sleep_pattern,
            "activity_pattern": activity_pattern
        }

        return state
