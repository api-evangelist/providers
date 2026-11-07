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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/saab/hosts/saab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/saab-hosts.yml
- group: other
  href: https://artifacts.apis.io/saab/vendors/saab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/saab-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.saab.com/site-info/legal-notice
- group: operate
  title: ''
  type: Support
  url: https://www.saab.com/support
- group: auth
  title: ''
  type: Security
  url: https://www.saab.com/products/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.saab.com/site-info/data-privacy/privacy-notices
- group: company
  title: ''
  type: Newsroom
  url: https://www.saab.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.saab.com/markets/australia/about/leadership
- group: auth
  href: https://artifacts.apis.io/saab/security/saab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/saab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://saab.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://saab.com/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Saab AB is a Swedish aerospace and defence company that designs, manufactures, and delivers advanced technology systems and services for civil and military customers worldwide. Its portfolio includes aircraft, submarines, radar, missile systems, and digital solutions, focusing on safety, security, and sustainability. The company operates globally with a strong emphasis on innovation and collaboration across its various business areas.
image: https://www.saab.com/favicon.ico
layout: provider
modified: '2026-10-14'
name: Saab
nav: Providers
network: true
overview: 'Saab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Defence, Technology, and Sweden.


  Saab''s developer surface includes support and 9 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 11.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/saab/saab-2026-11-03T142615.png
security:
- kind: domain-security
  name: Saab Domain Security
  slug: saab-domain-security
  summary_line: TLSv1.3 · DMARC
slug: saab
tags:
- Company
- Aerospace
- Defence
- Technology
- Sweden
website: https://saab.com/
---
