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
api_count: 1
apis:
- description: Equitable Bank / EQ Bank exposes no public first-party developer API. Under explicit customer consent, EQ Bank customers can share their financial data with third-party fintech applications through th
  name: EQ Bank Consumer Data Sharing (via Flinks)
  slug: eq-bank-consumer-data-sharing
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/equitable-bank-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/equitable-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.equitablebank.ca
- group: company
  title: ''
  type: Website
  url: https://www.eqbank.ca
- group: company
  title: ''
  type: Blog
  url: https://www.equitablebank.ca/blog
- group: operate
  title: ''
  type: Support
  url: https://www.equitablebank.ca/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.equitablebank.ca/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.equitablebank.ca/legal/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/equitable-bank
created: '2026-07-23'
description: 'Equitable Bank is Canada''s seventh largest independent Schedule I bank by assets and a wholly owned subsidiary of EQB Inc. (TSX: EQB), a Toronto-based Canadian financial services company with over CAD $144 billion in combined assets under management and administration. Federally chartered and Canadian owned, Equitable Bank markets itself as "Canada''s Challenger Bank" and, in 2016, launched EQ Bank, its digital-only banking platform offering high interest savings accounts, GICs, and payments alongside the parent bank''s single-family residential and commercial lending. Equitable Bank and Equitable Trust are members of the Canada Deposit Insurance Corporation (CDIC). On the open-finance front, Equitable Bank does not operate a public first-party developer portal or publish downloadable API specifications; consumer permissioned data sharing is delivered through the Canadian aggregator Flinks (Flinks Outbound) rather than a first-party API. Canada''s federal Consumer-Driven Banking
  framework (legislated in Budget 2024 with the Financial Consumer Agency of Canada as overseer) is not yet operational, so the bank''s data-access posture today is voluntary and aggregator-mediated.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Equitable Bank
nav: Providers
network: true
overview: 'Equitable Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Schedule I Bank, and Digital Banking.


  Equitable Bank''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/equitable-bank/refs/heads/main/screenshots/equitable-bank-2026-07-25T213552.png
security:
- kind: domain-security
  name: Equitable Bank Domain Security
  slug: equitable-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: equitable-bank
tags:
- Financial-Services
- Banking
- Canada
- Schedule I Bank
- Digital Banking
- Open Banking
- Consumer-Driven Banking
- Data Aggregation
- Challenger Bank
website: https://www.equitablebank.ca
---
