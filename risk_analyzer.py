
import pandas as pd

from detector import analyze_shipment

# Load our simulated temperature readings
data = pd.read_csv("temperature_readings.csv")

print("COLD-CHAIN SHIPMENT RISK REPORT")
print("=" * 45)

for shipment_id, readings in data.groupby("shipment_id"):

    result = analyze_shipment(readings)

    peak = result["peak_c"]
    lowest = result["lowest_c"]
    outside_minutes = result["minutes_out_of_range"]
    flagged = result["flagged"]

    # Simple prototype risk classification
    if lowest < 0:
        risk = "HIGH RISK - FREEZING ALERT"

    elif outside_minutes >= 30:
        risk = "HIGH RISK - SUSTAINED EXCURSION"

    elif flagged:
        risk = "REVIEW - TEMPERATURE EXCURSION"

    else:
        risk = "NORMAL - NO SUSTAINED EXCURSION"

    print(f"\nShipment ID: {shipment_id}")
    print(f"Peak temperature: {peak} C")
    print(f"Lowest temperature: {lowest} C")
    print(f"Time out of range: {outside_minutes} minutes")
    print(f"Risk status: {risk}")