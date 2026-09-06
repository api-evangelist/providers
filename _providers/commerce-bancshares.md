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
- description: Commerce Bank's corporate API program, published through a registration-gated external developer portal and the CommercePayments developer platform, covering payments, treasury, and embedded-banking i
  name: Commerce Bank Developer APIs
  slug: commerce-developer-apis
artifact_total: 2
common:
- group: start
  title: ''
  type: Login
  url: https://banking.commercebank.com/cbi/login.aspx
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commerce-bancshares-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.commercebank.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.commercebank.com/
- group: company
  title: ''
  type: Blog
  url: https://www.commercebank.com/business/trends-and-insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.commercebank.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commercebank.com/security-center/privacy-statement
- group: operate
  title: ''
  type: Support
  url: https://www.commercebank.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commerce_bank
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commerce-bancshares-llms.txt
created: '2026-07-23'
description: 'Commerce Bank is the principal banking subsidiary of Commerce Bancshares, Inc. (NASDAQ CBSH), a Missouri-based regional bank holding company with roughly $32 billion in assets and dual headquarters in Kansas City and St. Louis. Commerce Bank is a Missouri state-chartered bank and Federal Reserve member, founded in 1865, offering personal, business, commercial, and wealth-management services across the U.S. Midwest. Its API posture is corporate/embedded-banking oriented rather than a fully open public program: it runs a registration-gated external developer portal (developers.commercebank.com) and a CommercePayments developer platform, and delivers ERP-embedded banking via Commerce Connections Direct. Consumer-permissioned data sharing is largely intermediated through aggregators such as Plaid and platforms like Modern Treasury rather than a documented first-party, self-serve open-banking API. No public FDX or CFPB Section 1033 data-access posture is documented, and no downloadable
  OpenAPI/Swagger is publicly available.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Commerce Bank
nav: Providers
network: true
overview: 'Commerce Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Regional Bank, and Payments.


  Commerce Bank''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commerce-bancshares/refs/heads/main/screenshots/commerce-bancshares-2026-07-25T210127.png
security:
- kind: domain-security
  name: Commerce Bancshares Domain Security
  slug: commerce-bancshares-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commerce-bancshares
tags:
- Financial-Services
- Banking
- United States
- Regional Bank
- Payments
- Treasury Management
- Embedded Banking
- Open Finance
- Data Aggregation
website: https://www.commercebank.com/
---
