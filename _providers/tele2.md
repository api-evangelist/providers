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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/tele2/well-known/tele2-tele2-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tele2-tele2-security.txt
- group: auth
  href: https://artifacts.apis.io/tele2/well-known/tele2-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tele2-security.txt
- group: agent
  href: https://artifacts.apis.io/tele2/well-known/tele2-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tele2-well-known.yml
- group: other
  href: https://artifacts.apis.io/tele2/hosts/tele2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tele2-hosts.yml
- group: other
  href: https://artifacts.apis.io/tele2/vendors/tele2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tele2-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tele2.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tele2.com/investors/the-share/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://www.tele2.com/media
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tele2.com/
- group: auth
  href: https://artifacts.apis.io/tele2/security/tele2-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tele2-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tele2/security/tele2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tele2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tele2.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://tele2.com/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Tele2 is a leading European telecommunications operator offering mobile, broadband, and digital services across multiple countries. It focuses on innovative, affordable connectivity solutions for consumers and businesses, emphasizing sustainability and smart network technologies. The company operates in Sweden, the Baltics, and other markets, providing 5G, IoT, and wholesale services, and maintains a corporate website with extensive information about its vision, governance, and offerings.
image: https://www.tele2.com/files/HuvudKVkomprimerad1THUMB.jpg
layout: provider
modified: '2026-10-14'
name: Tele2
nav: Providers
network: true
overview: 'Tele2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Mobile, Broadband, and Europe.


  Tele2''s developer surface includes documentation and 11 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 49.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 9.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 11.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tele2/tele2-2026-11-03T144412.png
security:
- kind: domain-security
  name: Tele2 Domain Security
  slug: tele2-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tele2 Vulnerability Disclosure
  slug: tele2-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tele2
tags:
- Company
- Telecommunications
- Mobile
- Broadband
- Europe
website: https://tele2.com/
---
