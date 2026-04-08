---
aid: dnv
url: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/apis.yml
apis:
- aid: dnv:dnv-class-status-api
  name: DNV Class Status API
  tags:
  - Azure AD
  - Classification
  - Maritime
  - OAuth2
  - Safety
  - Vessel
  image: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/image.png
  humanURL: https://maritime.dnv.com/api/cs-iacs-customer
  baseURL: https://maritime.dnv.com/api/cs-iacs-customer
  properties:
  - url: https://maritime.dnv.com/api/cs-iacs-customer/docs/index.html
    type: Reference
  - url: https://maritime.dnv.com/api/cs-iacs-customer
    type: Documentation
  - url: https://maritime.dnv.com/api/cs-iacs-customer
    type: Authentication
  - url: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/openapi/dnv-class-status-openapi.yml
    type: OpenAPI
  description: DNV's Class Status API provides programmatic access to vessel classification data. Authentication uses OAuth 2.0 with Azure AD B2C as the identity provider. Access tokens are obtained from https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token and are valid for approximately 20 minutes. Access requires a separate API contract with DNV.
- aid: dnv:dnv-veracity-api
  name: DNV Veracity Platform API
  tags:
  - Analytics
  - Data Platform
  - Energy
  - IoT
  - Maritime
  image: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/image.png
  humanURL: https://www.veracity.com/
  baseURL: https://api.veracity.com
  properties:
  - url: https://developer.veracity.com/docs/section/api-explorer/api-explorer
    type: Documentation
  - url: https://developer.veracity.com/docs/section/datastandards/operationalvesseldata
    type: Reference
  - url: https://www.veracity.com/
    type: Portal
  description: DNV Veracity is an open and secure industry data platform facilitating exchange of datasets, APIs, applications, and insights across maritime, oil and gas, and energy sectors. Veracity APIs enable access to operational vessel data, maritime analytics, and fleet management services for over 18,000 companies and 200,000 users.
- aid: dnv:dnv-vessel-register-api
  name: DNV Vessel Register
  tags:
  - Classification
  - Fleet Management
  - Maritime
  - Vessel Registry
  image: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/image.png
  humanURL: https://vesselregister.dnv.com/vesselregister
  baseURL: https://vesselregister.dnv.com
  properties:
  - url: https://vesselregister.dnv.com/vesselregister
    type: Documentation
  description: DNV Vessel Register provides access to DNV's public registry of classified vessels including vessel identification, classification status, certificates, and survey history. The register supports fleet management and regulatory compliance workflows.
name: Dnv
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The API is documented using Swagger, please see API Documentation tab above.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

