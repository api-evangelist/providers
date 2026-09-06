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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saudara-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://saudara.ai
- group: other
  title: ''
  type: Company
  url: https://www.ycombinator.com/companies/saudara
created: '2026-07-17'
description: Saudara AI is an AI-native sourcing brokerage, founded in 2024 and based in Spokane, Washington, that connects American brands with vetted Indonesian manufacturers. Buyers submit requests for quotes (RFQs) and the company pairs human brokers with AI agents that scan factories, verify certifications, benchmark pricing against market data, and prepare quotes, returning vetted supplier options within 48 hours. Saudara AI also handles quality control, logistics, improved payment terms (30/70 and net-60), and vendor financing. As of its launch the company reports having sourced over $1M for 40+ brands. It operates as a brokerage service and does not publish a public developer API, documentation, or SDKs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saudara-ai.png
layout: provider
modified: '2026-07-21'
name: Saudara Ai
nav: Providers
network: true
overview: Saudara Ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sourcing, Manufacturing, Supply Chain, and Procurement.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
    - southeast-asia
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/saudara-ai/refs/heads/main/screenshots/saudara-ai-2026-09-02T154435.png
security:
- kind: domain-security
  name: Saudara Ai Domain Security
  slug: saudara-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: saudara-ai
tags:
- Company
- Sourcing
- Manufacturing
- Supply Chain
- Procurement
- Artificial Intelligence
- Indonesia
website: https://saudara.ai
---
