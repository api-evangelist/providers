---
aid: finch
name: Finch
description: Finch is a unified employment API providing standardized read and write access to HRIS, payroll, and benefits systems. Through a single integration, developers can pull company directory data, individual PII, employment records, payments, pay statements, and benefits across hundreds of providers (ADP, Gusto, Paylocity, Workday, BambooHR, Rippling, Justworks, TriNet, and more). Finch Connect handles end-user authorization via OAuth.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
tags:
  - Employment
  - HRIS
  - Payroll
  - Benefits
  - HR
  - Unified API
  - Workforce
url: https://raw.githubusercontent.com/api-evangelist/finch/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: finch:finch-api
    name: Finch API
    description: Unified REST API for HRIS, payroll, and benefits providers. Supports Company, Directory, Individual, Employment, Payment, Pay Statement, and Benefits resources. Authentication uses OAuth 2.0 via Finch Connect to issue per-employer bearer access tokens.
    humanURL: https://www.tryfinch.com/
    baseURL: https://api.tryfinch.com
    tags:
      - Employment
      - HRIS
      - Payroll
      - Benefits
      - Unified API
    properties:
      - type: Documentation
        url: https://developer.tryfinch.com/
      - type: API Reference
        url: https://developer.tryfinch.com/api-reference/
      - type: SignUp
        url: https://dashboard.tryfinch.com/signup
      - type: Pricing
        url: https://www.tryfinch.com/pricing
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/finch/refs/heads/main/openapi/finch-openapi.yml
common:
  - type: Website
    url: https://www.tryfinch.com/
  - type: Documentation
    url: https://developer.tryfinch.com/
  - type: API Reference
    url: https://developer.tryfinch.com/api-reference/
  - type: SignUp
    url: https://dashboard.tryfinch.com/signup
  - type: Pricing
    url: https://www.tryfinch.com/pricing
  - type: Blog
    url: https://www.tryfinch.com/blog
  - type: Changelog
    url: https://developer.tryfinch.com/changelog
  - type: StatusPage
    url: https://status.tryfinch.com/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
