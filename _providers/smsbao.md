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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/smsbao/hosts/smsbao-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smsbao-hosts.yml
- group: build
  href: https://artifacts.apis.io/smsbao/packages/smsbao-packages.yml
  title: ''
  type: Packages
  url: packages/smsbao-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.smsbao.com/help
- group: build
  title: ''
  type: SDKs
  url: https://www.smsbao.com/tags/SDK
- group: company
  title: ''
  type: Newsroom
  url: https://www.smsbao.com/news
- group: start
  title: ''
  type: Login
  url: https://www.smsbao.com/login
- group: auth
  href: https://artifacts.apis.io/smsbao/security/smsbao-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smsbao-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smsbao.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.smsbao.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: SmsBao, operated by Shanghai Zi Cheng Electronic Technology Co., Ltd., provides enterprise SMS services since 2015. It offers verification, notification, and marketing SMS with high throughput, supporting over 100,000 registered users and delivering up to 360,000 messages per hour across China and globally. The platform includes API documentation, SDK examples in multiple languages, and a console for message tracking and billing.
layout: provider
modified: '2026-10-27'
name: SmsBao
nav: Providers
network: true
overview: 'SmsBao is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SMS, Messaging, API, China, and Enterprise.


  SmsBao''s developer surface includes support and 7 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 46.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Smsbao Domain Security
  slug: smsbao-domain-security
  summary_line: TLSv1.3 · HSTS
slug: smsbao
tags:
- SMS
- Messaging
- API
- China
- Enterprise
website: https://www.smsbao.com/
---
