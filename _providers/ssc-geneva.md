---
access_model:
  confidence: medium
  label: Pricing unknown · Enterprise, client-only (on request)
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - website
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 5
apis:
- description: Investor accounts and capital activity
  name: SS&C Geneva Investors API
  slug: ssc-geneva-investors-api
- description: Net Asset Value calculation and reporting
  name: SS&C Geneva NAV API
  slug: ssc-geneva-nav-api
- description: Portfolio and fund management
  name: SS&C Geneva Portfolios API
  slug: ssc-geneva-portfolios-api
- description: Portfolio positions and holdings
  name: SS&C Geneva Positions API
  slug: ssc-geneva-positions-api
- description: Trade capture and processing
  name: SS&C Geneva Trades API
  slug: ssc-geneva-trades-api
artifact_total: 6
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ssc-geneva/overview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/security/ssc-geneva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ssc-geneva-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ssc-advent
- group: company
  title: ''
  type: Website
  url: https://www.ssctech.com/
- group: start
  title: ''
  type: Portal
  url: https://www.ssctech.com/products
- group: company
  title: ''
  type: Blog
  url: https://www.ssctech.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ssctech.com/about/support-client-portals
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ssctech.com/about/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.ssctech.com/resources
coverage:
  detail: SS&C publishes no public API reference or machine-readable specification for Geneva. Integration documentation is provided to licensed clients through SS&C's client portals. A placeholder OpenAPI (placeholder server on a reserved example domain) and everything derived from it were quarantined to _scaffold/ on 2026-10-17.
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-03-18'
description: SS&C Geneva is an enterprise-grade fund accounting and portfolio management platform for asset managers, hedge funds, and fund administrators. Geneva supports NAV calculation, trade processing, investor accounting, position management, and regulatory reporting across multi-asset portfolios including equities, fixed income, derivatives, and alternative investments.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ssc-geneva.png
layout: provider
modified: '2026-05-19'
name: SS&C Geneva
nav: Providers
network: true
overview: 'SS&C Geneva is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fund Accounting, Asset Management, Portfolio Management, Financial Services, and Hedge Funds.


  SS&C Geneva''s developer surface includes developer portal, engineering blog, support, documentation, and 5 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -25.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 30.5
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 39.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/screenshots/ssc-geneva-2026-06-20T194436.png
security:
- kind: domain-security
  name: Ssc Geneva Domain Security
  slug: ssc-geneva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ssc-geneva
tags:
- Fund Accounting
- Asset Management
- Portfolio Management
- Financial Services
- Hedge Funds
- NAV Calculation
website: https://www.ssctech.com/
---
