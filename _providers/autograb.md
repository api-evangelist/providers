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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autograb/refs/heads/main/well-known/autograb-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autograb-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autograb/refs/heads/main/well-known/autograb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autograb-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autograb/refs/heads/main/hosts/autograb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autograb-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.autograb.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autograb
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autograb/refs/heads/main/security/autograb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autograb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autograb.com.au
created: '2026-09-26'
description: AutoGrab provides automotive intelligence platforms across multiple regions, offering real-time vehicle data, market insights, and tools for sourcing, pricing, valuation, and inventory analysis. Their solutions serve dealerships, finance and insurance companies, enhancing decision‑making and operational efficiency through AI‑driven analytics and scalable infrastructure.
layout: provider
modified: '2026-09-26'
name: Autograb
nav: Providers
network: true
overview: Autograb is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Data, Artificial Intelligence, and Marketplace.
random_paper: 17
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
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
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autograb Domain Security
  slug: autograb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: autograb
tags:
- Company
- Automotive
- Data
- Artificial Intelligence
- Marketplace
- Platform
website: https://autograb.com.au
---
