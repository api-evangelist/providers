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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/scotiabank/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tangerine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tangerine.ca
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tangerine.ca/en/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tangerine.ca/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.tangerine.ca/en/help-centre
- group: company
  title: ''
  type: Blog
  url: https://www.tangerine.ca/en/thejuice
- group: start
  title: ''
  type: SignUp
  url: https://www.tangerine.ca/app/#/visitor-enroll/instructions?locale=en_CA
- group: start
  title: ''
  type: Login
  url: https://www.tangerine.ca/app/#/login/login-id?locale=en_CA
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/tangerine-bank
created: '2026-07-23'
description: Tangerine is a Canadian direct (branchless) bank headquartered in Toronto, Ontario, and a federally regulated Schedule I bank chartered as Tangerine Bank (institution number 614). Founded in 1997 as ING Direct Canada, it was acquired by Scotiabank in 2012 and rebranded as Tangerine in 2014; it remains a separate legal entity operating as Scotiabank's digital-banking arm, serving roughly two million clients with no-fee chequing and savings accounts, GICs, mortgages, mutual funds, and a cash-back Mastercard delivered entirely through mobile and web. On API and open-finance posture, Tangerine publishes no first-party public developer portal or downloadable API specifications; Canada has no operational consumer-driven-banking mandate yet (the federal framework is legislated but not live), so third-party access to Tangerine account and transaction data today is aggregator-based via Plaid and Finicity (Mastercard) rather than through a documented first-party API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Tangerine
nav: Providers
network: true
overview: 'Tangerine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Digital Bank, and Neobank.


  Tangerine''s developer surface includes support, engineering blog, signup flow, and 7 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tangerine/refs/heads/main/screenshots/tangerine-2026-09-02T162525.png
security:
- kind: domain-security
  name: Tangerine Domain Security
  slug: tangerine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tangerine
tags:
- Financial-Services
- Banking
- Canada
- Digital Bank
- Neobank
- Schedule I Bank
- Data Aggregation
- Interac
website: https://www.tangerine.ca
---
