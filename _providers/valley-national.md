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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valley-national-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://valley.com
- group: company
  title: ''
  type: Blog
  url: https://valley.com/about/newsroom
- group: operate
  title: ''
  type: Support
  url: https://valley.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://valley.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://valley.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/valley-bank
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ValleyNationalBank
created: '2026-07-23'
description: 'Valley National Bank is a nationally chartered commercial bank (OCC-regulated) and the principal banking subsidiary of Valley National Bancorp (NASDAQ: VLY), a regional financial holding company founded in 1927 with roughly $64 billion in assets and more than 200 offices serving consumers, families, and businesses across New Jersey, New York, Florida, Alabama, California, and Illinois. Its business spans consumer banking, commercial banking, and treasury services. As of this profile Valley National Bank operates no first-party public developer portal and publishes no downloadable API specifications; consumer-permissioned account and transaction data is reached only through third-party open-finance aggregators (Finicity by Mastercard is documented, alongside general Plaid/Tink connectivity) rather than a directly exposed FDX-conformant or first-party API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Valley National Bank
nav: Providers
network: true
overview: 'Valley National Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Regional Bank, and Commercial Banking.


  Valley National Bank''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valley-national/refs/heads/main/screenshots/valley-national-2026-09-02T165326.png
security:
- kind: domain-security
  name: Valley National Domain Security
  slug: valley-national-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: valley-national
tags:
- Financial-Services
- Banking
- United States
- Regional Bank
- Commercial Banking
- Open Finance
- Data Aggregation
website: https://valley.com
---
