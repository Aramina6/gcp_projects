from dask_management import DaskManagement
from data_processing import load_data, merge_data, calculate_risk_adjusted_profit
import dask.dataframe as dd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

if __name__ == "__main__":
    # Initialize Dask management
    dask_manager = DaskManagement(n_workers=4, threads_per_worker=2, memory_limit="4GB")

    # File paths
    financial_data_path = "financial_data.csv"
    geospatial_data_path = "geospatial_data.csv"

    # Load and process data
    financial_ddf, geospatial_ddf = load_data(financial_data_path, geospatial_data_path)
    merged_ddf = merge_data(financial_ddf, geospatial_ddf)
    merged_ddf = calculate_risk_adjusted_profit(merged_ddf)

    # Compute merged data to prepare for ML
    merged_df = merged_ddf.compute()

    # Prepare features and target
    features = merged_df.drop(columns=["issuer", "name", "country", "risk_adjusted_profit"])
    target = merged_df["risk_adjusted_profit"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Convert data to DMatrix for XGBoost
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    # Define XGBoost parameters
    params = {
        "objective": "reg:squarederror",
        "max_depth": 6,
        "eta": 0.1,
        "eval_metric": "rmse",
    }

    # Train the model
    evals = [(dtrain, "train"), (dtest, "test")]
    model = xgb.train(params, dtrain, num_boost_round=100, evals=evals, early_stopping_rounds=10)

    # Make predictions
    y_pred = model.predict(dtest)

    # Evaluate the model
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print(f"Root Mean Squared Error: {rmse}")

    # Save the trained model
    model.save_model("risk_adjusted_profit_model.json")

    # Shutdown the Dask cluster
    dask_manager.shutdown_cluster()
