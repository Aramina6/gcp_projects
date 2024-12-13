# Google Cloud Platform (GCP) Virtual Machine (Compute Engine)

Google Cloud Platform (GCP) offers **Compute Engine**, which provides virtual machines (VMs) that run on Google Cloud's infrastructure. It is a powerful service to run applications and workloads, providing scalable and customizable computing resources.

## Key Features of Compute Engine:
1. **Customizable VM Types**: Choose from predefined machine types or create custom configurations based on the number of CPUs and memory.
2. **Scalability**: Scale from small VMs for light workloads to large VMs for high-performance computing.
3. **Global Reach**: Deploy VMs in different regions worldwide, offering low-latency connections for your users.
4. **Persistent Disks**: Attach persistent storage, which retains data even after the VM is stopped or terminated.
5. **Preemptible VMs**: Cost-effective, short-lived instances ideal for fault-tolerant workloads.

## Key Components:
1. **Virtual Machines (VMs)**: Compute Engine provides VM instances with various operating systems and customizable specifications.
2. **Persistent Disks**: Storage for VM instances, available in SSD or HDD types.
3. **Images**: VMs can be created from different pre-built OS images or custom images.
4. **Networking**: Configure VMs with static or ephemeral external IPs and control the firewall rules.
5. **Metadata**: Apply metadata to VMs for instance-level settings.

## Regions and Zones in GCP Compute Engine:
GCP regions are independent geographical locations where resources can be deployed. Each region contains multiple zones.

### **Region List**:
Here are some GCP regions and zones available globally:

- **us-central1**: Iowa (zone: `us-central1-a`, `us-central1-b`, `us-central1-c`, etc.)
- **us-west1**: Oregon
- **us-east1**: South Carolina
- **europe-west1**: Belgium
- **asia-east1**: Taiwan
- **australia-southeast1**: Sydney
- **southamerica-east1**: São Paulo

### Common Regions and Zones Commands:
- **List available regions**:
    ```bash
    gcloud compute regions list
    ```
- **List available zones**:
    ```bash
    gcloud compute zones list
    ```

## VM Machine Types:
Compute Engine provides **Predefined** and **Custom machine types**.

### 1. **Predefined Machine Types**:
- **N1 Standard**: Balanced CPUs and memory (e.g., `n1-standard-1`, `n1-standard-2`).
- **N2 Standard**: More memory per core, newer hardware (e.g., `n2-standard-4`).
- **C2 Standard**: High-performance computing (e.g., `c2-standard-4`).
- **M2**: Memory optimized (e.g., `m2-ultramem-416`).
- **T2D**: Cost-optimized VMs (e.g., `t2d-standard-2`).

### 2. **Custom Machine Types**:
Allows you to configure the number of vCPUs and memory based on your needs.

Example: To create a custom machine with 4 vCPUs and 16GB RAM:
```bash
gcloud compute instances create my-instance --custom-cpu=4 --custom-memory=16GB --zone=us-central1-a
