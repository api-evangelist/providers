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
  href: https://artifacts.apis.io/thousand-api-com/hosts/thousand-api-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thousand-api-com-hosts.yml
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI or other machine-readable contract was found at standard locations on the provider's API host.
  evidence:
  - status: 404
    url: https://api.thousand-api.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 'thousand-api-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-31'
name: thousand-api-com
nav: Providers
network: true
overview: thousand-api-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Thousand Api Com Plans Pricing
  plan_count: 0
  slug: thousand-api-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Thousand Api Com Rate Limits
  slug: thousand-api-com-rate-limits
scopes:
- name: Thousand Api Com Scopes
  scope_count: 0
  slug: thousand-api-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 1.9
  coverage:
    artifact_dirs: 17
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
  name: Thousand Api Com Authentication
  slug: thousand-api-com-authentication
  summary_line: 0 schemes
slug: thousand-api-com
tags:
- Company
---
