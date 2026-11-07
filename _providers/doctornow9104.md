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
- group: auth
  href: https://artifacts.apis.io/doctornow9104/well-known/doctornow9104-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doctornow9104-security.txt
- group: agent
  href: https://artifacts.apis.io/doctornow9104/well-known/doctornow9104-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doctornow9104-well-known.yml
- group: other
  href: https://artifacts.apis.io/doctornow9104/hosts/doctornow9104-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doctornow9104-hosts.yml
- group: auth
  href: https://artifacts.apis.io/doctornow9104/security/doctornow9104-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doctornow9104-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docnow.ai
coverage:
  checked: '2026-10-23'
  detail: The company website provides no developer documentation or API endpoints.
  evidence:
  - status: 200
    url: https://docnow.ai
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: 'Doctornow9104 is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-23'
name: Doctornow9104
nav: Providers
network: true
overview: Doctornow9104 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 21
score:
  band: minimal
  composite: 2.7
  coverage:
    artifact_dirs: 6
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
    operational_transparency: 10.5
  previous_composite: 2.7
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
screenshot: https://apis.io/screenshots/doctornow9104/doctornow9104-2026-11-03T130854.png
security:
- kind: domain-security
  name: Doctornow9104 Domain Security
  slug: doctornow9104-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: doctornow9104
tags:
- Company
website: https://docnow.ai
---
