
import numpy as np
import pandas as pd

# Make the random results repeatable
np.random.seed(42)

# 48 hours, with one reading every 5 minutes
N = 576


def normal_trace():
    """Create a normal temperature pattern around 5 degrees."""
    t = np.arange(N)

    temperature = (
        5
        + 0.8 * np.sin(2 * np.pi * t / 288)
        + np.random.normal(0, 0.25, N)
    )

    return temperature


# Problem 1: a door is left open
def door_open(temperature, at):
    temperature[at:at + 4] += 5


# Problem 2: the cooler slowly stops working
def cooler_failing(temperature, at):
    rise = np.minimum(
        np.arange(N - at) * 0.03, 12
    )
    temperature[at:] += rise


# Problem 3: the shipment freezes
def freeze(temperature, at):
    temperature[at:at + 30] = -2


# Problem 4: one incorrect sensor reading
def glitch(temperature, at):
    temperature[at] = 30


problems = {
    "door_open": door_open,
    "cooler_failing": cooler_failing,
    "freeze": freeze,
    "glitch": glitch,
    "none": None
}

shipments = []
answer_key = []

for shipment_id in range(1, 26):

    # Start with normal temperatures
    temperature = normal_trace()

    # Choose a problem type
    problem = np.random.choice(
        list(problems.keys()),
        p=[0.20, 0.20, 0.15, 0.15, 0.30]
    )

    # Choose when the problem starts
    if problems[problem] is not None:
        start = np.random.randint(50, 400)
        problems[problem](temperature, start)

    # Store every reading
    shipment_data = pd.DataFrame({
        "shipment_id": shipment_id,
        "time_minutes": np.arange(N) * 5,
        "temperature_c": temperature
    })

    shipments.append(shipment_data)

    # Save the correct answer separately
    answer_key.append({
        "shipment_id": shipment_id,
        "problem": problem
    })


# Combine all shipment readings into one table
all_readings = pd.concat(shipments, ignore_index=True)

# Save both files
all_readings.to_csv("temperature_readings.csv", index=False)

pd.DataFrame(answer_key).to_csv(
    "answer_key.csv", index=False
)

print("Dataset created successfully!")
print("Number of shipments:", len(shipments))
print("Total temperature readings:", len(all_readings))
print("\nKnown problems:")
print(pd.DataFrame(answer_key)["problem"].value_counts())