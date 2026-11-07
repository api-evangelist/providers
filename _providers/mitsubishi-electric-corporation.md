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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/mitsubishi-electric-corporation/well-known/mitsubishi-electric-corporation-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mitsubishi-electric-corporation-www-security.txt
- group: agent
  href: https://artifacts.apis.io/mitsubishi-electric-corporation/well-known/mitsubishi-electric-corporation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mitsubishi-electric-corporation-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://www.mitsubishielectric.com/psirt/policy/index.html
- group: other
  href: https://artifacts.apis.io/mitsubishi-electric-corporation/hosts/mitsubishi-electric-corporation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mitsubishi-electric-corporation-hosts.yml
- group: auth
  href: https://artifacts.apis.io/mitsubishi-electric-corporation/security/mitsubishi-electric-corporation-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mitsubishi-electric-corporation-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mitsubishi-electric-corporation/security/mitsubishi-electric-corporation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mitsubishi-electric-corporation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://global.mitsubishielectric.com/
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI or other machine-readable contract found at known API hosts.
  evidence:
  - status: 0
    url: https://api.mitsubishielectric.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: 'Mitsubishi Electric Corporation is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-26'
name: Mitsubishi Electric Corporation
nav: Providers
network: true
overview: Mitsubishi Electric Corporation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 6
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 5.3
  previous_composite: 3.6
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/mitsubishi-electric-corporation/mitsubishi-electric-corporation-2026-11-03T135812.png
security:
- kind: domain-security
  name: Mitsubishi Electric Corporation Domain Security
  slug: mitsubishi-electric-corporation-domain-security
  summary_line: no transport/DNS hardening detected
- kind: vulnerability-disclosure
  name: Mitsubishi Electric Corporation Vulnerability Disclosure
  slug: mitsubishi-electric-corporation-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mitsubishi-electric-corporation
tags:
- Company
website: http://global.mitsubishielectric.com/
---
