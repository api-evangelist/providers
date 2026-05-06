---
aid: microsoft-azure-site-recovery
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-site-recovery/refs/heads/main/apis.yml
name: Azure Site Recovery
description: Azure Site Recovery REST API provides management of disaster recovery for Azure VMs, on-premises VMs, and physical servers. It supports configuring replication, running test failovers, executing planned and unplanned failovers, and managing recovery plans.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Disaster Recovery
  - Replication
  - Business Continuity
  - Failover
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: microsoft-azure-site-recovery:rest-api
    name: Azure Site Recovery REST API
    description: Azure Site Recovery REST API provides management of disaster recovery for Azure VMs, on-premises VMs, and physical servers. It supports configuring replication, running test failovers, executing planned and unplanned failovers, and managing recovery plans.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/site-recovery/
    baseURL: https://management.azure.com/
    tags:
      - Disaster Recovery
      - Replication
      - Failover
      - Recovery Plans
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/site-recovery/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-flows-app-scenarios
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/site-recovery/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/site-recovery/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-quickstart
  - type: Status
    url: https://azure.status.microsoft/en-us/status
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/product/site-recovery/
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-site-recovery
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
