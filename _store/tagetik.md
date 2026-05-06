---
aid: tagetik
name: CCH Tagetik
description: CCH Tagetik (a Wolters Kluwer solution) is a comprehensive Corporate Performance Management platform covering financial close and consolidation, extended planning and analysis, ESG and regulatory reporting, and corporate tax management. The platform exposes data via OData v4 REST APIs and SCIM, enabling integration with Power BI, Qlik, SAP HANA, and other BI tools. OAuth 2.0 and Basic Authentication are supported for secure access.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Budgeting
  - Corporate Performance Management
  - ESG
  - Financial Close
  - Financial Consolidation
  - Financial Planning
  - OData
  - Reporting
created: '2025-01-15'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tagetik/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tagetik:cch-tagetik-odata-api
    name: CCH Tagetik OData API
    description: OData v4 REST API providing read access to CCH Tagetik financial and analytical workspace data. Enables external tools such as Power BI, Qlik, and custom integrations to query financial models, consolidation data, and analytical workspace datasets. Supports Basic Authentication and OAuth 2.0 Client Credentials flow. Available from CCH Tagetik Service Pack 23 (version 5.3+).
    humanURL: https://www.wolterskluwer.com/en/solutions/cch-tagetik/technology-integrations
    baseURL: https://{your-tagetik-environment}/
    tags:
      - Financial Data
      - Integration
      - OData
      - REST
    properties:
      - type: Documentation
        url: https://help.tagetik.com
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-query/connectors/wolters-kluwer-cch-tagetik
      - type: Power BI Connector
        url: https://learn.microsoft.com/en-us/power-query/connectors/wolters-kluwer-cch-tagetik
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tagetik/refs/heads/main/openapi/cch-tagetik-odata-openapi.yml
  - aid: tagetik:cch-tagetik-scim-api
    name: CCH Tagetik SCIM API
    description: SCIM v2 (System for Cross-domain Identity Management) API for automated user provisioning and deprovisioning in CCH Tagetik. Supports synchronizing users and groups from Microsoft Entra ID (Azure AD) and other identity providers.
    humanURL: https://www.wolterskluwer.com/en/solutions/cch-tagetik/technology-integrations
    baseURL: https://{your-tagetik-environment}/scim/v2
    tags:
      - Identity Management
      - SCIM
      - User Provisioning
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/azure/active-directory/saas-apps/cch-tagetik-tutorial
common:
  - type: Website
    url: https://www.wolterskluwer.com/en/solutions/cch-tagetik
  - type: Documentation
    url: https://help.tagetik.com
  - type: Technology Integrations
    url: https://www.wolterskluwer.com/en/solutions/cch-tagetik/technology-integrations
  - type: Support
    url: https://www.wolterskluwer.com/en/solutions/cch-tagetik/services/support
  - type: Power BI Integration
    url: https://learn.microsoft.com/en-us/power-query/connectors/wolters-kluwer-cch-tagetik
  - type: Azure AD SSO Tutorial
    url: https://learn.microsoft.com/azure/active-directory/saas-apps/cch-tagetik-tutorial
  - type: Training
    url: https://www.academy.registration.tagetik.com
  - type: JSON Schema
    url: https://raw.githubusercontent.com/api-evangelist/tagetik/refs/heads/main/json-schema/cch-tagetik-financial-record-schema.json
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/tagetik/refs/heads/main/vocabulary/tagetik-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
