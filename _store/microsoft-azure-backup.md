---
aid: microsoft-azure-backup
name: Azure Backup
description: Learn how Azure Backup contributes to your business continuity and disaster recovery (BCDR) strategy by backing up data to the Azure clouds.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-backup/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
tags:
  - Backup
  - Data Protection
  - Disaster Recovery
  - Recovery Services
apis:
  - aid: microsoft-azure-backup:rest-api
    name: Azure Backup REST API
    tags:
      - Backup
      - Data Protection
      - Disaster Recovery
      - Recovery Services
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/backup/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/backup/
        type: Documentation
    description: Azure Backup REST API enables programmatic management of backup policies, protected items, recovery points, and restore operations. It supports backing up VMs, SQL databases, file shares, and SAP HANA workloads through Recovery Services vaults.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
