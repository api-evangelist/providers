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
  href: https://artifacts.apis.io/lockheed-martin/hosts/lockheed-martin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lockheed-martin-hosts.yml
- group: other
  href: https://artifacts.apis.io/lockheed-martin/vendors/lockheed-martin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lockheed-martin-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lockheedmartin.com/en-us/suppliers/business-area-procurement/aeronautics/terms-and-conditions.html
- group: other
  title: ''
  type: Leadership
  url: https://www.lockheedmartin.com/en-au/leadership/jeremy-king.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.lockheedmartin.com/en-us/suppliers/documentation/2026tandc.html
- group: auth
  href: https://artifacts.apis.io/lockheed-martin/security/lockheed-martin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lockheed-martin-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lmco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lockheed-martin
- group: company
  title: ''
  type: Website
  url: https://www.lockheedmartin.com
- group: company
  title: ''
  type: Careers
  url: https://www.lockheedmartinjobs.com
- group: company
  title: ''
  type: Newsroom
  url: https://news.lockheedmartin.com
- group: other
  title: ''
  type: Suppliers
  url: https://www.lockheedmartin.com/en-us/suppliers.html
- group: company
  title: ''
  type: Blog
  url: https://news.lockheedmartin.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lockheedmartin.com/en-us/contact/privacy-center.html
- group: operate
  title: ''
  type: Support
  url: https://www.lockheedmartin.com/en-us/contact.html
coverage:
  checked: '2026-10-20'
  detail: Lockheed Martin publishes no developer portal or API; api.lockheedmartin.com and developer.lockheedmartin.com do not resolve, no OpenAPI/llms.txt is served on www.lockheedmartin.com, and its only public technical surface is open-source code in github.com/lmco.
  evidence:
  - status: 0
    url: https://api.lockheedmartin.com
  - status: 0
    url: https://developer.lockheedmartin.com
  - status: 404
    url: https://www.lockheedmartin.com/openapi.json
  - status: 404
    url: https://www.lockheedmartin.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: Lockheed Martin is a global security, defense, and aerospace company headquartered in Bethesda, Maryland, building aircraft, missiles, space systems, and mission software for government customers. It publishes no public developer program or API; its public technical footprint is open-source work in the lmco GitHub organization (e.g. Laika BOSS, Hoppr, Dependency-Track forks).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lockheed-martin.png
layout: provider
modified: '2026-10-20'
name: Lockheed Martin
nav: Providers
network: true
overview: 'Lockheed Martin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Defense, Aerospace, Security, Fortune 500, and Open Source.


  Lockheed Martin''s developer surface includes documentation, engineering blog, support, and 12 more developer resources.'
press:
- date: ''
  title: Search our Job Opportunities at Lockheed Martin Corporation
  url: https://www.lockheedmartinjobs.com/search-jobs
- date: ''
  title: Lockheed Martin Corporation (LMT) Stock Price, News ...
  url: https://finance.yahoo.com/quote/LMT/
- date: ''
  title: Lockheed Corporation
  url: https://en.wikipedia.org/wiki/Lockheed_Corporation
- date: ''
  title: 'Lockheed Martin: Leading Aerospace and Defense'
  url: https://www.lockheedmartin.com/en-us/index.html
- date: ''
  title: Lockheed Martin
  url: https://en.wikipedia.org/wiki/Lockheed_Martin
random_paper: 15
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lockheed-martin/lockheed-martin-2026-06-20T184639.png
security:
- kind: domain-security
  name: Lockheed Martin Domain Security
  slug: lockheed-martin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lockheed-martin
tags:
- Defense
- Aerospace
- Security
- Fortune 500
- Open Source
- Government
website: https://www.lockheedmartin.com
---
