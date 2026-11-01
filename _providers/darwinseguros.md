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
  href: https://artifacts.apis.io/darwinseguros/hosts/darwinseguros-hosts.yml
  title: ''
  type: Hosts
  url: hosts/darwinseguros-hosts.yml
- group: other
  href: https://artifacts.apis.io/darwinseguros/vendors/darwinseguros-vendors.yml
  title: ''
  type: Vendors
  url: vendors/darwinseguros-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/darwinseguros
- group: auth
  href: https://artifacts.apis.io/darwinseguros/security/darwinseguros-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/darwinseguros-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.darwinseguros.com
- group: company
  title: ''
  type: Blog
  url: https://www.darwinseguros.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.darwinseguros.com/termos-e-politicas
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/6942edc36939800251e4af0f/699ca7719b7ad6083d765bcb_Poli%CC%81tica%20de%20Privacidade_%2025%2003%2025%201.pdf
coverage:
  checked: '2026-10-22'
  detail: API endpoints return 403, indicating authentication required and no public spec available.
  evidence:
  - status: 403
    url: https://api.darwinseguros.com/v1/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-22'
description: Darwinseguros is a Brazilian insurance company offering personal and corporate insurance solutions, including auto, fleet, and business coverage. The company provides a portal for customers and brokers, detailed policy terms, and a blog with insurance advice.
layout: provider
modified: '2026-10-22'
name: Darwinseguros
nav: Providers
network: true
overview: 'Darwinseguros is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Brazil, Auto Insurance, and Business Insurance.


  Darwinseguros'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Darwinseguros Domain Security
  slug: darwinseguros-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: darwinseguros
tags:
- Company
- Insurance
- Brazil
- Auto Insurance
- Business Insurance
- BrokerPortal
website: https://www.darwinseguros.com
---
