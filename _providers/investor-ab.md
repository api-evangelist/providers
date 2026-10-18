---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/investor-ab/refs/heads/main/hosts/investor-ab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/investor-ab-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/investor-ab/refs/heads/main/security/investor-ab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/investor-ab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://investorab.com/
coverage:
  checked: '2026-10-15'
  detail: The API host https://api.investorab.com/ returned no response, and no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 0
    url: https://api.investorab.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Investor AB is a Swedish investment firm that provides capital and strategic support to technology startups and growth-stage companies. The company focuses on fostering innovation across sectors such as fintech, healthtech, and clean energy, offering both financial resources and operational expertise. While currently a stub in the API Evangelist network, Investor AB aims to develop robust API services to enable partners and developers to integrate with its investment platforms, access portfolio data, and automate reporting processes.
layout: provider
modified: '2026-10-14'
name: Investor AB
nav: Providers
network: true
overview: Investor AB is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 8
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Investor Ab Domain Security
  slug: investor-ab-domain-security
  summary_line: DMARC
slug: investor-ab
tags:
- Company
website: https://investorab.com/
---
