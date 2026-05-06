---
aid: kombo
name: Kombo
description: Kombo is a unified API for HR and ATS integrations, enabling B2B SaaS companies to connect with HRIS, payroll, recruiting, and learning systems through a single integration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ATS
  - Embedded iPaaS
  - HRIS
  - LMS
  - Payroll
  - Unified API
url: https://raw.githubusercontent.com/api-evangelist/kombo/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kombo:unified-api
    name: Kombo Unified API
    description: Kombo provides a unified API that connects B2B SaaS products with HR, payroll, applicant tracking, and learning management systems through a single integration point, handling data normalization and authentication across 300+ HR and ATS tools.
    humanURL: https://www.kombo.dev
    baseURL: https://api.kombo.dev
    tags:
      - ATS
      - HRIS
      - Payroll
      - Unified API
    properties:
      - type: Documentation
        url: https://docs.kombo.dev
      - type: Getting Started
        url: https://docs.kombo.dev/getting-started
      - type: OpenAPI
        url: https://api.kombo.dev/openapi.json
      - type: SDKs
        url: https://kombo.dev/libraries-and-sdks
      - type: Integrations
        url: https://www.kombo.dev/categories/all
      - type: Security
        url: https://security.kombo.dev
  - aid: kombo:hris-api
    name: Kombo Unified HRIS API
    description: Unified HRIS API for accessing employee data, absence management, time-off tracking, document management, and provisioning workflows across HR systems.
    humanURL: https://docs.kombo.dev
    tags:
      - HRIS
      - Employees
      - Time Off
    properties:
      - type: Documentation
        url: https://docs.kombo.dev
      - type: OpenAPI
        url: https://api.kombo.dev/openapi.json
  - aid: kombo:ats-api
    name: Kombo Unified ATS API
    description: Unified ATS API for managing job postings, candidates, applications, and recruitment pipelines across applicant tracking systems.
    humanURL: https://docs.kombo.dev
    tags:
      - ATS
      - Recruiting
    properties:
      - type: Documentation
        url: https://docs.kombo.dev
      - type: OpenAPI
        url: https://api.kombo.dev/openapi.json
  - aid: kombo:ats-assessment-api
    name: Kombo Unified ATS-Assessment API
    description: Unified ATS-Assessment API for assessment writing, notifications, and result submission across ATS platforms.
    humanURL: https://docs.kombo.dev
    tags:
      - ATS
      - Assessments
    properties:
      - type: Documentation
        url: https://docs.kombo.dev
      - type: OpenAPI
        url: https://api.kombo.dev/openapi.json
  - aid: kombo:lms-api
    name: Kombo Unified LMS API
    description: Unified LMS API for user management, courses, and learning progress tracking across learning management systems.
    humanURL: https://docs.kombo.dev
    tags:
      - LMS
      - Learning
    properties:
      - type: Documentation
        url: https://docs.kombo.dev
      - type: OpenAPI
        url: https://api.kombo.dev/openapi.json
common:
  - type: Website
    url: https://www.kombo.dev
  - type: Documentation
    url: https://docs.kombo.dev
  - type: OpenAPI
    url: https://api.kombo.dev/openapi.json
  - type: SDKs
    url: https://kombo.dev/libraries-and-sdks
  - type: Security
    url: https://security.kombo.dev
  - type: Support
    url: mailto:support@kombo.dev
  - type: GitHub Organization
    url: https://github.com/kombo-api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
