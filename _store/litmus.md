---
aid: litmus
url: https://raw.githubusercontent.com/api-evangelist/litmus/refs/heads/main/apis.yml
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
name: Litmus
tags:
- Developer Tools
- Email Testing
- Marketing Tools
- Quality Assurance
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Email testing and analytics platform that allows developers and marketers to preview, test, and analyze email campaigns across multiple email clients and devices before sending.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

