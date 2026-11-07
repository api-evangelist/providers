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
    mcp_server: false
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
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/ghosty-studio/llms/ghosty-studio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ghosty-studio-llms.txt
- group: agent
  href: https://artifacts.apis.io/ghosty-studio/well-known/ghosty-studio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ghosty-studio-well-known.yml
- group: other
  href: https://artifacts.apis.io/ghosty-studio/hosts/ghosty-studio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ghosty-studio-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ghosty-studio/security/ghosty-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ghosty-studio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ghosty.studio/
coverage:
  checked: '2026-10-30'
  detail: No public API documentation or machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.ghosty.studio/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-30'
description: 'ghosty-studio is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-30'
name: ghosty-studio
nav: Providers
network: true
overview: ghosty-studio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 11
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 9
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
  previous_composite: 2.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ghosty-studio/ghosty-studio-2026-11-03T132817.png
security:
- kind: domain-security
  name: Ghosty Studio Domain Security
  slug: ghosty-studio-domain-security
  summary_line: DMARC
slug: ghosty-studio
tags:
- Company
website: https://ghosty.studio/
---
