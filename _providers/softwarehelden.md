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
api_count: 1
apis:
- description: API for Softwarehelden platform (details behind login)
  name: Softwarehelden API
  slug: softwarehelden-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/softwarehelden/hosts/softwarehelden-hosts.yml
  title: ''
  type: Hosts
  url: hosts/softwarehelden-hosts.yml
- group: other
  href: https://artifacts.apis.io/softwarehelden/vendors/softwarehelden-vendors.yml
  title: ''
  type: Vendors
  url: vendors/softwarehelden-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.softwarehelden.com/
- group: auth
  href: https://artifacts.apis.io/softwarehelden/security/softwarehelden-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/softwarehelden-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://softwarehelden.com/
- group: company
  title: ''
  type: Blog
  url: https://www.softwarehelden.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.softwarehelden.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.softwarehelden.com/impressum
coverage:
  checked: '2026-10-19'
  detail: Developer portal requires login and renders via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://portal.softwarehelden.com/Login?ReturnUrl=%2F
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Softwarehelden is a German digital transformation and AI software company offering the Cluu platform, which connects complex IT landscapes into a unified digital environment. It enables businesses to modernize processes, integrate AI, and improve efficiency without replacing existing systems. Services include products, solutions, consulting, and support for enterprises navigating digitalization challenges, with a focus on automotive testing, data management, and AI-driven automation.
layout: provider
modified: '2026-10-18'
name: Softwarehelden
nav: Providers
network: true
overview: 'Softwarehelden is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Digital Transformation, Automation, and AutomotiveTesting.


  Softwarehelden''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Softwarehelden Domain Security
  slug: softwarehelden-domain-security
  summary_line: TLSv1.3 · HSTS
slug: softwarehelden
tags:
- Company
- Artificial Intelligence
- Digital Transformation
- Automation
- AutomotiveTesting
website: https://softwarehelden.com/
---
