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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fleetline-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fleetline.ai/
- group: start
  title: ''
  type: Login
  url: https://fleetline.ai/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fleetline.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fleetline.ai/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fleetlineai
created: '2026-07-17'
description: Fleetline is an all-in-one AI dispatch and fleet-optimization platform for trucking fleets. Its AI-based dispatch engine ingests load, driver, and ELD data, simulates billions of scenarios, and recommends the best assignment plan so operators maximize revenue, productivity, and fleet utilization. The platform aggregates major load boards into a unified workspace, identifies schedule gaps and fills them with spot loads, composes complex trips with tradeoff analysis, forecasts delays, breakdowns, and HOS violations, and includes an AI assistant trained on fleet history and TMS data. Fleetline is a Bloomberg Beta portfolio company; it exposes a marketing site, a customer login/auth portal, and an internal API host, but publishes no public developer API, documentation, or SDKs at this time.
image: https://db.fleetline.ai/storage/v1/object/public/fleetline-cdn/fleetline-logo_symbol-black.svg
layout: provider
modified: '2026-07-19'
name: Fleetline
nav: Providers
network: true
overview: Fleetline is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Fleet Management, Trucking, and Logistics.
random_paper: 7
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fleetline/refs/heads/main/screenshots/fleetline-2026-07-25T214738.png
security:
- kind: domain-security
  name: Fleetline Domain Security
  slug: fleetline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fleetline
tags:
- Company
- Artificial Intelligence
- Fleet Management
- Trucking
- Logistics
- Freight
- Dispatch
- Optimization
website: https://www.fleetline.ai/
---
