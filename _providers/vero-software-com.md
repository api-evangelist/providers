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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/vero-software-com/hosts/vero-software-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vero-software-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/vero-software-com/security/vero-software-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vero-software-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.vero-software.com
coverage:
  checked: '2026-10-29'
  detail: No public API documentation or machine‑readable contract was found for Vero Software.
  evidence:
  - status: connection-failed
    url: http://api.vero-software.com
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: 'Vero Software is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by battery-ventures) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-29'
name: Vero Software
nav: Providers
network: true
overview: Vero Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 0
score:
  band: minimal
  composite: 1.3
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
    discoverability: 26.8
    operational_transparency: 0.0
  previous_composite: 1.3
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
security:
- kind: domain-security
  name: Vero Software Com Domain Security
  slug: vero-software-com-domain-security
  summary_line: no transport/DNS hardening detected
slug: vero-software-com
tags:
- Company
website: http://www.vero-software.com
---
