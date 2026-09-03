---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Capitalist Agentic Access
  operation_count: 1
  slug: capitalist-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Capitalist API enables programmatic mass payouts, transfers, currency conversion, and balance and transaction management across Capitalist's supported payment systems and cryptocurrencies. It is d
  name: Capitalist API
  slug: capitalist-api
- baseURL: https://api.capitalist.net
  baseurl_source: spec
  description: The Capitalist Payments API API from Capitalist — 1 operation(s) for capitalist payments api.
  name: Capitalist Capitalist Payments API API
  slug: capitalist-capitalist-payments-api-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Capitalist Payments Capitalist Payments API API
  slug: open-capitalist-capitalist-payments-api-api
- collection_type: open
  name: Capitalist Payments API
  slug: open-capitalist
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/capitalist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capitalist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/capitalist-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capitalist-net
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capitalist-inc
- group: company
  title: ''
  type: Website
  url: https://capitalist.net/
- group: docs
  title: ''
  type: Documentation
  url: https://capitalist.net/developers/api
- group: start
  title: ''
  type: Signup
  url: https://capitalist.net/reg
- group: start
  title: ''
  type: Login
  url: https://capitalist.net/login
- group: commercial
  title: ''
  type: Pricing
  url: https://capitalist.net/fees
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capitalist.net/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capitalist.net/useragreement
created: '2024-11-05'
description: Capitalist is a payment platform that lets businesses make mass payouts and receive money across multiple payment systems and cryptocurrencies without having to open separate accounts with each. The Capitalist API automates bulk payouts, exchange between currencies and digital assets, account balance queries, and transaction history retrieval for fintech, affiliate-network, and marketplace use cases operating across the CIS region and globally.
finops:
- name: Capitalist Finops
  service_category: API
  slug: capitalist-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capitalist.png
layout: provider
modified: '2026-04-23'
name: Capitalist
nav: Providers
network: true
overview: 'Capitalist publishes 1 API on the [APIs.io](https://apis.io/) network: Capitalist Payments API API. Tagged areas include Bulk Payouts, Cryptocurrency, Finance, Mass Payments, and Payment Platform.


  Capitalist''s developer surface includes authentication, documentation, signup flow, pricing, and 8 more developer resources.'
plans:
- name: Capitalist Plans Pricing
  plan_count: 3
  slug: capitalist-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Capitalist Rate Limits
  slug: capitalist-rate-limits
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/capitalist/refs/heads/main/screenshots/capitalist-2026-06-20T173944.png
security:
- kind: authentication
  name: Capitalist Authentication
  slug: capitalist-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Capitalist Domain Security
  slug: capitalist-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: capitalist
tags:
- Bulk Payouts
- Cryptocurrency
- Finance
- Mass Payments
- Payment Platform
- Payments
- Payouts
- Remittance
website: https://capitalist.net/
---
