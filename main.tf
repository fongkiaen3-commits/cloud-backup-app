provider "aws" {
  region = "ap-southeast-2"
}

resource "aws_backup_vault" "cloud_backup_vault" {
  name = "cloud-backup-app-vault"
  tags = {
    Project = "CloudBackupApp"
    Owner   = "DevOpsTeam"
  }
}

resource "aws_backup_plan" "cloud_backup_plan" {
  name = "cloud-backup-plan"

  rule {
    rule_name         = "daily-backup"
    target_vault_name = aws_backup_vault.cloud_backup_vault.name
    schedule          = "cron(0 12 * * ? *)"
    lifecycle {
      delete_after = 30
    }
  }

  tags = {
    Project = "CloudBackupApp"
  }
}

