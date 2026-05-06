---
aid: escape
name: Escape
url: https://raw.githubusercontent.com/api-evangelist/escape/refs/heads/main/apis.yml
description: Escape was founded in 2020 after one of our co-founders experienced a cyberattack and saw firsthand how vulnerable exposed APIs can be. Driven by a belief in the power of AI to transform cybersecurity, we built a platform that emulates hacker behavior to identify vulnerabilities before they can be exploited. Escape is a DAST (Dynamic Application Security Testing) platform that helps you document all your APIs, detect complex business logic flaws across modern applications like APIs, SPAs, and Microservices, and seamlessly integrate security into your CI/CD pipeline.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Contract
position: Consumer
access: 3rd-Party
tags:
  - Platform
  - Security
created: '2025-01-08'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: escape:escape-public-api
    name: Escape Public API
    description: The Escape Public API (V3) provides programmatic access to DAST scanning profiles, assets, integrations, scan results, authentications, issues, and job/report exports. Endpoints support automation of API security testing workflows and CI/CD pipeline integration.
    humanURL: https://docs.escape.tech/documentation/automate/public-api/
    baseURL: https://public.escape.tech/v3
    tags:
      - API Security
      - DAST
      - Security
      - Vulnerability Scanning
    properties:
      - type: Documentation
        url: https://docs.escape.tech/documentation/automate/public-api/
      - type: OpenAPI
        url: openapi/escape-openapi.yml
      - type: Authentication
        url: https://docs.escape.tech/documentation/automate/public-api/
common:
  - type: Documentation
    url: https://docs.escape.tech/
    name: Home - Escape Documentation
  - type: Blog
    url: https://escape.tech/blog/
    name: Escape - The API Security Blog
  - type: Integrations
    url: https://docs.escape.tech/documentation/inventory/integrations/
    name: Integrations - Escape Documentation
  - type: CaseStudies
    url: https://escape.tech/blog/tag/case-study/
    name: Case Study - Escape
  - type: PrivacyPolicy
    url: https://escape.tech/privacy
    name: Privacy Policy - Escape
  - type: TermsOfService
    url: https://escape.tech/terms
    name: Terms of Service
  - type: Website
    url: https://escape.tech/
    name: Escape - The only DAST that works with your modern stack
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
