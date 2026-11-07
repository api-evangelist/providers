---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for Myst (no machine-readable spec found)
  name: Myst API
  slug: myst-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/myst/llms/myst-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/myst-llms.txt
- group: other
  href: https://artifacts.apis.io/myst/hosts/myst-hosts.yml
  title: ''
  type: Hosts
  url: hosts/myst-hosts.yml
- group: build
  href: https://artifacts.apis.io/myst/packages/myst-packages.yml
  title: ''
  type: SDKs
  url: packages/myst-packages.yml
- group: build
  href: https://artifacts.apis.io/myst/packages/myst-packages.yml
  title: ''
  type: Packages
  url: packages/myst-packages.yml
- group: auth
  href: https://artifacts.apis.io/myst/security/myst-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/myst-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.myst.ai/
created: '2026-10-29'
description: 'Myst is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by gradient-ventures) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-29'
name: Myst
nav: Providers
network: true
overview: Myst is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Myst Plans Pricing
  plan_count: 0
  slug: myst-plans-pricing
random_paper: 5
scopes:
- name: Myst Scopes
  scope_count: 0
  slug: myst-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 19
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
    developer_ergonomics: 7.1
    discoverability: 42.9
    operational_transparency: 0.0
  previous_composite: 5.8
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Myst Authentication
  slug: myst-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Myst Domain Security
  slug: myst-domain-security
  summary_line: TLSv1.3
slug: myst
tags:
- Company
website: https://www.myst.ai/
---
