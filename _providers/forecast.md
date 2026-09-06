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
  - '{''url'': ''https://www.forecast.app/'', ''status'': 301, ''note'': ''declared website redirects to https://www.accelo.com/forecast — a different registrable domain (forecast.app -> accelo.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'REST-style JSON API exposing the full Forecast platform: projects, tasks, sub-tasks, phases, sprints, time registrations, allocations, persons, clients, rate cards, invoices, and webhook subscriptions'
  name: Forecast API
  slug: forecast-api
artifact_total: 6
asyncapis:
- description: ''
  name: Forecast Webhooks
  slug: forecast-webhooks
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/accelo/
- group: company
  title: ''
  type: Website
  url: https://www.forecast.app/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Forecast-it/API
- group: docs
  title: ''
  type: APIReference
  url: https://support.forecast.app/hc/en-us/articles/5153680387473-API-Documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Forecast-it/API/blob/master/README.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Forecast-it
- group: operate
  title: ''
  type: Support
  url: https://support.forecast.app/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.forecast.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.forecast.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.forecast.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.forecast.app/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forecast-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/forecast-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/forecast-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/forecast-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/forecast-trust-center.yml
created: '2026-07-17'
description: Forecast is an AI-powered project and resource management platform (a professional services automation / PSA tool) for project-driven companies, covering predictive project planning, resource allocation, capacity planning, time tracking, budgets, rate cards, and financial forecasting. Forecast exposes a complete REST API (JSON over HTTPS at api.forecast.it) for projects, tasks, time registrations, allocations, people, clients, and webhooks, authenticated with a per-integration API key. Originally a Danish/UK startup backed by Balderton Capital, Forecast was acquired by Accelo in 2025 and the forecast.app brand has since been integrated into accelo.com, while the api.forecast.it API endpoints remain operational. Added to the API Evangelist network from a VC-portfolio lead and enriched from the public Forecast API documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forecast.png
layout: provider
modified: '2026-07-19'
name: forecast
nav: Providers
network: true
overview: 'forecast publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Project Management, Resource Management, Professional Services Automation, and Time Tracking.


  The forecast catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  forecast''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 10 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 36.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forecast/refs/heads/main/screenshots/forecast-2026-07-25T214928.png
security:
- kind: authentication
  name: Forecast Authentication
  slug: forecast-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Forecast Domain Security
  slug: forecast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Forecast Vulnerability Disclosure
  slug: forecast-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Forecast Trust Center
  slug: forecast-trust-center
  summary_line: SOC 2, ISO 27017, ISO 27018, PCI DSS, FIPS 140
slug: forecast
tags:
- Company
- Project Management
- Resource Management
- Professional Services Automation
- Time Tracking
- PSA
website: https://www.forecast.app/
---
