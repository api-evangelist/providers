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
  band: agent-aware
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/aisim-now/conformance/aisim-now-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aisim-now-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aisim-now/llms/aisim-now-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aisim-now-llms.txt
- group: agent
  href: https://artifacts.apis.io/aisim-now/well-known/aisim-now-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aisim-now-well-known.yml
- group: other
  href: https://artifacts.apis.io/aisim-now/hosts/aisim-now-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aisim-now-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aisim-now/security/aisim-now-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aisim-now-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aisim.now/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://aisim.now/openapi.json
  - status: 401
    url: https://api.aisim.now/mcp
  - status: 200
    url: https://aisim.now/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Travel eSIM provider offering AI‑assisted data plan selection for over 160 countries. Users can browse plans, get personalized recommendations via Claude, ChatGPT or Muse, and purchase instantly. The service includes customer support, flexible regional and global plans, and seamless eSIM installation before travel.
image: https://aisim.now/opengraph-image.jpg?713447312a214a24
layout: provider
modified: '2026-11-01'
name: aisim.now
nav: Providers
network: true
overview: aisim.now is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include eSIM, Travel Data, AI Assistant, Prepaid Plans, and Mobile Hotspot.
random_paper: 4
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 4.3
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aisim Now Domain Security
  slug: aisim-now-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aisim-now
tags:
- eSIM
- Travel Data
- AI Assistant
- Prepaid Plans
- Mobile Hotspot
website: https://aisim.now/
---
