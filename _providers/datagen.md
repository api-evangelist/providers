---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/datagen/hosts/datagen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datagen-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://datagen.tech/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://datagen.tech/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: 'Datagen is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by scale-venture-partners) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-29'
name: Datagen
nav: Providers
network: true
overview: Datagen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Datagen Plans Pricing
  plan_count: 0
  slug: datagen-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Datagen Rate Limits
  slug: datagen-rate-limits
scopes:
- name: Datagen Scopes
  scope_count: 0
  slug: datagen-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 1.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datagen Authentication
  slug: datagen-authentication
  summary_line: 0 schemes
slug: datagen
tags:
- Company
website: https://datagen.tech/
---
