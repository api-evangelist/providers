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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Raymond James Bank exposes no first-party public API. Consumer-permissioned account and transaction data is available only indirectly through third-party data aggregators (e.g., Plaid). This entry is '
  name: Raymond James Bank Consumer Data Access (Aggregator-Only)
  slug: raymond-james-bank-data-access
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raymond-james-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.raymondjamesbank.com/
- group: company
  title: ''
  type: About
  url: https://www.raymondjamesbank.com/more/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.raymondjamesbank.com/more/news-and-media
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.raymondjamesbank.com/privacy-and-security-statements
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.raymondjamesbank.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.raymondjamesbank.com/more/contact-us
- group: start
  title: ''
  type: Login
  url: https://www.raymondjamesbank.com/account-login
created: '2026-07-23'
description: 'Raymond James Bank is a Florida-chartered state member bank headquartered in St. Petersburg, Florida, and a wholly owned subsidiary of Raymond James Financial, Inc. (NYSE: RJF), a diversified financial services holding company founded in 1962. Supervised by the Federal Reserve and the Florida Office of Financial Regulation, the bank provides securities-based lending, residential mortgages, commercial and industrial and commercial real estate loans, tax-exempt loans, and deposit products (including its Enhanced Savings Program) primarily to Raymond James wealth-management and institutional clients. On open finance, the bank runs no first-party public developer portal and publishes no downloadable API specifications; consumer-permissioned account data is reachable only indirectly through third-party aggregators such as Plaid. No FDX participation or CFPB Section 1033 data-access posture is publicly documented for this institution as of this record.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Raymond James Bank
nav: Providers
network: true
overview: 'Raymond James Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Wealth Management, and Securities-Based Lending.


  Raymond James Bank''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/raymond-james-bank/refs/heads/main/screenshots/raymond-james-bank-2026-09-02T152931.png
security:
- kind: domain-security
  name: Raymond James Bank Domain Security
  slug: raymond-james-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: raymond-james-bank
tags:
- Financial-Services
- Banking
- United States
- Wealth Management
- Securities-Based Lending
- Open Finance
- Data Aggregation
website: https://www.raymondjamesbank.com/
---
