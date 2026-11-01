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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Dyson provides developer resources for its connected devices, documented on the support site.
  name: Dyson Support API
  slug: dyson-support-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dyson/llms/dyson-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dyson-llms.txt
- group: other
  href: https://artifacts.apis.io/dyson/hosts/dyson-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dyson-hosts.yml
- group: other
  href: https://artifacts.apis.io/dyson/vendors/dyson-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dyson-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dyson.com/inside-dyson/terms
- group: operate
  title: ''
  type: Support
  url: https://www.dyson.com/support
- group: start
  title: ''
  type: SignUp
  url: https://www.dyson.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.dyson.com/en/homepage.aspx
- group: company
  title: ''
  type: Newsroom
  url: https://www.dyson.com/discover/news
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dyson.com/support/floor-cleaners/wet/washg1/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.dyson.com/support/journey/guides/portable-fans
- group: auth
  href: https://artifacts.apis.io/dyson/security/dyson-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dyson-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dyson.com
coverage:
  checked: '2026-10-24'
  detail: Dyson's support documentation is rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://www.dyson.com/support
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Dyson is a British technology company that designs and manufactures household appliances such as vacuum cleaners, air purifiers, hair care tools, and lighting. Known for its innovative engineering and sleek design, Dyson sells products worldwide through its website and retail partners, and provides developer resources for its connected devices and services.
layout: provider
modified: '2026-10-24'
name: Dyson
nav: Providers
network: true
overview: 'Dyson is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Appliances, Innovation, and Consumer.


  Dyson''s developer surface includes support, signup flow, getting-started guide, documentation, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dyson Domain Security
  slug: dyson-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dyson
tags:
- Company
- Technology
- Appliances
- Innovation
- Consumer
website: https://www.dyson.com
---
