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
api_count: 1
apis:
- description: Public beta API for AI Arena providing aerospace, automotive, and intelligence data.
  name: AI Arena API
  slug: ai-arena-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/ai-arena-ca/conformance/ai-arena-ca-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-arena-ca-conformance.yml
- group: other
  href: https://artifacts.apis.io/ai-arena-ca/hosts/ai-arena-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-arena-ca-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-arena-ca/vendors/ai-arena-ca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-arena-ca-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ai-arena-ca/security/ai-arena-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-arena-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-arena.ca/
created: '2026-11-01'
description: AI Arena is an independent music discovery platform that hosts AI‑created and artist‑submitted tracks. Users can battle songs head‑to‑head, vote, and climb rankings in real‑time playlists. The service emphasizes exposure for emerging creators, offering blind battles, genre‑based playlists, and live events, while storing only links to externally hosted music.
layout: provider
modified: '2026-11-01'
name: AI Arena
nav: Providers
network: true
overview: AI Arena is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Artificial Intelligence, Discovery, Community, and Independent.
random_paper: 23
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 6.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Arena Ca Domain Security
  slug: ai-arena-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ai-arena-ca
tags:
- Music
- Artificial Intelligence
- Discovery
- Community
- Independent
website: https://ai-arena.ca/
---
