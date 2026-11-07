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
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/canopyb4c1/llms/canopyb4c1-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canopyb4c1-llms.txt
- group: agent
  href: https://artifacts.apis.io/canopyb4c1/well-known/canopyb4c1-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canopyb4c1-well-known.yml
- group: other
  href: https://artifacts.apis.io/canopyb4c1/hosts/canopyb4c1-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canopyb4c1-hosts.yml
- group: other
  href: https://artifacts.apis.io/canopyb4c1/vendors/canopyb4c1-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canopyb4c1-vendors.yml
- group: auth
  href: https://artifacts.apis.io/canopyb4c1/security/canopyb4c1-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canopyb4c1-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getcanopy.co
coverage:
  checked: '2026-10-06'
  detail: The company provides consumer humidifiers and air purifiers, not a software API.
  evidence:
  - status: 200
    url: https://getcanopy.co
  reason: not-a-software-company
  state: none
created: '2026-10-06'
description: 'Canopyb4c1 is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-06'
name: Canopyb4c1
nav: Providers
network: true
overview: Canopyb4c1 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 12
score:
  band: minimal
  composite: 2.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 33.9
    operational_transparency: 0.0
  previous_composite: 2.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/canopyb4c1/canopyb4c1-2026-11-03T123137.png
security:
- kind: domain-security
  name: Canopyb4C1 Domain Security
  slug: canopyb4c1-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: canopyb4c1
tags:
- Company
website: https://getcanopy.co
---
