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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference discovered at https://dodo.day/api
  name: DoDo API
  slug: dodo-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dodo-day/llms/dodo-day-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dodo-day-llms.txt
- group: agent
  href: https://artifacts.apis.io/dodo-day/well-known/dodo-day-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dodo-day-well-known.yml
- group: other
  href: https://artifacts.apis.io/dodo-day/hosts/dodo-day-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dodo-day-hosts.yml
- group: other
  href: https://artifacts.apis.io/dodo-day/vendors/dodo-day-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dodo-day-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dodo.day/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dodo.day/privacy
- group: auth
  href: https://artifacts.apis.io/dodo-day/security/dodo-day-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dodo-day-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dodo.day/
coverage:
  checked: '2026-11-05'
  detail: API reference page at https://dodo.day/api returns HTML rendered by JavaScript, with no machine‑readable OpenAPI/AsyncAPI/GraphQL spec discovered.
  evidence:
  - status: 200
    url: https://dodo.day/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: 'dodo-day is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://dodo.day/og-image.png
layout: provider
modified: '2026-11-05'
name: DoDo
nav: Providers
network: true
overview: DoDo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 17
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dodo Day Domain Security
  slug: dodo-day-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dodo-day
tags:
- Company
website: https://dodo.day/
---
