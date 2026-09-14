---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ukg Ready Agentic Access
  operation_count: 3
  slug: ukg-ready-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: RESTful API for UKG Ready providing programmatic access to employees, HR records, payroll, time and attendance, schedules, accruals, benefits, and workforce reporting. The base URL is per-tenant (http
  name: UKG Ready REST API
  slug: rest-api
- baseURL: https://{hostname}/api
  baseurl_source: declared
  description: Access token issuance
  name: UKG Ready Authentication API
  slug: ukg-ready-authentication-api
- baseURL: https://{hostname}/api
  baseurl_source: declared
  description: Tenant content and posts
  name: UKG Ready Content API
  slug: ukg-ready-content-api
- baseURL: https://{hostname}/api
  baseurl_source: declared
  description: Workgroup and organizational unit management
  name: UKG Ready Groups API
  slug: ukg-ready-groups-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UKG Ready Authentication API
  slug: open-ukg-ready-authentication-api
- collection_type: open
  name: UKG Ready Authentication Content API
  slug: open-ukg-ready-content-api
- collection_type: open
  name: UKG Ready Authentication Groups API
  slug: open-ukg-ready-groups-api
- collection_type: open
  name: UKG Ready API
  slug: open-ukg-ready
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ukg-ready-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ukg-ready-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ukg-ready-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ultimatesoftware
- group: company
  title: ''
  type: Website
  url: https://www.ukg.com/solutions/ukg-ready
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ukg.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ukg.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ukg.com/solutions/ukg-ready/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.ukg.com/contact
- group: operate
  title: ''
  type: Community
  url: https://community.ukg.com
- group: operate
  title: ''
  type: Support
  url: https://www.ukg.com/support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ukg
created: '2026-05-11'
description: UKG Ready (formerly Kronos Workforce Ready) is UKG's unified Human Capital Management (HCM) suite for small and midmarket organizations, combining HR, payroll, talent management, benefits administration, time and attendance, scheduling, and compliance into a single cloud platform. UKG Ready exposes REST and GraphQL APIs (per-tenant host of the form https://{hostname}/api/...) using OAuth 2.0 authorization code flow with bearer tokens for managing employees, schedules, timekeeping, payroll, benefits, and workforce data.
graphqls:
- description: ''
  name: UKG Ready GraphQL API
  slug: ukg-ready-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ukg-ready.png
layout: provider
modified: '2026-05-11'
name: UKG Ready
nav: Providers
network: true
overview: 'UKG Ready publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Content API, and Groups API. Tagged areas include HCM, Payroll, Workforce Management, Time and Attendance, and HR.


  UKG Ready''s developer surface includes authentication, documentation, pricing, signup flow, support, and 7 more developer resources.'
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/ukg-ready/refs/heads/main/screenshots/ukg-ready-2026-06-20T200009.png
security:
- kind: authentication
  name: Ukg Ready Authentication
  slug: ukg-ready-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ukg Ready Domain Security
  slug: ukg-ready-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ukg-ready
tags:
- HCM
- Payroll
- Workforce Management
- Time and Attendance
- HR
- Benefits
website: https://www.ukg.com/solutions/ukg-ready
---
