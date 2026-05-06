---
aid: microsoft-azure-cost-management
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/apis.yml
apis:
  - aid: microsoft-azure-cost-management:rest-api
    name: Azure Cost Management REST API
    tags:
      - Billing
      - Budget
      - Cost Management
      - FinOps
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/cost-management/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/cost-management/
        type: Documentation
    description: Azure Cost Management REST API enables programmatic access to cost analysis, budgets, exports, and recommendations. It supports querying usage data, creating budgets with alerts, scheduling cost exports, and retrieving optimization recommendations for cloud spending.
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
modified: '2026-04-28'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
description: Azure Cost Management provides programmatic access to cost analysis, budgets, exports, and recommendations across cloud spending. This collection documents the REST APIs that support multidimensional usage queries, budget alerts, scheduled cost exports, and FinOps optimization recommendations.
---
