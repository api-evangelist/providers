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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The Crunchtime Inventory & Labor API is a REST/JSON web-services API for integrating restaurant back-office data with the Crunchtime platform. It exposes 150+ operations organized by functional area —
  name: Crunchtime Inventory & Labor API
  slug: crunchtime-inventory-labor-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.crunchtime.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.crunchtime.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.crunchtime.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.crunchtime.com/docs/getting-started-with-apis
- group: operate
  title: ''
  type: Support
  url: https://crunchtime.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.crunchtime.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.crunchtime.com/request-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crunchtime.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crunchtime.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.crunchtime.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crunchtime-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/crunchtime-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crunchtime-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crunchtime-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crunchtime-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crunchtime-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/crunchtime-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crunchtime-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crunchtime-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crunchtime-domain-security.yml
created: '2026-07-17'
description: Crunchtime (CrunchTime! Information Systems) is an AI-powered restaurant operations management platform used by 850+ multi-unit restaurant brands across 150,000+ locations to run inventory and food-cost control, labor and scheduling, operations execution (tasks, audits, temperature and food-prep labeling), kitchen display (KDS), guest/host-stand management, learning & development, and operational intelligence (Crunchtime Insights and Data Streaming). For integrators, Crunchtime publishes the Inventory & Labor developer hub — a REST/JSON API of 150+ operations (employees, locations, budgets, recipes, purchase orders, inventory counts, schedules, sales/menu-mix and more) served from the net-chef.com web services, authenticated with per-environment API tokens plus a site name and application user. The company merged with QSR Automations to cover the full restaurant food lifecycle and is a Battery Ventures portfolio company.
image: https://www.crunchtime.com/hubfs/2026-Crunchtime-Suite-ftr_@2x.jpg
layout: provider
modified: '2026-07-18'
name: Crunchtime
nav: Providers
network: true
overview: 'Crunchtime publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant Operations, Inventory Management, Labor & Scheduling, and Food Cost.


  Crunchtime''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 13 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 4
  name: Crunchtime Rate Limits
  slug: crunchtime-rate-limits
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 55.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 36.8
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/screenshots/crunchtime-2026-07-25T210820.png
security:
- kind: authentication
  name: Crunchtime Authentication
  slug: crunchtime-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Crunchtime Domain Security
  slug: crunchtime-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crunchtime
tags:
- Company
- Restaurant Operations
- Inventory Management
- Labor & Scheduling
- Food Cost
- Kitchen Display
- Point-of-Sale
- Supply Chain
- Hospitality
- REST API
website: https://developer.crunchtime.com/
---
