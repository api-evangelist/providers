---
aid: cyclr
name: Cyclr
x-type: company
description: Cyclr is an embedded iPaaS (integration platform as a service) used by SaaS vendors to deliver native integrations to their customers without each vendor building and maintaining one-off connectors. The platform provides a connector library covering hundreds of business applications (CRM, marketing, finance, support, ERP, e-commerce), drag-and-drop integration templates, embedded LAUNCH and Marketplace UIs, custom connector creation, fully managed authentication, and workflow orchestration. Cyclr exposes a public REST API at api.cyclr.com (with regional EU / AU / UK / US2 siblings) protected by OAuth 2.0 client credentials. Account-scoped calls require an X-Cyclr-Account header to identify the target Cyclr account.
url: https://raw.githubusercontent.com/api-evangelist/cyclr/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consumer
created: '2025-06-06'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Connectors
  - Custom Connectors
  - Data Synchronization
  - Embedded iPaaS
  - Embedded SaaS Integration
  - Embedded UI
  - Integration Platform
  - Integrations
  - Marketplace
  - OAuth 2.0
  - REST API
  - SaaS
  - Templates
  - Webhooks
  - White Label
  - Workflows
apis:
  - aid: cyclr:api
    name: Cyclr API
    description: Cyclr's REST API allows partners to manage their accounts, install and authenticate connectors, install templates as cycles, build and configure cycle steps, and embed LAUNCH and Marketplace UIs into their host SaaS product. Authentication uses OAuth 2.0 client credentials issued in the Cyclr Console; account-scoped operations include the X-Cyclr-Account HTTP header.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cyclr.com
    baseURL: https://api.cyclr.com/v1.0
    tags:
      - Accounts
      - Connectors
      - Cycles
      - Embedded UI
      - OAuth 2.0
      - REST
      - Steps
      - Templates
    properties:
      - type: Documentation
        url: https://cyclr.com
      - type: APIDocumentation
        url: https://docs.cyclr.com/api/
      - type: APIReference
        url: https://api.cyclr.com/docs/index
      - type: OpenAPI
        url: openapi/cyclr-cyclr-openapi.yml
      - type: AsyncAPI
        url: asyncapi/cyclr-cyclr-asyncapi.yml
      - type: JSONSchema
        url: json-schema/cyclr-account.json
      - type: JSONSchema
        url: json-schema/cyclr-connector.json
      - type: JSONSchema
        url: json-schema/cyclr-installed-connector.json
      - type: JSONSchema
        url: json-schema/cyclr-template.json
      - type: JSONSchema
        url: json-schema/cyclr-cycle.json
      - type: JSONSchema
        url: json-schema/cyclr-step.json
      - type: JSONLD
        url: json-ld/cyclr-context.jsonld
      - type: Capabilities
        url: capabilities/cyclr-api-capabilities.yml
      - type: Rules
        url: rules/cyclr-api-rules.yml
common:
  - type: Website
    url: https://cyclr.com/
  - type: Connectors
    url: https://cyclr.com/connectors
  - type: Pricing
    url: https://cyclr.com/product/pricing
  - type: CaseStudies
    url: https://cyclr.com/case-studies
  - type: Webinars
    url: https://cyclr.com/resources/webinars
  - type: Blog
    url: https://cyclr.com/blog
  - type: Branding
    url: https://cyclr.com/brand
  - type: Partners
    url: https://cyclr.com/become-a-partner
  - type: Security
    url: https://cyclr.com/security-and-compliance
  - type: GDPR
    url: https://cyclr.com/legal/gdpr-compliance
  - type: SLA
    url: https://cyclr.com/sla
  - type: ChangeLog
    url: https://community.cyclr.com/user-documentation/release-notes/introduction-to-release-notes
  - type: Login
    url: https://my.cyclr.com/account/login
  - type: GetStarted
    url: https://cyclr.com/get-started
  - type: Vocabulary
    url: vocabulary/cyclr-vocabulary.yml
  - type: Capabilities
    url: capabilities/cyclr-api-capabilities.yml
  - type: Rules
    url: rules/cyclr-api-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
