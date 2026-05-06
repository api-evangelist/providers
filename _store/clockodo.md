---
aid: clockodo
name: Clockodo
url: https://raw.githubusercontent.com/api-evangelist/clockodo/refs/heads/main/apis.yml
created: '2025-02-17'
modified: '2026-04-27'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
x-type: company
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Absence Management
  - Billing
  - Project Management
  - Stop Clock
  - Time Tracking
  - Timesheets
description: 'Clockodo is a German-built, cloud-based time-tracking and project- management application used by service firms, agencies, and freelancers. In addition to its web and mobile apps, Clockodo exposes a REST API at my.clockodo.com that mirrors the objects in the UI: time entries, customers, projects, services, users, absences, holiday quotas, lump-sum services, and a real-time stop-clock. Authentication uses a per-user email plus per-user API key delivered as the X-ClockodoApiUser/X-ClockodoApiKey header pair (or HTTP Basic), and every call must include the X-Clockodo-External-Application header identifying the integrating application.'
apis:
  - aid: clockodo:clockodo-api
    name: Clockodo API
    tags:
      - Absence Management
      - Billing
      - Project Management
      - Stop Clock
      - Time Tracking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.clockodo.com/en/api/
    baseURL: https://my.clockodo.com/api
    properties:
      - url: https://www.clockodo.com/en/api/
        type: Documentation
      - url: https://www.clockodo.com/en/api/authentication/
        type: Authentication
      - url: openapi/clockodo-openapi.yml
        type: OpenAPI
    description: The Clockodo API is a REST interface at my.clockodo.com that lets developers automate time tracking and project management. v2 endpoints under /api/v2 cover entries, customers, projects, services, users, lump-sum services, and the stop-clock; legacy endpoints under /api cover absences and holiday quotas. Calls authenticate with X-ClockodoApiUser plus X-ClockodoApiKey (or HTTP Basic with the same credentials) and identify the calling app via X-Clockodo-External-Application; responses are JSON.
common:
  - type: Website
    url: https://www.clockodo.com/en/
  - type: Documentation
    url: https://www.clockodo.com/en/api/
  - type: Blog
    url: https://www.clockodo.com/en/blog/
  - type: Pricing
    url: https://www.clockodo.com/en/pricing/
  - type: TermsOfService
    url: https://www.clockodo.com/en/terms-and-conditions/
  - type: PrivacyPolicy
    url: https://www.clockodo.com/en/data-privacy/
  - type: OpenAPI
    url: openapi/clockodo-openapi.yml
  - type: JSONSchema
    url: json-schema/clockodo-entry-schema.json
  - type: JSONLDContext
    url: json-ld/clockodo-context.jsonld
  - type: Spectral
    url: rules/clockodo-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/clockodo-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
