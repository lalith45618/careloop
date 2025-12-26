import pandas as pd
from agents.observation import ObservationAgent
from agents.adaption import AdaptationAgent
from agents.planning import PlanningAgent
from agents.interaction import InteractionAgent


def run_careloop(dataset_path, label):
    print(f"\n--- Processing {label} ---")

    data = pd.read_csv(dataset_path)

    observation_agent = ObservationAgent()
    adaptation_agent = AdaptationAgent()
    planning_agent = PlanningAgent()
    interaction_agent = InteractionAgent()

    current_plan = planning_agent.initial_plan()
    print("Initial Plan:", current_plan)

    previous_day = None

    for _, row in data.iterrows():
        state = observation_agent.observe(row)
        adapt = adaptation_agent.should_adapt(state)

        if adapt:
            current_plan, reason = planning_agent.adapt_plan(state)

            if previous_day:
                print(
                    f"[ADAPTATION] Triggered by {previous_day} → "
                    f"{row['day']} plan updated."
                )

            message = interaction_agent.generate_message(True, reason)
            print("User Message:", message)
        else:
            message = interaction_agent.generate_message(False)
            print(f"[NO CHANGE] {row['day']}: {message}")

        previous_day = row["day"]

    print("Final Plan after", label, ":", current_plan)


if __name__ == "__main__":
    run_careloop("data/week_stable.csv", "Stable Week")
    run_careloop("data/week_disrupted.csv", "Disrupted Week")
