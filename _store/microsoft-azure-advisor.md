---
aid: microsoft-azure-advisor
name: Microsoft Azure Advisor
description: Microsoft Azure Advisor is a personalized cloud consultant that helps you follow best practices to optimize your Azure deployments. It analyzes your resource configuration and usage telemetry, then recommends solutions to improve the cost effectiveness, performance, reliability, security, and operational excellence of your Azure resources.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Advisor
  - Best Practices
  - Cost Optimization
  - Microsoft Azure
  - Optimization
  - Recommendations
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-advisor/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-azure-advisor:rest-api
    name: Azure Advisor REST API
    description: Azure Advisor REST API provides personalized recommendations for optimizing Azure deployments across reliability, security, performance, cost, and operational excellence. It supports retrieving recommendations, suppressing alerts, and configuring recommendation settings.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/advisor/
    baseURL: https://management.azure.com/
    tags:
      - Best Practices
      - Cost Optimization
      - Optimization
      - Recommendations
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/advisor/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/advisor/operation-groups
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-vs-authorization
      - type: SDK
        url: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/advisor
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/advisor/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: StatusPage
    url: https://status.azure.com/
  - type: GitHubOrganization
    url: https://github.com/Azure
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
