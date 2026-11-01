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
  href: https://artifacts.apis.io/ceptor/vendors/ceptor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ceptor-vendors.yml
- group: other
  href: https://artifacts.apis.io/ceptor/hosts/ceptor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ceptor-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ceptor.io/
- group: auth
  href: https://artifacts.apis.io/ceptor/security/ceptor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ceptor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ceptor.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://ceptor.io/
  reason: no-developer-program
  state: none
created: '2026-10-19'
description: Asseco is a European IT solutions provider specializing in banking, insurance, and public sector software. Through its Ceptor platform, it offers API management, access management, and gateway services, enabling secure digital transformation for enterprises. The company focuses on integration, security, and scalable cloud/on‑premise deployments, serving clients across Europe and beyond.
layout: provider
modified: '2026-10-19'
name: Asseco
nav: Providers
network: true
overview: 'Asseco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Insurance, Public Sector, and API Management.


  Asseco''s developer surface includes documentation and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ceptor Domain Security
  slug: ceptor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ceptor
tags:
- Company
- Banking
- Insurance
- Public Sector
- API Management
- Europe
website: https://ceptor.io/
---
