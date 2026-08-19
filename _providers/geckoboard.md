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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Geckoboard Agentic Access
  operation_count: 5
  slug: geckoboard-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 3
apis:
- description: 'REST API for pushing custom data into Geckoboard for use on dashboards. Supports creating datasets with typed schemas (number, money, percentage, date, datetime, duration, string), appending records, '
  name: Geckoboard Datasets API
  slug: datasets-api
- description: Manage dataset schemas and records
  name: Geckoboard Datasets API
  slug: geckoboard-datasets-api
- description: API key verification
  name: Geckoboard Health API
  slug: geckoboard-health-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Geckoboard Datasets API
  slug: open-geckoboard-datasets-api
- collection_type: open
  name: Geckoboard Datasets Health API
  slug: open-geckoboard-health-api
- collection_type: open
  name: Geckoboard Datasets API
  slug: open-geckoboard
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/geckoboard-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/geckoboard-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/geckoboard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geckoboard-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/geckoboard-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geckoboard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geckoboard
- group: company
  title: ''
  type: Website
  url: https://www.geckoboard.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.geckoboard.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.geckoboard.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.geckoboard.com/signup
- group: operate
  title: ''
  type: Support
  url: https://support.geckoboard.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.geckoboard.com
- group: company
  title: ''
  type: Blog
  url: https://www.geckoboard.com/blog/rss/
created: '2026-05-11'
description: Geckoboard is a cloud dashboard service that lets teams build TV-ready, real-time business dashboards from spreadsheets, databases, and 90+ pre-built integrations (Salesforce, HubSpot, Stripe, Zendesk, Google Analytics, etc.). The Geckoboard Datasets API lets developers push their own data into Geckoboard by defining a schema and appending or replacing records, which can then power any dashboard visualization. The API is HTTPS-only and authenticates with HTTP Basic auth using a Geckoboard API key as the username.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geckoboard.png
layout: provider
modified: '2026-05-11'
name: Geckoboard
nav: Providers
network: true
overview: 'Geckoboard publishes 2 APIs on the [APIs.io](https://apis.io/) network: Datasets API and Health API. Tagged areas include Dashboards, Data Visualization, Business Intelligence, KPI Tracking, and Real-Time Reporting.


  Geckoboard''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 147
score:
  band: thin
  composite: 36.0
  delta: -0.8
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 56.6
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geckoboard/refs/heads/main/screenshots/geckoboard-2026-06-20T181707.png
security:
- kind: authentication
  name: Geckoboard Authentication
  slug: geckoboard-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Geckoboard Domain Security
  slug: geckoboard-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Geckoboard Vulnerability Disclosure
  slug: geckoboard-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Geckoboard Trust Center
  slug: geckoboard-trust-center
  summary_line: PCI DSS, GDPR
slug: geckoboard
tags:
- Dashboards
- Data Visualization
- Business Intelligence
- KPI Tracking
- Real-Time Reporting
- TV Dashboards
website: https://www.geckoboard.com
---
