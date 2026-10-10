
import pandas as pd


def find_excursions(temperatures, low=2, high=8):
    """
    Find temperature readings outside the safe range.
    Flag a sustained excursion after 3 consecutive bad readings.
    """

    bad = (temperatures < low) | (temperatures > high)

    starts = []
    consecutive_bad = 0

    for index, is_bad in enumerate(bad):

        if is_bad:
            consecutive_bad += 1
        else:
            consecutive_bad = 0

        # Flag the start of a 3-reading sequence
        if consecutive_bad == 3:
            starts.append(index - 2)

    return starts, bad


def calculate_features(temperatures, bad):
    """Calculate useful measurements for shipment risk review."""

    return {
        "peak_c": round(float(temperatures.max()), 1),

        "lowest_c": round(float(temperatures.min()), 1),

        "minutes_out_of_range": int(bad.sum() * 5),

        "hours_above_8": round(
            float((temperatures > 8).sum() * 5 / 60), 2
        ),

        "hours_below_2": round(
            float((temperatures < 2).sum() * 5 / 60), 2
        )
    }


def analyze_shipment(readings):
    """Analyze all readings belonging to one shipment."""

    temperatures = readings["temperature_c"]

    starts, bad = find_excursions(temperatures)

    features = calculate_features(temperatures, bad)

    return {
        "flagged": len(starts) > 0,
        "excursion_starts": starts,
        **features
    }


# Test the detector on the generated dataset
data = pd.read_csv("temperature_readings.csv")

print("TEMPERATURE DETECTION RESULTS")

for shipment_id, readings in data.groupby("shipment_id"):

    result = analyze_shipment(readings)

    print("\nShipment:", shipment_id)
    print("Excursion detected:", result["flagged"])
    print("Peak temperature:", result["peak_c"], "C")
    print("Lowest temperature:", result["lowest_c"], "C")
    print(
        "Minutes out of range:",
        result["minutes_out_of_range"]
    )
    print("Hours above 8 C:", result["hours_above_8"])
    print("Hours below 2 C:", result["hours_below_2"])