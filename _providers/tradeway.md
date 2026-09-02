---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradeway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tradesaretheway.com/
- group: start
  title: ''
  type: Login
  url: https://tradesaretheway.com/field-app/assistant
created: '2026-07-17'
description: Tradeway is an AI-powered field assistant for residential trade contractors working in electrical, plumbing, and HVAC. Technicians use it to plan jobs step by step with the right materials and code requirements, to identify parts from a photo with nearby supplier pricing and sourcing, and to get hands-free answers to technical questions on the job site. For business owners it centralizes crew history and field activity into a single view, reducing callbacks and rework through built-in code checks and standardized, repeatable processes so new hires can bill like veterans. Tradeway is backed by Bloomberg Beta. As of this enrichment pass the company publishes no public API, developer portal, SDKs, or API documentation; this profile captures its identity and domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tradeway.png
layout: provider
modified: '2026-07-21'
name: Tradeway
nav: Providers
network: true
overview: Tradeway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contractors, Trades, HVAC, and Plumbing.
random_paper: 4
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Tradeway Domain Security
  slug: tradeway-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tradeway
tags:
- Company
- Contractors
- Trades
- HVAC
- Plumbing
- Electrical
- Field Service
- AI Assistant
- Construction
website: https://tradesaretheway.com/
---
