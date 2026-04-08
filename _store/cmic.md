---
aid: cmic
url: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/apis.yml
apis:
- aid: cmic:cmic-api
  name: CMiC Construction ERP API
  tags:
  - Construction
  - ERP
  - Finance
  - OAuth2
  - Project Management
  image: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/image.png
  humanURL: https://developers.cmicglobal.com/
  baseURL: https://api.cmic.ca
  properties:
  - url: https://developers.cmicglobal.com/docs/overview
    type: Documentation
  - url: https://developers.cmicglobal.com/v1/docs/authentication
    type: Authentication
  - url: https://developers.cmicglobal.com/docs/developer-api-account
    type: GettingStarted
  - url: https://docs.cmicglobal.com/portal/Content/E_Reference_Material/CMiC_API/Reference/API_and_OAuth2/API_and_OAuth2.htm
    type: Reference
  - url: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/openapi/cmic-construction-erp-openapi.yml
    type: OpenAPI
  description: CMiC provides enterprise ERP and project management software for the construction industry. The REST API uses OAuth 2.0 (client credentials flow) with support for third-party identity providers like Microsoft Azure. APIs enable access to project financials, subcontractor management, job costing, equipment tracking, and document management. Application-level security is enforced across all endpoints respecting company, job, project, and employee access rules.
- aid: cmic:cmic-power-bi-connector
  name: CMiC API Power BI Connector
  tags:
  - Analytics
  - Business Intelligence
  - Construction
  - ERP
  - Power BI
  image: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/image.png
  humanURL: https://docs.cmicglobal.com/portal/Content/Home.htm
  baseURL: https://api.cmic.ca
  properties:
  - url: https://docs.cmicglobal.com/portal/Content/Home.htm
    type: Documentation
  description: CMiC's Power BI Connector allows users to connect Microsoft Power BI directly to CMiC ERP data through the CMiC API, enabling business intelligence dashboards and reports for construction project financials, job costing, and operational metrics.
name: Cmic
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Creating an API Service Account.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

