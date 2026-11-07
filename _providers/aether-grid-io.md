---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/aether-grid-io/hosts/aether-grid-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aether-grid-io-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aether-grid-io/security/aether-grid-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aether-grid-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aether-grid.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://aether-grid.io/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: AETHER provides predictive industrial diagnostics powered by IoT sensors and AI. It identifies failing components in equipment, estimates remaining time to failure, and offers actionable insights without the need for historical data or extensive training. The platform serves manufacturers and operators seeking to reduce downtime and improve maintenance efficiency through real-time vibration analysis and cloud-based monitoring.
layout: provider
modified: '2026-10-31'
name: AETHER
nav: Providers
network: true
overview: AETHER is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, IoT, Predictive Analytics, Industrial, and Diagnostics.
random_paper: 17
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 3.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aether Grid Io Domain Security
  slug: aether-grid-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aether-grid-io
tags:
- Energy
- IoT
- Predictive Analytics
- Industrial
- Diagnostics
website: https://aether-grid.io/
---
