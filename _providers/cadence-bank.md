---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - '{''url'': ''https://www.cadencebank.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.huntington.com/landing-pages/cadencebank — a different registrable domain (cadencebank.com -> huntington.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cadence-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cadencebank.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cadence-bank
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.cadencebank.com/
- group: operate
  title: ''
  type: Support
  url: https://cadencebank.com/customer-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cadencebank.com/policies-and-disclosures/online-privacy-disclosure
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cadencebank.com/policies-and-disclosures
- group: start
  title: ''
  type: Login
  url: https://portal.cadencebank.com/consumer/SignOn.aspx
created: '2026-07-23'
description: Cadence Bank is a regional U.S. commercial bank headquartered in Tupelo, Mississippi and Houston, Texas, formed in October 2021 when legacy Cadence Bancorporation merged into BancorpSouth Bank (the surviving entity, subsequently renamed Cadence Bank; NYSE ticker CADE). It is a Mississippi state-chartered bank operating roughly 400+ branches across the U.S. South, Midwest, and Texas with about $48-50 billion in assets, offering consumer banking, mortgages, home equity, credit cards, small business and commercial banking, treasury management, and wealth/insurance services. On open finance, Cadence Bank exposes no first-party public developer API or developer portal; consumer-permissioned account data is reachable only through third-party aggregators (notably Plaid), which is the honest, prevailing posture for most U.S. regional banks. No documented direct FDX (Financial Data Exchange) membership or published CFPB Section 1033 data-access API was found as of this profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Cadence Bank
nav: Providers
network: true
overview: 'Cadence Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Regional Bank, and Commercial Banking.


  Cadence Bank''s developer surface includes support and 7 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cadence-bank/refs/heads/main/screenshots/cadence-bank-2026-07-25T204210.png
security:
- kind: domain-security
  name: Cadence Bank Domain Security
  slug: cadence-bank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cadence-bank
tags:
- Financial-Services
- Banking
- United States
- Regional Bank
- Commercial Banking
- Treasury Management
- Open Finance
- Data Aggregation
website: https://www.cadencebank.com/
---
