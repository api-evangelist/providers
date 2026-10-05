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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-planet/refs/heads/main/hosts/blue-planet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blue-planet-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-planet/refs/heads/main/vendors/blue-planet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blue-planet-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.blueplanet.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blue-planet/refs/heads/main/security/blue-planet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blue-planet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blueplanet.com/
coverage:
  checked: '2026-09-29'
  detail: Developer portal requires sign‑in and returns only HTML pages, no machine‑readable spec.
  evidence:
  - status: 200
    url: https://developer.blueplanet.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: Blue Planet is a stub entry in the API Evangelist catalog, representing a company for which detailed API information has not yet been discovered. The entry serves as a placeholder pending further investigation to identify the company's official website, API offerings, and related documentation. This placeholder will be enriched as more data becomes available through subsequent profiling steps.
layout: provider
modified: '2026-09-29'
name: Blue Planet
nav: Providers
network: true
overview: 'Blue Planet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Data, and Cloud.


  Blue Planet''s developer surface includes documentation and 4 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blue Planet Domain Security
  slug: blue-planet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blue-planet
tags:
- Company
- Technology
- Data
- Cloud
website: https://blueplanet.com/
---
