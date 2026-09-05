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
  url: security/glp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.glp.com
created: '2026-07-17'
description: 'GLP is a leading global logistics real estate and investment management company, developing and operating warehouses, distribution centers, and supply-chain infrastructure alongside a large fund and asset-management business. It was surfaced as a portfolio company of hillhouse and added to the API Evangelist network for enrichment. Sector: logistics. As of this enrichment pass GLP publishes a WAF-protected corporate website but no discoverable public developer program, API documentation, or developer portal; this profile remains a lead awaiting a public API surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glp.png
layout: provider
modified: '2026-07-19'
name: GLP
nav: Providers
network: true
overview: GLP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Real-Estate, Supply Chain, and Warehousing.
random_paper: 8
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Glp Domain Security
  slug: glp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: glp
tags:
- Company
- Logistics
- Real-Estate
- Supply Chain
- Warehousing
- Investment Management
website: https://www.glp.com
---
