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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cronch-io/hosts/cronch-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cronch-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/cronch-io/vendors/cronch-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cronch-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cronch-io/security/cronch-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cronch-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cronch.io/
coverage:
  checked: '2026-11-04'
  detail: The provider's website returns 404 and no developer documentation or API endpoints are publicly available.
  evidence:
  - status: 404
    url: https://cronch.io/
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: Cronch is a personal agent for developers that helps plan meals, water intake, and breaks around your calendar. It integrates with your schedule to send timely reminders, promoting health and productivity while you code. The service is currently in private beta, offering free access and paid tiers for teams. Cronch aims to simplify daily wellness routines for developers by automating routine health checks and providing a seamless, calendar‑aware experience.
layout: provider
modified: '2026-11-04'
name: Cronch
nav: Providers
network: true
overview: Cronch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Personal Agent, Developer Tools, Health, and Productivity.
random_paper: 10
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cronch Io Domain Security
  slug: cronch-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cronch-io
tags:
- Company
- Personal Agent
- Developer Tools
- Health
- Productivity
website: https://cronch.io/
---
