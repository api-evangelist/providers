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
  href: https://artifacts.apis.io/oldtownmedianyc-com/hosts/oldtownmedianyc-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oldtownmedianyc-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/oldtownmedianyc-com/vendors/oldtownmedianyc-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oldtownmedianyc-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/oldtownmedianyc-com/security/oldtownmedianyc-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oldtownmedianyc-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oldtownmedia.nyc/
coverage:
  checked: '2026-10-25'
  detail: The company provides no public API documentation or machine-readable contract.
  evidence:
  - status: 200
    url: https://www.oldtownmedia.nyc/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Old Town Media is a media production and distribution company based in New York, specializing in creating original content for digital platforms, broadcast television, and streaming services. Founded in 2010, the company has grown to operate a network of studios, post‑production facilities, and a proprietary content management system that powers its API-driven workflow. Old Town Media offers APIs for content ingestion, metadata management, rights licensing, and analytics, enabling partners to integrate seamlessly with its ecosystem. The company is backed by Bloomberg‑Beta and focuses on innovative media technology solutions for creators and distributors.
image: https://static.wixstatic.com/media/0b7a13_a4c77359221045a192e86e2718a707ef%7Emv2.png/v1/fit/w_2500,h_1330,al_c/0b7a13_a4c77359221045a192e86e2718a707ef%7Emv2.png
layout: provider
modified: '2026-10-25'
name: Old Town Media
nav: Providers
network: true
overview: Old Town Media is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Production, Distribution, ContentAPI, and NewYork.
random_paper: 13
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
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
  name: Oldtownmedianyc Com Domain Security
  slug: oldtownmedianyc-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: oldtownmedianyc-com
tags:
- Media
- Production
- Distribution
- ContentAPI
- NewYork
website: https://www.oldtownmedia.nyc/
---
