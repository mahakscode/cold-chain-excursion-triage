
import pandas as pd
from detector import analyze_shipment

# Load the temperature readings and the answer key
readings = pd.read_csv("temperature_readings.csv")
answer_key = pd.read_csv("answer_key.csv")

results = []

# Analyze every shipment
for shipment_id, group in readings.groupby("shipment_id"):

    result = analyze_shipment(group)

    results.append({
        "shipment_id": shipment_id,
        "detected": result["flagged"],
        "peak_c": result["peak_c"],
        "lowest_c": result["lowest_c"],
        "minutes_out_of_range": result["minutes_out_of_range"]
    })

# Convert results into a table
results_df = pd.DataFrame(results)

# Compare the predictions with the known problems
evaluation = answer_key.merge(
    results_df,
    on="shipment_id"
)

print("\nSHIPMENT-BY-SHIPMENT EVALUATION")
print(
    evaluation[
        ["shipment_id", "problem", "detected"]
    ].to_string(index=False)
)

# Summarize detection results for each problem type
print("\nDETECTION SUMMARY")

summary = evaluation.groupby("problem").agg(
    total_shipments=("shipment_id", "count"),
    flagged_shipments=("detected", "sum")
)

summary["detection_rate_percent"] = (
    summary["flagged_shipments"]
    / summary["total_shipments"] * 100
).round(1)

print(summary)

# Count missed faults and false alarms
faults = evaluation["problem"] != "none"

missed = faults & (~evaluation["detected"])
false_alarms = (~faults) & evaluation["detected"]

print("\nTOTAL SHIPMENTS:", len(evaluation))
print("Known fault shipments:", int(faults.sum()))
print("Fault shipments detected:", int((faults & evaluation["detected"]).sum()))
print("Fault shipments missed:", int(missed.sum()))
print("False alarms on normal shipments:", int(false_alarms.sum()))

# Save results for future analysis
evaluation.to_csv("evaluation_results.csv", index=False)

print("\nEvaluation saved to evaluation_results.csv")