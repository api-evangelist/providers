---
aid: microsoft-azure-automation
name: Azure Automation
description: Learn how the Azure Automation service provides a highly reliable and scalable workflow execution engine to automate frequently repeated management tasks.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-automation/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
tags:
  - Automation
  - Configuration Management
  - Runbooks
  - Update Management
apis:
  - aid: microsoft-azure-automation:rest-api
    name: Azure Automation REST API
    tags:
      - Automation
      - Configuration Management
      - Runbooks
      - Update Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/automation/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/automation/
        type: Documentation
    description: Azure Automation REST API enables management of process automation through runbooks, desired state configuration, update management, and change tracking. It supports creating PowerShell and Python runbooks, scheduling jobs, managing credentials, and configuring hybrid workers.
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
