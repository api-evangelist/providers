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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streamloan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://streamloan.io
created: '2026-07-17'
description: StreamLoan was a digital mortgage software company offering a point-of-sale (POS) and loan-origination platform that connected loan officers, borrowers, and real-estate agents to convert leads into funded home loans faster. Its toolkit spanned lead management, borrower communication and collaboration, workflow automation, document collection, security/privacy controls, and a branded borrower experience aimed at cutting the 40+ day mortgage close cycle. Backed by 500 Global. As of this enrichment pass the company appears defunct - streamloan.io is parked on a registrar IP and every developer/app/api/docs/portal subdomain is unreachable (DNS records remain but no host responds), and no public API or developer program was ever documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/streamloan.png
layout: provider
modified: '2026-07-21'
name: StreamLoan
nav: Providers
network: true
overview: StreamLoan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mortgage, Lending, Loan Origination, and Point-of-Sale.
random_paper: 7
score:
  band: minimal
  composite: 1.5
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
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Streamloan Domain Security
  slug: streamloan-domain-security
  summary_line: no transport/DNS hardening detected
slug: streamloan
tags:
- Company
- Mortgage
- Lending
- Loan Origination
- Point-of-Sale
- Fintech
- Real-Estate
- Software-as-a-Service
- Banking
- Financial-Services
website: https://streamloan.io
---
