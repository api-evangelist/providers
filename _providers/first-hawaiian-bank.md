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
api_count: 1
apis:
- description: First Hawaiian Bank exposes no public first-party API. Consumer-permissioned account and transaction data is available only through third-party financial data aggregators such as Plaid, which handle a
  name: First Hawaiian Bank Consumer Data Access (Aggregator-Only)
  slug: consumer-data-access
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-hawaiian-bank-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-hawaiian-bank-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/first-hawaiian-bank-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.fhb.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.fhb.com/en/online-mobile-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-hawaiian-bank
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fhb.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fhb.com/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.fhb.com/en/contact-us
created: '2026-07-23'
description: First Hawaiian Bank is Hawaii's oldest and largest financial institution, founded in 1858 and headquartered at First Hawaiian Center in Honolulu. It is a Hawaii state-chartered commercial bank and member FDIC, operating as the principal subsidiary of First Hawaiian, Inc. (NASDAQ ticker FHB), a publicly traded bank holding company. The bank serves consumer and commercial customers through roughly 57 branches in Hawaii plus locations in Guam and Saipan, offering deposit accounts, lending, wealth management, treasury/cash management, and merchant services. On the open-finance front, First Hawaiian operates no public first-party developer portal and publishes no downloadable OpenAPI/Swagger specifications; probes of developer.fhb.com, api.fhb.com, and fhb.com/en/developers returned no host or HTTP 404. Consumer-permissioned account data is reachable only through third-party aggregators (notably Plaid), not a direct bank API. No documented Financial Data Exchange (FDX) participation
  or published CFPB Section 1033 data-access posture was found as of this record. Its commercial online banking product (FHB Commercial Online, formerly OBC) is a traditional web application rather than a developer-facing API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: First Hawaiian Bank
nav: Providers
network: true
overview: 'First Hawaiian Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Hawaii, and Regional Bank.


  First Hawaiian Bank''s developer surface includes documentation, support, and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/first-hawaiian-bank/refs/heads/main/screenshots/first-hawaiian-bank-2026-07-25T214608.png
security:
- kind: domain-security
  name: First Hawaiian Bank Domain Security
  slug: first-hawaiian-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: first-hawaiian-bank
tags:
- Financial-Services
- Banking
- United States
- Hawaii
- Regional Bank
- Open Finance
- Data Aggregation
- Commercial Banking
website: https://www.fhb.com
---
