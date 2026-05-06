---
aid: microsoft-azure-data-factory
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/apis.yml
apis:
  - aid: microsoft-azure-data-factory:rest-api
    name: Azure Data Factory REST API
    tags:
      - Data Integration
      - Data Pipeline
      - ETL
      - Orchestration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/datafactory/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/datafactory/
        type: Documentation
    description: Azure Data Factory REST API enables programmatic management of data integration pipelines for orchestrating data movement and transformation at scale. It supports creating pipelines, datasets, linked services, triggers, and data flows for ETL and ELT workloads across cloud and on-premises data stores.
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
description: Azure Data Factory is a cloud-based data integration service that orchestrates and automates the movement and transformation of data. This collection documents the REST APIs for managing pipelines, datasets, linked services, triggers, and data flows across ETL and ELT workloads spanning cloud and on-premises stores.
---
