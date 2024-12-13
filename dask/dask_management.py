# dask_management.py
from dask.distributed import Client, LocalCluster
from data_processing import load_data, merge_data, calculate_risk_adjusted_profit, save_data

class DaskManagement:
    def __init__(self, n_workers=4, threads_per_worker=2, memory_limit="2GB"):
        self.cluster = LocalCluster(n_workers=n_workers, threads_per_worker=threads_per_worker, memory_limit=memory_limit)
        self.client = Client(self.cluster)

    def get_cluster_info(self):
        return self.cluster

    def get_client_info(self):
        return self.client

    def check_cluster_health(self):
        try:
            self.client.scheduler_info()
            return "Cluster is healthy"
        except Exception as e:
            return f"Cluster health check failed: {e}"

    def shutdown_cluster(self):
        self.client.close()
        self.cluster.close()

if __name__ == "__main__":
    # Initialize Dask management
    dask_manager = DaskManagement(n_workers=4, threads_per_worker=2, memory_limit="4GB")

    # Check cluster

