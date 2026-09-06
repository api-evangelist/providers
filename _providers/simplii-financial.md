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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simplii-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.simplii.com/en/home.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.simplii.com/en/legal.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.simplii.com/en/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.simplii.com/en/legal.html
- group: operate
  title: ''
  type: Support
  url: https://www.simplii.com/en/contact-us.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simplii-financial
created: '2026-07-23'
description: Simplii Financial is the no-fee direct banking brand of the Canadian Imperial Bank of Commerce (CIBC), one of Canada's Big Six Schedule I domestic banks. Launched November 1, 2017, Simplii succeeded CIBC's two-decade President's Choice Financial (PC Financial) co-venture with Loblaws, migrating roughly two million accounts to the new brand. Simplii is not a separately chartered bank; it operates as a division and trade name of CIBC under CIBC's Schedule I federal charter, offering no-fee daily chequing and savings, mortgages, personal loans, lines of credit, GICs, mutual funds, and USD accounts through online, mobile, and telephone channels only (no branches), with CDIC deposit insurance provided through CIBC. On open finance, Simplii exposes no first-party public developer API or developer portal; consumer financial-data access today is aggregator- and screen-scraping-based via Plaid, Finicity, and MX (CIBC signed a data-access agreement with MX), consistent with Canada's voluntary,
  pre-mandate posture while the federal Consumer-Driven Banking framework (Budget 2024 / FES 2024, overseen by the FCAC) is legislated but not yet operational.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Simplii Financial
nav: Providers
network: true
overview: 'Simplii Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Digital Bank, and Direct Banking.


  Simplii Financial''s developer surface includes documentation, support, and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simplii-financial/refs/heads/main/screenshots/simplii-financial-2026-09-02T155548.png
security:
- kind: domain-security
  name: Simplii Financial Domain Security
  slug: simplii-financial-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: simplii-financial
tags:
- Financial-Services
- Banking
- Canada
- Digital Bank
- Direct Banking
- Big Six
- CIBC
- Consumer-Driven Banking
- Data Aggregation
website: https://www.simplii.com/en/home.html
---
