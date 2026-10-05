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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aviasales/refs/heads/main/hosts/aviasales-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aviasales-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aviasales/refs/heads/main/vendors/aviasales-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aviasales-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aviasales/refs/heads/main/packages/aviasales-packages.yml
  title: ''
  type: SDKs
  url: packages/aviasales-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aviasales/refs/heads/main/packages/aviasales-packages.yml
  title: ''
  type: Packages
  url: packages/aviasales-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aviasales.ru/terms-of-use
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aviasales/refs/heads/main/security/aviasales-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aviasales-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aviasales.ru/
- group: company
  title: ''
  type: Blog
  url: https://www.aviasales.ru/psgr
- group: operate
  title: ''
  type: Support
  url: https://www.aviasales.ru/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aviasales.ru/privacy
coverage:
  checked: '2026-09-26'
  detail: No machine‑readable API specification was found; only HTML pages such as the Terms of Service are available.
  evidence:
  - status: 200
    url: https://www.aviasales.ru/terms-of-use
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Aviasales is a leading Russian online travel service that helps users find and purchase the cheapest airline tickets. The platform aggregates offers from over 2000 airlines, covering routes to more than 190 countries, and also provides hotel bookings, travel guides, and personalized travel experiences. It serves millions of travelers annually, offering price comparisons, flexible search options, and a user-friendly interface for planning trips.
layout: provider
modified: '2026-09-26'
name: Aviasales
nav: Providers
network: true
overview: 'Aviasales is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Flights, Booking, and Russia.


  Aviasales'' developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aviasales Domain Security
  slug: aviasales-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aviasales
tags:
- Company
- Travel
- Flights
- Booking
- Russia
website: https://www.aviasales.ru/
---
