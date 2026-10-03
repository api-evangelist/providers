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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aribio/refs/heads/main/hosts/aribio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aribio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aribio/refs/heads/main/vendors/aribio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aribio-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aribio/refs/heads/main/security/aribio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aribio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aribiogroup.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: AriBio, operating under the ARIBIO Group, integrates biotechnology, artificial intelligence, and energy/data center infrastructure technologies to drive Korea's future core industries. The company aims to become a next‑generation global platform group, merging bio‑tech and AI for innovative solutions across healthcare, energy, and digital infrastructure.
image: https://cdn.imweb.me/upload/S2026062357464fa378127/b10f0909e84f2.png
layout: provider
modified: '2026-09-26'
name: AriBio
nav: Providers
network: true
overview: AriBio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Artificial Intelligence, Energy, Data Center, and South Korea.
random_paper: 14
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aribio Domain Security
  slug: aribio-domain-security
  summary_line: TLSv1.3
slug: aribio
tags:
- Biotechnology
- Artificial Intelligence
- Energy
- Data Center
- South Korea
website: https://aribiogroup.com/
---
