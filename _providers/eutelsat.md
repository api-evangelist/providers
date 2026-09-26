---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eutelsat/refs/heads/main/llms/eutelsat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eutelsat-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eutelsat/refs/heads/main/well-known/eutelsat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eutelsat-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eutelsat/refs/heads/main/hosts/eutelsat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eutelsat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eutelsat/refs/heads/main/vendors/eutelsat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eutelsat-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.eutelsat.com:443/satellite-services/government/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eutelsat.com:443/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.eutelsat.com/media-press/media-centre/news/full-year-2024-25-results
- group: company
  title: ''
  type: Blog
  url: https://www.eutelsat.com/mediacentre/blog/redefining-inflight-connectivity
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eutelsat/refs/heads/main/security/eutelsat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eutelsat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eutelsat.com/
coverage:
  checked: 2026-09-22
  detail: API documentation appears to be rendered via JavaScript with no accessible OpenAPI spec.
  evidence:
  - status: 0
    url: https://api.eutelsat.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: Eutelsat is a high‑performance multi‑orbit satellite communications operator offering GEO and OneWeb LEO satellite services. It provides resilient, secure connectivity for land, sea and air customers, operating 31 GEO satellites and a constellation of over 600 LEO satellites to deliver broadband and data services worldwide.
image: https://www.eutelsat.com/sites/default/files/2026-08/Composite-Images-20260803-124639.png
layout: provider
modified: '2026-09-22'
name: Eutelsat
nav: Providers
network: true
overview: 'Eutelsat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellite, Communications, Geo, and LEO.


  Eutelsat''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 9.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eutelsat Domain Security
  slug: eutelsat-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eutelsat
tags:
- Company
- Satellite
- Communications
- Geo
- LEO
website: https://www.eutelsat.com/
---
