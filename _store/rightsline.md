---
aid: rightsline
name: Rightsline
description: Rightsline is the leading rights and royalties software platform for media, entertainment, and content businesses. Its REST API enables real-time integration of contacts, product catalogs, revenue data, and workflow automation for rights tracking, availability, royalty calculations, and vendor delivery across the content lifecycle.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Content Management
  - Entertainment
  - Media
  - Rights Management
  - Royalties
url: https://raw.githubusercontent.com/api-evangelist/rightsline/refs/heads/main/apis.yml
created: '2025-02-08'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rightsline:rights-api
    name: Rightsline Rights API
    description: RESTful API for managing rights, licenses, and availability data. Supports creation, retrieval, modification, and deletion of up to 100 records per request. Enables automation of rights tracking, availability validation, vendor delivery requests, and workflow actions.
    humanURL: https://api-docs.rightsline.com/
    baseURL: https://app.rightsline.com/v4
    tags:
      - Availability
      - Content
      - Rights Management
      - Workflows
    properties:
      - type: Documentation
        url: https://api-docs.rightsline.com/
      - type: PostmanWorkspace
        url: https://postman.rightsline.com/
      - type: Authentication
        url: https://api-docs.rightsline.com/authentication/user-permissions
  - aid: rightsline:royalties-api
    name: Rightsline Royalties API
    description: RESTful API for managing royalties, revenue data, and financial workflows. Supports bulk loading of revenue, sales, and usage data. Enables automation of finance billing requests and royalty calculations.
    humanURL: https://api-docs.rightsline.com/
    baseURL: https://app.rightsline.com/v4
    tags:
      - Billing
      - Finance
      - Revenue
      - Royalties
    properties:
      - type: Documentation
        url: https://api-docs.rightsline.com/
      - type: PostmanWorkspace
        url: https://postman.rightsline.com/
common:
  - type: Website
    url: https://www.rightsline.com
  - type: Documentation
    url: https://api-docs.rightsline.com/
  - type: Portal
    url: https://app.rightsline.com
  - type: PostmanWorkspace
    url: https://postman.rightsline.com/
  - type: Authentication
    url: https://api-docs.rightsline.com/authentication/user-permissions
  - type: GettingStarted
    url: https://api-docs.rightsline.com/getting-started
  - type: Blog
    url: https://www.rightsline.com/resources/api-integration/
  - type: TermsOfService
    url: https://www.rightsline.com/terms-of-service/
  - type: PrivacyPolicy
    url: https://www.rightsline.com/privacy-policy/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/rightsline/refs/heads/main/openapi/rightsline-openapi.yml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/rightsline/refs/heads/main/rules/rightsline-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/rightsline/refs/heads/main/capabilities/rights-royalties-management.yaml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rightsline/refs/heads/main/json-schema/rightsline-right-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rightsline/refs/heads/main/json-schema/rightsline-royalty-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/rightsline/refs/heads/main/json-ld/rightsline-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/rightsline/refs/heads/main/vocabulary/rightsline-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
