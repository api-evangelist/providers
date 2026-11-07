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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DataKnows provides AI-driven data services with 350 billion data points to help home buyers, real‑estate developers, advertisers and local businesses make better decisions.
  name: Dataknows API
  slug: dataknows-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/dataknows/hosts/dataknows-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataknows-hosts.yml
- group: auth
  href: https://artifacts.apis.io/dataknows/security/dataknows-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataknows-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dataknows.ai
coverage:
  checked: '2026-10-22'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract discovered despite probing API host.
  evidence:
  - status: 0
    url: https://api.dataknows.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: DataKnows provides AI-driven data services with 350 billion data points to help home buyers, real‑estate developers, advertisers and local businesses make better decisions. Their platform offers products like GrowthMate, AEO Pro and Richgo, delivering price forecasts, site feasibility analysis and advertising performance insights.
layout: provider
modified: '2026-10-22'
name: Dataknows
nav: Providers
network: true
overview: Dataknows is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Real Estate, Data Analytics, Advertising, and B2B.
random_paper: 12
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 3.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dataknows/dataknows-2026-11-03T130216.png
security:
- kind: domain-security
  name: Dataknows Domain Security
  slug: dataknows-domain-security
  summary_line: TLSv1.2 · DMARC
slug: dataknows
tags:
- Artificial Intelligence
- Real Estate
- Data Analytics
- Advertising
- B2B
website: https://www.dataknows.ai
---
