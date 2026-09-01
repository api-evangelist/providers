---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The NTSB provides transportation accident investigation data and safety recommendations for aviation, rail, highway, marine, and pipeline transportation.
  name: National Transportation Safety Board
  slug: national-transportation-safety-board
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-transportation-safety-board-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ntsb
- group: company
  title: ''
  type: Website
  url: https://www.ntsb.gov/
- group: company
  title: ''
  type: Blog
  url: https://www.ntsb.gov/news/press-releases/Pages/default.aspx
created: '2024-12-03'
description: The National Transportation Safety Board (NTSB) is an independent federal agency responsible for investigating transportation accidents, including those involving airplanes, trains, ships, and pipelines. The NTSB promotes safety and prevents future accidents by conducting thorough investigations and making recommendations to improve safety standards.
finops:
- name: National Transportation Safety Board Finops
  service_category: API
  slug: national-transportation-safety-board-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-transportation-safety-board.png
layout: provider
modified: '2026-04-28'
name: National Transportation Safety Board
nav: Providers
network: true
overview: 'National Transportation Safety Board publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Safety, and Transportation.


  National Transportation Safety Board''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: National Transportation Safety Board Plans Pricing
  plan_count: 3
  slug: national-transportation-safety-board-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: National Transportation Safety Board Rate Limits
  slug: national-transportation-safety-board-rate-limits
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-transportation-safety-board/refs/heads/main/screenshots/national-transportation-safety-board-2026-06-20T190047.png
security:
- kind: domain-security
  name: National Transportation Safety Board Domain Security
  slug: national-transportation-safety-board-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-transportation-safety-board
tags:
- Federal-Government
- Safety
- Transportation
website: https://www.ntsb.gov/
---
