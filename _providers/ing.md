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
api_count: 1
apis:
- description: The ING Developer Portal provides a marketplace of APIs covering Open Banking (PSD2 Account Information and Payment Initiation), payments, and bank-as-a-service capabilities. Third-party providers can
  name: ING Developer Portal APIs
  slug: ing-developer-portal
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ing-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ing-bank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ing
- group: company
  title: ''
  type: Website
  url: https://www.ing.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.ing.com/
- group: other
  title: ''
  type: Marketplace
  url: https://developer.ing.com/api-marketplace/marketplace
created: '2026-05-05'
description: A Dutch multinational banking and financial services corporation headquartered in Amsterdam. Provides retail banking, direct banking, commercial banking, and wholesale banking services to millions of customers across Europe and globally. Operates a public Developer Portal exposing Open Banking, PSD2, and payment-related APIs for third-party developers and fintech partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ing.png
layout: provider
modified: '2026-05-16'
name: ING
nav: Providers
network: true
overview: 'ING publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Banks, European Banking, Open Banking, and PSD2.


  ING''s developer surface includes developer portal and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 4.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ing/refs/heads/main/screenshots/ing-2026-06-20T183349.png
security:
- kind: domain-security
  name: Ing Domain Security
  slug: ing-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ing
tags:
- Financial
- Banks
- European Banking
- Open Banking
- PSD2
website: https://www.ing.com/
---
