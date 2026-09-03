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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citi-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/citi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/citi
- group: company
  title: ''
  type: Website
  url: https://www.citi.com
- group: start
  title: ''
  type: Portal
  url: https://developer.citi.com/
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.developerhub.citi.com/
- group: other
  title: ''
  type: API Catalog
  url: https://sandbox.developerhub.citi.com/api-catalog-list
- group: other
  title: ''
  type: Canonical Profile
  url: https://raw.githubusercontent.com/api-evangelist/citigroup/refs/heads/main/apis.yml
created: '2026-03-21'
description: Citi is the consumer-facing brand of Citigroup, the global diversified financial services holding company. The Citi developer surface is cataloged under the canonical Citigroup profile, which covers the Citi Developer Hub, retail Accounts and Transactions, Money Movement, Authorization, Customer Onboarding, Pay with Points, Utilities, and CitiConnect for corporate treasury. This entry exists as an alias so the citi short name resolves to the same catalog as citigroup.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/citi.png
layout: provider
modified: '2026-04-23'
name: Citi
nav: Providers
network: true
overview: 'Citi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial-Services, Open Banking, Payments, and Treasury.


  Citi''s developer surface includes developer portal, sandbox, and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/citi/refs/heads/main/screenshots/citi-2026-06-20T174409.png
security:
- kind: domain-security
  name: Citi Domain Security
  slug: citi-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: citi
tags:
- Banking
- Financial-Services
- Open Banking
- Payments
- Treasury
website: https://www.citi.com
---
