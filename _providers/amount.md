---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amount-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amount.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amount
created: '2026-07-17'
description: Amount is a Chicago-based financial technology company that provides banks, credit unions, and fintechs with a digital lending and account-origination platform. Spun out of the consumer lender Avant in 2020 and backed by QED Investors, Amount delivers configurable software for personal loans, point-of-sale and buy-now-pay-later financing, deposit and account opening, and integrated fraud, identity verification, and decisioning. Its product API is delivered to enterprise banking customers through a private, credentialed developer portal (docs.amount.com) rather than a public self-serve API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amount.png
layout: provider
modified: '2026-07-17'
name: Amount
nav: Providers
network: true
overview: Amount is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Lending, Banking, and Financial-Services.
random_paper: 9
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Amount Domain Security
  slug: amount-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: amount
tags:
- Company
- Fintech
- Lending
- Banking
- Financial-Services
- Loan Origination
- Account Opening
- Fraud
- Decisioning
- Buy Now Pay Later
website: https://amount.com
---
