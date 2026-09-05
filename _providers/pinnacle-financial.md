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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinnacle-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pnfp.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pnfp/
- group: operate
  title: ''
  type: Support
  url: https://www.pnfp.com/contact-us/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.pnfp.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pnfp.com/privacy-practices/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pinnacle-financial-llms.txt
created: '2026-07-23'
description: 'Pinnacle Financial Partners, Inc. (NASDAQ: PNFP) is a Nashville, Tennessee based regional bank holding company whose principal subsidiary, Pinnacle Bank, is a Tennessee state-chartered, FDIC-insured commercial bank (FDIC Cert #35583) originally founded in 2000 as Pinnacle National Bank and renamed in 2012. Pinnacle operates across the Southeast — Tennessee, the Carolinas, Virginia, Georgia and Alabama — serving consumer, small-business, commercial and wealth clients. On the open-finance side Pinnacle runs NO public first-party developer API portal; its consumer digital and mobile banking is delivered on a third-party core/digital platform (Apiture), and consumer-permissioned account and transaction data is made available to fintechs only through data aggregators (Plaid and Finicity/Mastercard) rather than through a documented bank-operated API. No direct Financial Data Exchange (FDX) membership or published CFPB Section 1033 data-access posture was found; open-finance participation
  is aggregator-mediated.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Pinnacle Financial
nav: Providers
network: true
overview: 'Pinnacle Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Regional Bank, and Open Finance.


  Pinnacle Financial''s developer surface includes support and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pinnacle-financial/refs/heads/main/screenshots/pinnacle-financial-2026-09-02T151303.png
security:
- kind: domain-security
  name: Pinnacle Financial Domain Security
  slug: pinnacle-financial-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pinnacle-financial
tags:
- Financial-Services
- Banking
- United States
- Regional Bank
- Open Finance
- Data Aggregation
website: https://www.pnfp.com/
---
