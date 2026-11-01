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
    mcp_server: documented
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/demetrix/hosts/demetrix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/demetrix-hosts.yml
- group: other
  href: https://artifacts.apis.io/demetrix/vendors/demetrix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/demetrix-vendors.yml
- group: auth
  href: https://artifacts.apis.io/demetrix/security/demetrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/demetrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.demetrix.com/
coverage:
  checked: '2026-10-23'
  detail: The Demetrix website is a Squarespace site rendering content via JavaScript, preventing machine‑readable API discovery.
  evidence:
  - status: 200
    url: https://www.demetrix.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: 'Demetrix is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
image: http://static1.squarespace.com/static/6828bcce7458550ff2d511a4/t/6828be647ad16a394f2372e1/1759253474240/Logo+White.png?format=1500w
layout: provider
modified: '2026-10-22'
name: Demetrix
nav: Providers
network: true
overview: Demetrix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 2
score:
  band: minimal
  composite: 1.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 30.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Demetrix Domain Security
  slug: demetrix-domain-security
  summary_line: TLSv1.3 · HSTS
slug: demetrix
tags:
- Company
website: https://www.demetrix.com/
---
