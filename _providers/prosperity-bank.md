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
  url: security/prosperity-bank-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prosperity-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.prosperitybankusa.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prosperity-bank
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prosperitybankusa.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prosperitybankusa.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.prosperitybankusa.com/contact-us
created: '2026-07-23'
description: 'Prosperity Bank is a Texas-chartered commercial bank (member FDIC, NMLS ID 466414) and the banking subsidiary of Prosperity Bancshares, Inc. (NYSE: PB), a Houston, Texas based regional financial holding company with roughly $37-43 billion in total assets and 300-plus full-service branches across Texas and central Oklahoma. It offers consumer and commercial banking, treasury management, mortgage, and wealth services, and has grown largely through acquisitions (LegacyTexas, Lone Star State Bancshares, American Bank Holding, Southwest Bancshares, Stellar Bancorp). On open finance, Prosperity Bank operates no first-party public developer portal or documented API: developer. and api. subdomains do not resolve, and no /developers or /api pages exist. Consumer-permissioned account and transaction data is reachable only through third-party aggregators (Finicity/Mastercard Open Banking, Plaid, and similar), not a directly published bank API. No FDX-conformant data-access API or CFPB
  Section 1033 posture is publicly documented by the bank as of this review.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Prosperity Bank
nav: Providers
network: true
overview: 'Prosperity Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Regional Bank, and Texas.


  Prosperity Bank''s developer surface includes support and 6 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prosperity-bank/refs/heads/main/screenshots/prosperity-bank-2026-09-02T152219.png
security:
- kind: domain-security
  name: Prosperity Bank Domain Security
  slug: prosperity-bank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: prosperity-bank
tags:
- Financial-Services
- Banking
- United States
- Regional Bank
- Texas
- Open Finance
- Data Aggregation
website: https://www.prosperitybankusa.com/
---
