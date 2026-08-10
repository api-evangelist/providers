---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: Read-only API to retrieve compliance reports and their associated files for your fleet, exposed through the Fleetworthy Compliance API portal (Azure API Management).
  name: Fleetworthy Read Reports API
  slug: fleetworthy-read-reports-api
- description: Create, read, update, and delete asset (vehicle/equipment) information to sync fleet asset data with external systems, exposed through the Fleetworthy Compliance API portal.
  name: Fleetworthy Asset Management API
  slug: fleetworthy-asset-management-api
- description: Create, read, update, and delete driver records and driver compliance data, exposed through the Fleetworthy Compliance API portal.
  name: Fleetworthy Driver Management API
  slug: fleetworthy-driver-management-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/fleetworthy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fleetworthy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fleetworthy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fleetworthy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fleetworthy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fleetworthy.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fleetworthy.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/fleetworthy-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://fleetworthy.com/get-started/
- group: start
  title: ''
  type: Login
  url: https://fleetworthy.com/login/
- group: commercial
  title: ''
  type: Pricing
  url: https://fleetworthy.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://bestpass01.my.site.com/help/s/?language=en_US
- group: company
  title: ''
  type: Blog
  url: https://fleetworthy.com/resources/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fleetworthy.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fleetworthy.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fleetworthy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fleetworthy.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fleetworthy.com/
created: '2026-07-17'
description: Fleetworthy is a North American fleet compliance, safety, and technology company (Madison, WI) that combines the Bestpass, Drivewyze, and related brands into a single integrated platform for commercial trucking fleets. Its products span safety and compliance management (driver and asset compliance with real-time alerts, Driver Qualification File management, DOT audit readiness, IFTA and Form 2290 tax filing), unified toll management with nationwide coverage and dispute resolution, and weigh-station bypass across 925+ inspection sites. Fleetworthy exposes a RESTful Compliance API through an Azure API Management developer portal (developer.fleetworthy.com) with three published APIs — Read Reports, Asset Management, and Driver Management — letting integrators retrieve report data and files and create, read, update, and delete asset and driver records to automate compliance workflows and sync with external systems.
image: https://fleetworthy.com/wp-content/uploads/2024/01/fleetworthy-logo.png
layout: provider
modified: '2026-07-19'
name: Fleetworthy
nav: Providers
network: true
overview: 'Fleetworthy publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fleet Management, Compliance, Transportation, and Trucking.


  Fleetworthy''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, pricing, support, and 11 more developer resources.'
random_paper: 53
score:
  band: thin
  composite: 32.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fleetworthy/refs/heads/main/screenshots/fleetworthy-2026-07-25T214740.png
security:
- kind: authentication
  name: Fleetworthy Authentication
  slug: fleetworthy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fleetworthy Domain Security
  slug: fleetworthy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fleetworthy Trust Center
  slug: fleetworthy-trust-center
  summary_line: SOC 2, ISO/IEC 27001:2022, PCI DSS v4.0.1
slug: fleetworthy
tags:
- Company
- Fleet Management
- Compliance
- Transportation
- Trucking
- Safety
- Toll Management
- Weigh Station Bypass
- Logistics
website: https://fleetworthy.com/
---
