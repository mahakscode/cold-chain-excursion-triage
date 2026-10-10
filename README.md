# cold-chain-excursion-triage
Temperature anomaly detection and risk triage for simulated pharmaceutical cold-chain shipments

# Cold-Chain Excursion Triage

A Python-based prototype for detecting temperature excursions and generating risk alerts for simulated pharmaceutical cold-chain shipments.

## Problem Statement

Pharmaceutical products such as vaccines and insulin may require controlled temperatures during storage and transportation. Equipment failures, open doors, freezing events, and sensor glitches can cause abnormal temperature readings. This project aims to identify suspicious shipments and help prioritize them for further investigation.

## Solution

The prototype generates simulated shipment temperatures, injects different fault scenarios, detects sustained temperature excursions, calculates shipment-level risk features, and produces understandable risk alerts.

## Features

* Simulated temperature readings at five-minute intervals over 48 hours.
* Fault scenarios: door open, cooler failing, freezing, and sensor glitch.
* Rule-based temperature excursion detection using a configured 2–8°C range.
* Risk features including peak temperature, lowest temperature, and time outside the range.
* Shipment-level risk alerts.
* Evaluation against known simulated fault labels.

## Technologies Used

* Python
* NumPy
* Pandas
* Visual Studio Code

## Project Files

| File                     | Purpose                                                   |
| ------------------------ | --------------------------------------------------------- |
| `data_generator.py`      | Generates simulated temperature readings and fault labels |
| `detector.py`            | Detects temperature excursions and calculates features    |
| `evaluate.py`            | Evaluates detection results against known fault labels    |
| `risk_analyzer.py`       | Assigns prototype shipment risk alerts                    |
| `answer_key.csv`         | Contains simulated fault labels                           |
| `evaluation_results.csv` | Contains the initial evaluation results                   |

## How to Run

Install the required libraries:

```bash
python -m pip install numpy pandas
```

Generate the dataset:

```bash
python data_generator.py
```

Run temperature detection and evaluation:

```bash
python detector.py
python evaluate.py
```

Generate shipment risk alerts:

```bash
python risk_analyzer.py
```

Run the commands from the project folder. The scripts generate or read CSV files in that folder.

## Initial Evaluation

The initial test covered 25 simulated shipments:

* 4 out of 4 door-open shipments detected.
* 6 out of 6 cooler-failure shipments detected.
* 5 out of 5 freezing shipments detected.
* 2 isolated sensor glitches ignored.
* 0 false alarms among 8 normal shipments.

These are results from a small synthetic dataset and do not establish real-world accuracy.

## Future Scope

* Machine-learning classification of shipment conditions.
* Interactive Streamlit dashboard.
* Real-time temperature sensor integration.
* Product-specific temperature rules and improved testing.

## Important Note

This is an educational prototype using simulated data. Its alerts are not medical or pharmaceutical release decisions. Real shipment disposition requires approved product-specific guidance and qualified quality-team review.

