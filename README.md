# Cloud Backup App

This is the **Flask API backend** for our Cloud Backup Service project.  
It allows users to upload, list, and restore files stored in **Amazon S3**.  
(Currently, only `/upload` is fully implemented with AWS integration.)

---

## ✅ Features (so far)
- `/health` → returns `{ "status": "ok" }`  
- `/upload` → uploads a file to S3 bucket (`cloud-backup-jason123`)  
- `/list` → (dummy version for now, real S3 integration coming soon)  
- `/restore` → (dummy version for now)  
- Dockerized for containerized deployment  

---

## ⚙️ Setup Instructions

### 1. Clone Repo
```bash
git clone https://github.com/<your-username>/cloud-backup-app.git
cd cloud-backup-app


