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
- description: 'Marcus by Goldman Sachs does not publish a first-party consumer developer API. Consumer-permissioned account data is available only through third-party open-finance aggregators. Plaid supports Marcus '
  name: Marcus Consumer Data Access (Aggregator-Only)
  slug: marcus-aggregator-data-access
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marcus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.marcus.com/us/en
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goldman-sachs
- group: operate
  title: ''
  type: Support
  url: https://www.marcus.com/us/en/help-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.marcus.com/us/en/site-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marcus.com/us/en/privacy-policy
created: '2026-07-23'
description: Marcus by Goldman Sachs is the U.S. consumer banking brand of The Goldman Sachs Group, launched in 2016 to offer no-fee high-yield Online Savings Accounts and Certificates of Deposit (CDs) directly to retail customers online. Deposits are held at Goldman Sachs Bank USA, a New York State-chartered bank and member of the Federal Reserve System, insured by the FDIC. After Goldman's broad retreat from consumer lending, Marcus no longer originates personal loans and now centers on digital deposit products. Marcus operates NO public first-party consumer developer API and runs no self-serve developer portal for its retail banking products; the Goldman Sachs Developer platform (developer.gs.com) serves institutional Transaction Banking and Marquee offerings, not Marcus consumer banking. Consumer-permissioned account data (balances, transactions, account/holder info) is reachable only through third-party open-finance aggregators such as Plaid, Flinks, and MX, not a documented Marcus
  API. As a bank chartered in the U.S., Goldman Sachs Bank USA is subject to the emerging CFPB Section 1033 personal financial data rights framework, but no first-party FDX-conformant Marcus developer interface is publicly documented as of this record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Marcus by Goldman Sachs
nav: Providers
network: true
overview: 'Marcus by Goldman Sachs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Consumer Banking, and Neobank.


  Marcus by Goldman Sachs'' developer surface includes support and 5 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
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
  previous_composite: 11.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Marcus Domain Security
  slug: marcus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marcus
tags:
- Financial-Services
- Banking
- United States
- Consumer Banking
- Neobank
- Digital Banking
- Savings
- Open Finance
- Data Aggregation
website: https://www.marcus.com/us/en
---
