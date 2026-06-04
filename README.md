# Contractor Bid Plausibility Checker

A data-driven Decision Support System (DSS) built with Streamlit to evaluate the economic plausibility of contractor bids.

The application calculates a minimum cost baseline based on material costs and statutory labor requirements. Contractor bids are compared against this baseline to identify potentially unrealistic pricing, wage dumping, or calculation errors.

## Features

* Dynamic Bill of Materials (BoM) input
* Dynamic labor requirement input
* Automated material cost estimation
* Automated statutory labor cost calculation
* Real-time bid plausibility assessment
* Transparent and explainable decision logic

## How It Works

The system calculates:

Minimum Cost Baseline = Material Costs + Required Labor Costs

A bid is classified as:

* **Plausible** when the bid meets or exceeds the minimum cost baseline.
* **Red Flag** when the bid falls below the minimum cost baseline.

The baseline is intentionally limited to objective and verifiable cost components and excludes factors such as profit margins, market conditions, and contractor-specific business strategies.

## Tech Stack

* Python
* Streamlit
* Pandas

## Running Locally

Install dependencies:

```bash
pip install streamlit pandas
```

Start the application:

```bash
streamlit run app.py
```

## Disclaimer

This project is a proof of concept and is intended as a decision-support tool for bid evaluation. A red flag indicates that a bid may require further investigation and should not be interpreted as evidence of non-compliance or misconduct.