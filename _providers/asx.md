---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: REST programmatic interface to ASX Online's Market Information Application (Information Services), letting subscribers test connectivity, test token authentication, list the files of a subscribed prod
  name: ASX Market Information Application (MIA) REST API
  slug: asx-market-information-application-mia-rest-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/asx/plans/asx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asx-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/asx/conventions/asx-conventions.yml
  title: ''
  type: Conventions
  url: conventions/asx-conventions.yml
- group: auth
  href: https://artifacts.apis.io/asx/authentication/asx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asx-authentication.yml
- group: design
  href: https://artifacts.apis.io/asx/lifecycle/asx-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/asx-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/asx/errors/asx-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/asx-error-codes.yml
- group: other
  href: https://artifacts.apis.io/asx/hosts/asx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asx-hosts.yml
- group: other
  href: https://artifacts.apis.io/asx/vendors/asx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asx-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.asx.com.au/blog/investor-update/2026/the-rise-of-young-women-investors-nine-top-tips-for-getting-started
- group: auth
  href: https://artifacts.apis.io/asx/security/asx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.asx.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.asx.com.au/connectivity-and-data/information-services
- group: docs
  title: ''
  type: Documentation
  url: https://asxonline.com/public/documents/asxonline-information-services-user-guide.html
- group: docs
  title: ''
  type: APIReference
  url: https://asxonline.com/content/asxonline/public/documents/market-information-application--mia----rest-programmatic-interfa.html
- group: operate
  title: ''
  type: Support
  url: https://www.asx.com.au/about/contact-asx
- group: company
  title: ''
  type: Blog
  url: https://www.asx.com.au/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/asx
- group: operate
  title: ''
  type: StatusPage
  url: https://www.asx.com.au/content/asx/home/markets/market-resources/system-status.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.asx.com.au/issuers/issuer-services/pricing-calculator
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.asx.com.au/content/asx/home/legals/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asx.com.au/legals/privacy-statement
created: '2026-10-21'
description: ASX Limited (ABN 98 008 624 691) operates the Australian Securities Exchange, Australia's primary securities exchange. The ASX Group's activities span primary and secondary market services, including capital formation and hedging, trading and price discovery, clearing and settlement, and connectivity and market data. Through ASX Information Services (ASX Online) it licenses price, reference, benchmark and company-announcement data to subscribers, with a documented REST programmatic interface and Java downloader for the Market Information Application.
image: https://www.asx.com.au/content/asx/home.thumb.1000.1000.png
layout: provider
modified: '2026-10-21'
name: ASX
nav: Providers
network: true
overview: 'ASX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Stock Exchange, Financial Markets, Market Data, and Clearing and Settlement.


  ASX''s developer surface includes authentication, getting-started guide, documentation, API reference, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Asx Plans Pricing
  plan_count: 5
  slug: asx-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Asx Rate Limits
  slug: asx-rate-limits
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 33.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 24.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asx Authentication
  slug: asx-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Asx Domain Security
  slug: asx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asx
tags:
- Company
- Stock Exchange
- Financial Markets
- Market Data
- Clearing and Settlement
- Trading
- Australia
website: https://www.asx.com.au/
---
