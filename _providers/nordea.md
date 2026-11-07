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
  href: https://artifacts.apis.io/nordea/hosts/nordea-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nordea-hosts.yml
- group: other
  href: https://artifacts.apis.io/nordea/vendors/nordea-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nordea-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nordea.com/en/terms-and-conditions-trade
- group: operate
  title: ''
  type: Support
  url: https://www.nordea.com/en/our-services/cash-management/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nordea.com/en/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nordea.com/en/doc/price-list-for-account-holding-banks-2026.pdf
- group: company
  title: ''
  type: Newsroom
  url: https://www.nordea.com/en/media/15019
- group: start
  title: ''
  type: Login
  url: https://www.nordea.com/en/log-in
- group: auth
  href: https://artifacts.apis.io/nordea/security/nordea-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nordea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nordea.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://nordea.com/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Nordea is a leading Nordic universal bank offering a wide range of financial services including retail banking, corporate banking, asset management, and investment solutions across the Nordic region. The bank focuses on digital transformation and provides various APIs for account information, payments, and financial data to enable seamless integration for developers and partners.
image: https://www.nordea.com/sites/default/files/styles/olivero_hero/public/2024-05/top-banner-test-1.jpg.webp?itok=glXlPnGU
layout: provider
modified: '2026-10-14'
name: Nordea
nav: Providers
network: true
overview: 'Nordea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Finance, and Nordic.


  Nordea''s developer surface includes support, pricing, and 8 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 40.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 12.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nordea/nordea-2026-11-03T140254.png
security:
- kind: domain-security
  name: Nordea Domain Security
  slug: nordea-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: nordea
tags:
- Company
- Banking
- Finance
- Nordic
website: https://nordea.com/
---
