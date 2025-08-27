# Cloud Backup App

# Cloud Backup App

This is the **Flask API backend** for the Cloud Backup Service project.  
It allows users to upload, list, and restore files stored in **Amazon S3**.  
(Currently, `/health`, `/upload`, and `/list` are implemented.)

---

## ✅ Features (so far)
- `/health` → returns `{ "status": "ok" }`
- `/upload` → uploads a file to S3 bucket (from `.env` config)
- `/list` → lists files in the S3 bucket with metadata:
  - filename
  - size (bytes)
  - last_modified timestamp
- `/restore` → (coming soon, will use S3 versioning)
- Dockerized for containerized deployment
- Supports **Docker Compose** for easy setup

---

## ⚙️ Setup Instructions

### 1. Clone Repo
```bash
git clone https://github.com/<your-username>/cloud-backup-app.git
cd cloud-backup-app



