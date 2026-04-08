---
aid: tagetik
url: https://raw.githubusercontent.com/api-evangelist/tagetik/refs/heads/main/apis.yml
apis:
- name: Tagetik REST API
  description: RESTful API for accessing Tagetik's CPM platform, enabling data integration, workflow automation, and reporting capabilities.
  image: https://www.tagetik.com/images/api-logo.png
  humanURL: https://www.tagetik.com/solutions/api
  baseURL: https://api.tagetik.com/v1
  tags:
  - Consolidation
  - Financial Data
  - Integration
  - REST
  properties:
  - type: Documentation
    url: https://docs.tagetik.com/api/rest
  - type: OpenAPI
    url: https://api.tagetik.com/v1/openapi.json
  - type: Authentication
    url: https://docs.tagetik.com/api/authentication
  - type: Rate Limits
    url: https://docs.tagetik.com/api/rate-limits
- name: Tagetik Data Integration API
  description: API for importing and exporting financial data, master data, and metadata from various source systems.
  humanURL: https://www.tagetik.com/solutions/data-integration
  baseURL: https://api.tagetik.com/v1/data
  tags:
  - Data Integration
  - ETL
  - Export
  - Import
  properties:
  - type: Documentation
    url: https://docs.tagetik.com/api/data-integration
  - type: SDK
    url: https://github.com/tagetik/sdk-data-integration
- name: Tagetik Workflow API
  description: API for managing and automating financial close workflows, approvals, and task management.
  humanURL: https://www.tagetik.com/solutions/workflow
  baseURL: https://api.tagetik.com/v1/workflow
  tags:
  - Approvals
  - Automation
  - Financial Close
  - Workflow
  properties:
  - type: Documentation
    url: https://docs.tagetik.com/api/workflow
  - type: Examples
    url: https://docs.tagetik.com/api/workflow/examples
- name: Tagetik Reporting API
  description: API for generating and retrieving financial reports, dashboards, and analytics.
  humanURL: https://www.tagetik.com/solutions/reporting
  baseURL: https://api.tagetik.com/v1/reporting
  tags:
  - Analytics
  - Dashboards
  - Financial Reports
  - Reporting
  properties:
  - type: Documentation
    url: https://docs.tagetik.com/api/reporting
  - type: Report Templates
    url: https://docs.tagetik.com/api/reporting/templates
name: Tagetik
tags:
- Analytics
- Corporate Performance Management
- Financial Consolidation
- Financial Planning
- Reporting
type: Contract
image: https://www.tagetik.com/images/logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs for Tagetik's Corporate Performance Management platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

