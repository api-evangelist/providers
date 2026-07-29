---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Mosaic App Agentic Access
  operation_count: 23
  slug: mosaic-app-agentic-access
  summary_line: 23 operations · 17 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The Mosaic Open API exposes the workforce, project, and financial data Mosaic manages so firms can build custom integrations beyond the packaged ERP and PM connectors. It authenticates via API token a
  name: Mosaic Open API
  slug: open-api
- description: Team membership / people management
  name: Mosaic Members API
  slug: mosaic-app-members-api
- description: The Projects API from Mosaic — 3 operation(s) for projects.
  name: Mosaic Projects API
  slug: mosaic-app-projects-api
- description: The Tasks API from Mosaic — 2 operation(s) for tasks.
  name: Mosaic Tasks API
  slug: mosaic-app-tasks-api
- description: The Time Entries API from Mosaic — 2 operation(s) for time entries.
  name: Mosaic Time Entries API
  slug: mosaic-app-time-entries-api
- description: The Work Plans API from Mosaic — 3 operation(s) for work plans.
  name: Mosaic Work Plans API
  slug: mosaic-app-work-plans-api
artifact_total: 14
collections:
- collection_type: open
  name: Mosaic Open API
  slug: open-mosaic-app
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mosaic-app-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mosaic-app-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mosaic-app-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mosaic-app-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mosaicapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://readme.mosaicapp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://readme.mosaicapp.com/reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://readme.mosaicapp.com/docs/integration-steps
- group: operate
  title: ''
  type: ChangeLog
  url: https://readme.mosaicapp.com/changelog
- group: agent
  title: ''
  type: LlmsText
  url: https://readme.mosaicapp.com/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://mosaicapp.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/mosaic-app-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mosaic-app-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mosaic-app-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://mosaicapp.com/blog
created: '2026-05-23'
description: Mosaic is a resource management, workforce planning, and AI-assisted project management platform built for architecture, engineering, and professional services firms. It plugs into the ERPs those firms already run — Deltek (Ajera, Vantagepoint, Vision, Costpoint), Unanet, BST10, BQE Core, QuickBooks, Salesforce, and Microsoft Dynamics 365 — plus project management systems (Asana, Jira, GitHub, Karbon) and HRIS (BambooHR), then unifies the data into a single forecasting, time-entry, and capacity-planning surface. Mosaic exposes an Open API for custom integrations alongside its packaged connectors.
finops:
- name: Mosaic App Finops
  service_category: API
  slug: mosaic-app-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mosaic-app.png
layout: provider
modified: '2026-05-23'
name: Mosaic
nav: Providers
network: true
overview: 'Mosaic publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Members API, Projects API, Tasks API, and 2 more. Tagged areas include Resource Management, Workforce Planning, Project Management, AEC, and Professional Services.


  Mosaic''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Mosaic App Plans Pricing
  plan_count: 1
  slug: mosaic-app-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 2
  name: Mosaic App Rate Limits
  slug: mosaic-app-rate-limits
score:
  band: thin
  composite: 41.9
  delta: -1.8
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.4
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mosaic-app/refs/heads/main/screenshots/mosaic-app-2026-06-20T185820.png
security:
- kind: authentication
  name: Mosaic App Authentication
  slug: mosaic-app-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mosaic App Domain Security
  slug: mosaic-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mosaic App Trust Center
  slug: mosaic-app-trust-center
  summary_line: SOC 2
slug: mosaic-app
tags:
- Resource Management
- Workforce Planning
- Project Management
- AEC
- Professional Services
- Time Tracking
- Forecasting
- AI Assistant
- Integration Platform
- Fortune 500
website: https://mosaicapp.com/
---
