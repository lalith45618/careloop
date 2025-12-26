class InteractionAgent:
    def generate_message(self, adapted, reason=None):
        if not adapted:
            return "Your routine is stable. No changes needed today."

        return (
            "Your plan has been adjusted to support routine stability. "
            + reason
        )
