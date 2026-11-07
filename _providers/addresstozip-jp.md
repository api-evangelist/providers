---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/addresstozip-jp/hosts/addresstozip-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/addresstozip-jp-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://addresstozip.jp/
coverage:
  checked: '2026-10-31'
  detail: No public API documentation or machine-readable contracts were found; attempts to fetch common spec URLs on api.addresstozip.jp returned no data.
  evidence:
  - status: 0
    url: https://api.addresstozip.jp/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: addresstozip-jp is a Japanese service that provides address-to-zipcode conversion APIs. The company was initially added to the API Evangelist network as a stub based on harvest data, and its details are being enriched through the profiling pipeline. Further information about its offerings, documentation, and operational details will be gathered as the enrichment process continues.
layout: provider
modified: '2026-10-31'
name: addresstozip-jp
nav: Providers
network: true
overview: addresstozip-jp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 11
scopes:
- name: Addresstozip Jp Scopes
  scope_count: 0
  slug: addresstozip-jp-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  previous_composite: 2.8
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Addresstozip Jp Authentication
  slug: addresstozip-jp-authentication
  summary_line: 0 schemes
slug: addresstozip-jp
tags:
- Company
website: https://addresstozip.jp/
---
