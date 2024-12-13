import dask.dataframe as dd

def load_data(financial_data_path, geospatial_data_path):
    """
    Load financial and geospatial data as Dask DataFrames.
    """
    financial_ddf = dd.read_csv(financial_data_path)
    geospatial_ddf = dd.read_csv(geospatial_data_path)
    return financial_ddf, geospatial_ddf

def merge_data(financial_ddf, geospatial_ddf):
    """
    Merge financial data with geospatial data on latitude and longitude.
    """
    merged_ddf = dd.merge(
        financial_ddf,
        geospatial_ddf,
        how="inner",
        on=["latitude", "longitude"],
        suffixes=("_financial", "_geospatial")
    )
    return merged_ddf

def calculate_risk_adjusted_profit(merged_ddf):
    """
    Calculate risk-adjusted profit based on wildfire and cyclone probabilities.
    """
    def compute_adjusted_profit(row):
        wildfire_risk = row["wildfire_probability"]
        cyclone_risk = row["cyclone_probability"]
        profit_margin = row["profit_margin"]
        adjusted_profit = profit_margin * (1 - (wildfire_risk + cyclone_risk) / 2)
        return adjusted_profit

    merged_ddf["risk_adjusted_profit"] = merged_ddf.map_partitions(
        lambda df: df.apply(compute_adjusted_profit, axis=1),
        meta=("risk_adjusted_profit", "float")
    )
    return merged_ddf

def save_data(merged_ddf, output_path):
    """
    Compute and save the processed data to a CSV file.
    """
    merged_ddf.compute().to_csv(output_path, index=False)
