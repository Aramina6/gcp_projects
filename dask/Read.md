# **GeoRiskX: Dynamic Risk Analysis and Prediction**

## Overview
**GeoRiskX** is a scalable geospatial and financial risk analysis platform that leverages Dask on Kubernetes (GCP) for efficient data computation and integration. The project combines financial data of issuers and geospatial data on natural hazards to compute risk-adjusted profit predictions using machine learning (XGBoost).

This project is designed for organizations aiming to analyze the financial impact of environmental risks like wildfires and cyclones on facilities, enabling informed decision-making.

---

## Features
1. **Scalable Computing**:
   - Powered by **Dask**, a dynamic task scheduler optimized for parallel processing.
   - Runs on **Kubernetes** for elastic scaling on Google Cloud Platform (GCP).

2. **Data Integration**:
   - Merges financial data of issuers with geospatial hazard probabilities.
   - Handles large-scale data processing efficiently.

3. **Machine Learning Model**:
   - Predicts risk-adjusted profit using **XGBoost**, a state-of-the-art ML algorithm.
   - Provides insights into financial resilience against environmental risks.

4. **Dynamic Task Scheduling**:
   - Efficiently distributes computation across multiple workers.
   - Optimized for high throughput and reduced latency.

---

## Technology Stack
1. **Google Cloud Platform (GCP)**:
   - Kubernetes for container orchestration.
   - Cloud Storage for hosting input and output datasets.

2. **Dask**:
   - Dynamic task scheduler for parallelized data computation.
   - Manages workloads efficiently across distributed clusters.

3. **XGBoost**:
   - Used for predictive analytics on risk-adjusted profit.

4. **Python**:
   - Core programming language for data processing, task management, and modeling.

---

## Modules

### 1. `dask_management.py`
Manages the lifecycle of a Dask cluster, including:
   - Initialization of Dask client and workers.
   - Health checks and cluster shutdown operations.

### 2. `data_processing.py`
Handles data loading, merging, and computation:
   - Loads financial and geospatial datasets.
   - Merges datasets based on latitude and longitude.
   - Computes risk-adjusted profit metrics.

### 3. `xgboost_risk_model.py`
Trains an XGBoost model to predict risk-adjusted profit:
   - Utilizes the merged dataset.
   - Performs feature engineering and evaluation.

---

## How Dask Works
Dask is a flexible, parallel computing library designed for analytic computing. Its dynamic task scheduler optimizes computation by:
1. Breaking tasks into smaller chunks and executing them in parallel.
2. Dynamically allocating resources to maximize efficiency.
3. Scaling seamlessly from a single machine to distributed clusters.

In **GeoRiskX**, Dask handles:
   - Loading and processing large CSV datasets.
   - Merging datasets based on geospatial keys.
   - Parallelized feature computations for model preparation.

---

## Installation and Setup
### Prerequisites
1. **Python 3.8+**
2. **Google Cloud SDK** installed and authenticated.
3. **Kubernetes Cluster** set up on GCP.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/GeoRiskX.git
   cd GeoRiskX
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Dask cluster:
   ```bash
   python dask_management.py
   ```
4. Run the data processing pipeline:
   ```bash
   python xgboost_risk_model.py
   ```

---

## Example Use Case
1. **Input**:
   - Financial data of issuers including location, revenue, cost, and profit margins.
   - Geospatial data with probabilities of wildfire and cyclone occurrences.

2. **Output**:
   - A CSV file containing risk-adjusted profit predictions.
   - Insights into financial resilience to environmental risks.

---

## Future Work
- Integrate real-time geospatial data streams for dynamic risk analysis.
- Extend the model to include additional environmental risks like floods and earthquakes.
- Visualize results through a web-based dashboard.

---

## Contributing
We welcome contributions! Please fork the repository and submit a pull request with your enhancements.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

