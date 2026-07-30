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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Funnel Control Plane API provides configuration-management operations for a Funnel subscription — workspaces, data sources, custom dimensions and metrics, and data exports to BigQuery, Snowflake, '
  name: Funnel Control Plane API
  slug: funnel-control-plane-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://funnel.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.funnel.io/en/
- group: docs
  title: ''
  type: APIReference
  url: https://registry.terraform.io/providers/funnel-io/funnel/latest/docs
- group: company
  title: ''
  type: Blog
  url: https://funnel.io/blog
- group: operate
  title: ''
  type: Support
  url: https://help.funnel.io/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://funnel.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.funnel.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://funnel.io/general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://funnel.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/funnel-io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.funnel.io
- group: build
  title: ''
  type: Packages
  url: packages/funnel-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/funnel-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/funnel-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/funnel-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/funnel-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/funnel-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/funnel-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/funnel-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://funnel.io/funnel-information-security-overview
- group: auth
  title: ''
  type: TrustCenter
  url: security/funnel-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/funnel-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/funnel-llms.txt
created: '2026-07-17'
description: Funnel (funnel.io) is a marketing intelligence and marketing data hub that helps agencies and brands become more data-driven. It connects to hundreds of advertising, analytics, CRM, and social data platforms, then automatically collects, normalizes, and transforms that marketing data into a single, business-ready model. Funnel exports the harmonized data to cloud data warehouses (BigQuery, Snowflake), Google Cloud Storage, BI and visualization tools, and back to ad platforms, and layers on advanced marketing measurement (Marketing Mix Modeling and Multi-Touch Attribution) plus dashboards and reporting. Programmatic configuration is exposed through the Funnel Control Plane API, consumed via an official Terraform provider and an OAuth 2.0 client-credentials (Auth0) system-user flow, with regional US and EU data residency.
image: https://funnel.io/hubfs/Blog%20images.006.jpeg
layout: provider
modified: '2026-07-19'
name: Funnel
nav: Providers
network: true
overview: 'Funnel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Intelligence, Marketing Data, and Analytics.


  Funnel''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, authentication, and 16 more developer resources.'
random_paper: 74
score:
  band: thin
  composite: 33.8
  delta: -0.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 34.0
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/funnel/refs/heads/main/screenshots/funnel-2026-07-25T215322.png
security:
- kind: authentication
  name: Funnel Authentication
  slug: funnel-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Funnel Domain Security
  slug: funnel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Funnel Trust Center
  slug: funnel-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type II, CSA STAR Level 1
slug: funnel
tags:
- Company
- Marketing
- Marketing Intelligence
- Marketing Data
- Analytics
- Advertising
- Data Integration
- ETL
- Data Warehouse
- Attribution
- Reporting
- Business Intelligence
website: https://funnel.io/
---
