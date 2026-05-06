---
aid: microsoft-azure-batch
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/apis.yml
apis:
  - aid: microsoft-azure-batch:rest-api
    name: Azure Batch REST API
    tags:
      - Batch Computing
      - HPC
      - Job Scheduling
      - Parallel Processing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://batch.core.windows.net/
    humanURL: https://learn.microsoft.com/en-us/rest/api/batchservice/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/batchservice/
        type: Documentation
    description: Azure Batch REST API provides management of large-scale parallel and high-performance computing workloads. It supports creating pools of compute nodes, submitting jobs and tasks, auto-scaling based on workload, and managing task dependencies for batch processing scenarios.
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
created: '2026-03-13'
modified: '2026-04-28'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
description: Learn how to use the Azure Batch API to schedule and run large scale computational workloads.
---
