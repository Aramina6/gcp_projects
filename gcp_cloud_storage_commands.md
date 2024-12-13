# Google Cloud Storage Commands Notebook

## 1. Prerequisites
```bash
# Install Google Cloud SDK from https://cloud.google.com/sdk/docs/install
gcloud auth login

# Set your project ID
gcloud config set project [PROJECT_ID]
```

## 2. Basic Cloud Storage Commands

### Create a Bucket
```bash
gsutil mb -l [REGION] gs://[BUCKET_NAME]/
```
Example:
```bash
gsutil mb -l us-central1 gs://my-storage-bucket/
```

### List Buckets
```bash
gsutil ls
```

### Upload Files to Bucket
```bash
gsutil cp [LOCAL_FILE_PATH] gs://[BUCKET_NAME]/
```
Example:
```bash
gsutil cp file.txt gs://my-storage-bucket/
```

### Download Files from Bucket
```bash
gsutil cp gs://[BUCKET_NAME]/[FILE_NAME] [LOCAL_PATH]
```
Example:
```bash
gsutil cp gs://my-storage-bucket/file.txt ./downloaded_file.txt
```

### List Files in a Bucket
```bash
gsutil ls gs://[BUCKET_NAME]/
```
Example:
```bash
gsutil ls gs://my-storage-bucket/
```

### Delete a File from Bucket
```bash
gsutil rm gs://[BUCKET_NAME]/[FILE_NAME]
```
Example:
```bash
gsutil rm gs://my-storage-bucket/file.txt
```

### Delete a Bucket
```bash
gsutil rb gs://[BUCKET_NAME]
```
> **Note**: The bucket must be empty before deletion.

## 3. Setting Permissions

### Make Bucket Public
```bash
gsutil iam ch allUsers:objectViewer gs://[BUCKET_NAME]
```

### View Permissions
```bash
gsutil iam get gs://[BUCKET_NAME]
```

### Revoke Public Access
```bash
gsutil iam ch -d allUsers:objectViewer gs://[BUCKET_NAME]
```

## 4. Advanced Commands

### Synchronize Local Folder with Bucket
```bash
gsutil rsync -r [LOCAL_FOLDER_PATH] gs://[BUCKET_NAME]
```
Example:
```bash
gsutil rsync -r ./local_folder gs://my-storage-bucket
```

### Copy Between Buckets
```bash
gsutil cp gs://[SOURCE_BUCKET]/[FILE_NAME] gs://[DEST_BUCKET]/[FILE_NAME]
```
Example:
```bash
gsutil cp gs://source-bucket/file.txt gs://destination-bucket/file.txt
```

### Set Bucket Lifecycle Rules
Create a JSON file defining lifecycle rules (e.g., to delete objects older than 30 days):
```json
{
  "rule": [
    {
      "action": {"type": "Delete"},
      "condition": {"age": 30}
    }
  ]
}
```
Apply rules:
```bash
gsutil lifecycle set [RULE_FILE] gs://[BUCKET_NAME]
```
Example:
```bash
gsutil lifecycle set lifecycle.json gs://my-storage-bucket
```

### Change Default Storage Class
```bash
gsutil defstorageclass set [STORAGE_CLASS] gs://[BUCKET_NAME]
```
Options: `STANDARD`, `NEARLINE`, `COLDLINE`, `ARCHIVE`.

## 5. Monitoring and Logs

### Enable Logging
```bash
gsutil logging set on -b gs://[LOG_BUCKET] gs://[BUCKET_NAME]
```

### View Logs
Logs are stored in the specified log bucket. Use:
```bash
gsutil ls gs://[LOG_BUCKET]
```

## 6. Interact Using `gcloud` CLI

### Create a Bucket
```bash
gcloud storage buckets create [BUCKET_NAME] --location=[REGION]
```

### Upload a File
```bash
gcloud storage cp [LOCAL_FILE_PATH] gs://[BUCKET_NAME]/
```

### List Buckets
```bash
gcloud storage buckets list
```

### Delete a Bucket
```bash
gcloud storage buckets delete [BUCKET_NAME]
```

## 7. Automating with a Script
Example Bash script for automating uploads:
```bash
#!/bin/bash

BUCKET_NAME="my-storage-bucket"
FILES=("file1.txt" "file2.txt")

for FILE in "${FILES[@]}"; do
  gsutil cp "$FILE" gs://"$BUCKET_NAME"/
  echo "Uploaded $FILE to $BUCKET_NAME"
done
