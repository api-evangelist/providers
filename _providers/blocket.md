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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://vend.com/responsible-disclosure-policy.txt
- group: auth
  href: https://artifacts.apis.io/blocket/well-known/blocket-vend-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blocket-vend-security.txt
- group: auth
  href: https://artifacts.apis.io/blocket/well-known/blocket-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blocket-security.txt
- group: auth
  href: https://artifacts.apis.io/blocket/well-known/blocket-blocket-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blocket-blocket-security.txt
- group: agent
  href: https://artifacts.apis.io/blocket/well-known/blocket-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blocket-well-known.yml
- group: other
  href: https://artifacts.apis.io/blocket/hosts/blocket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blocket-hosts.yml
- group: build
  href: https://artifacts.apis.io/blocket/packages/blocket-packages.yml
  title: ''
  type: SDKs
  url: packages/blocket-packages.yml
- group: build
  href: https://artifacts.apis.io/blocket/packages/blocket-packages.yml
  title: ''
  type: Packages
  url: packages/blocket-packages.yml
- group: start
  title: ''
  type: Login
  url: https://www.blocket.se/auth/login
- group: auth
  href: https://artifacts.apis.io/blocket/security/blocket-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blocket-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blocket/security/blocket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blocket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blocket.se/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blocket.se/villkor
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vend.com/privacy/se-policy
- group: operate
  title: ''
  type: Support
  url: https://blocket.zendesk.com/hc/sv
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://blocket.zendesk.com/mcp
  - status: 200
    url: https://blocket.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Blocket is Sweden’s largest online marketplace for buying and selling new and used items, ranging from cars, furniture, electronics, to real estate and services. It connects millions of users across the country, offering a platform for classifieds, auctions, and business listings. The site provides search, messaging, and secure transaction features, serving both private individuals and companies.
layout: provider
modified: '2026-10-15'
name: Blocket
nav: Providers
network: true
overview: 'Blocket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Classifieds, E-Commerce, Sweden, and Online Ads.


  Blocket''s developer surface includes support and 14 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 15.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blocket Domain Security
  slug: blocket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blocket Vulnerability Disclosure
  slug: blocket-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: blocket
tags:
- Marketplace
- Classifieds
- E-Commerce
- Sweden
- Online Ads
website: https://blocket.se/
---
