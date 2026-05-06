---
aid: litmus
name: Litmus
description: Email testing and analytics platform that allows developers and marketers to preview, test, and analyze email campaigns across multiple email clients and devices before sending.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer Tools
  - Email Testing
  - Marketing Tools
  - Quality Assurance
url: https://raw.githubusercontent.com/api-evangelist/litmus/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-03-18'
specificationVersion: '0.19'
apis:
  - aid: litmus:litmus-instant-api
    name: Litmus Instant API
    description: The Litmus Instant API provides REST endpoints for generating email preview screenshots across 40+ email clients by submitting HTML directly without needing to send an actual email. It is used by email editors and ESP integrations to deliver real-time rendering previews within their own platforms.
    humanURL: https://docs.litmus.com/instant
    baseURL: https://instant-api.litmus.com/v1
    tags:
      - Email Clients
      - Email Testing
      - Previews
      - REST API
    properties:
      - type: Documentation
        url: https://docs.litmus.com/instant
      - type: Authentication
        url: https://docs.litmus.com/oauth-integration-guide
      - type: OpenAPI
        url: openapi/litmus-instant-openapi.yml
  - aid: litmus:litmus-legacy-previews-api
    name: Litmus Legacy Previews API
    description: The Litmus Legacy Previews API provides REST endpoints for running email preview tests, spam filter tests, link-check tests, and code analysis against submitted email HTML. Tests are initiated by POSTing to the API and results are polled until rendering is complete.
    humanURL: https://docs.litmus.com/legacy-previews
    baseURL: https://previews-api.litmus.com/api/v1
    tags:
      - Email Testing
      - Previews
      - REST API
      - Spam Testing
    properties:
      - type: Documentation
        url: https://docs.litmus.com/legacy-previews
      - type: OpenAPI
        url: openapi/litmus-legacy-previews-openapi.yml
  - aid: litmus:litmus-email-analytics-api
    name: Litmus Email Analytics API
    description: The Litmus Email Analytics API provides REST endpoints for retrieving email campaign engagement metrics including read rates, deletion rates, device types, email clients, geographic data, and forwarding activity. Campaign data is accessed by GUID and returns detailed activity summary reports.
    humanURL: https://docs.litmus.com/email-analytics
    baseURL: https://analytics-api.litmus.com/api/v1
    tags:
      - Campaign Metrics
      - Email Analytics
      - Reporting
      - REST API
    properties:
      - type: Documentation
        url: https://docs.litmus.com/email-analytics
      - type: OpenAPI
        url: openapi/litmus-email-analytics-openapi.yml
common:
  - url: https://www.litmus.com/
    type: Website
  - url: https://docs.litmus.com/
    type: Documentation
  - url: https://www.litmus.com/getting-started/test-your-email
    type: Getting Started
  - url: https://www.litmus.com/blog/
    type: Blog
  - url: https://litmus.com/community
    type: Community
  - url: https://docs.litmus.com/oauth-integration-guide
    type: Authentication
  - url: https://docs.litmus.com/oauth/web-application-flow
    type: Authentication
  - type: JSONSchema
    url: json-schema/litmus-email-test-schema.json
    name: Litmus Email Test JSON Schema
    description: JSON Schema for Litmus email test objects covering preview, spam filter, and link-check test requests and results.
  - type: JSON-LD
    url: json-ld/litmus-context.jsonld
    name: Litmus JSON-LD Context
    description: Linked data context mapping Litmus email test and campaign entities to standard vocabularies.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
