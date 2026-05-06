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
common:
  - url: https://www.dnv.com/
    type: Website
  - url: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/openapi/dnv-class-status-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/json-schema/dnv-vessel-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/json-ld/dnv-context.jsonld
    type: JSONLDContext
  - url: https://www.veracity.com/
    type: Portal
  - url: https://developer.veracity.com/docs/section/api-explorer/api-explorer
    type: Documentation
  - url: https://maritime.dnv.com/api/cs-iacs-customer
    type: Authentication
  - url: https://help-center.veracity.com/en/
    type: Support
  - url: https://support.veracity.com/
    type: Support
  - url: https://www.dnv.com/privacy/
    type: PrivacyPolicy
  - url: https://www.dnv.com/terms/
    type: TermsOfService
  - url: https://vesselregister.dnv.com/vesselregister
    type: Status
  - url: https://www.dnv.com/maritime/
    type: GettingStarted
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
modified: '2026-04-28'
name: DNV
tags:
  - Maritime
  - Energy
  - Classification
  - Vessel
  - Data Platform
description: DNV is a global classification, certification, and assurance provider for the maritime, energy, and industrial sectors. The API portfolio includes the Class Status API for vessel classification data, the Veracity industry data platform, and the public Vessel Register, supporting fleet management, regulatory compliance, and operational analytics workflows.
---
