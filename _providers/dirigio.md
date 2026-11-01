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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dirigio/hosts/dirigio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dirigio-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://dirigio.jp/news
- group: auth
  href: https://artifacts.apis.io/dirigio/security/dirigio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dirigio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dirigio.jp
- group: docs
  title: ''
  type: Documentation
  url: https://dirigio.jp/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dirigio.jp/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dirigio.jp/privacy-handling
- group: operate
  title: ''
  type: Contact
  url: https://dirigio.jp/contact
coverage:
  checked: '2026-10-23'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found on the provider's site.
  evidence:
  - status: 200
    url: https://dirigio.jp/about
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Dirigio is a Japanese technology company providing a mobile order platform called PICKS for restaurants. It connects stores, customers, and staff through its platform, offering features like coupon distribution, loyalty stamps, and friend referrals. The company aims to enhance the dining experience by leveraging technology to streamline ordering and foster community connections.
image: https://dirigio.jp/og-image.png
layout: provider
modified: '2026-10-23'
name: Dirigio
nav: Providers
network: true
overview: 'Dirigio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, RestaurantTech, Mobile Ordering, Japan, and Platform.


  Dirigio''s developer surface includes documentation and 7 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
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
  name: Dirigio Domain Security
  slug: dirigio-domain-security
  summary_line: TLSv1.2 · DMARC
slug: dirigio
tags:
- Company
- RestaurantTech
- Mobile Ordering
- Japan
- Platform
website: https://dirigio.jp
---
