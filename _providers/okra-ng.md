---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Okra Ng Agentic Access
  operation_count: 27
  slug: okra-ng-agentic-access
  summary_line: 27 operations · 27 acting
api_count: 8
apis:
- description: Linked bank accounts.
  name: Okra Accounts API
  slug: okra-ng-accounts-api
- description: Account authentication records and Link.
  name: Okra Auth API
  slug: okra-ng-auth-api
- description: Account balances.
  name: Okra Balance API
  slug: okra-ng-balance-api
- description: KYC identity on file with the bank.
  name: Okra Identity API
  slug: okra-ng-identity-api
- description: Income verification.
  name: Okra Income API
  slug: okra-ng-income-api
- description: Bank-to-bank payments.
  name: Okra Payments API
  slug: okra-ng-payments-api
- description: Transaction history and spending patterns.
  name: Okra Transactions API
  slug: okra-ng-transactions-api
- description: Callback management.
  name: Okra Webhooks API
  slug: okra-ng-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: Okra API
  slug: open-okra-ng
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/okra-ng-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/okra-ng-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/okra-ng-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/okraHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/okra-technologies
- group: company
  title: ''
  type: Website
  url: https://okra.ng/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.okra.ng/
- group: commercial
  title: ''
  type: Plans
  url: plans/okra-ng-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/okra-ng-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/okra-ng-finops.yml
created: '2026-06-21'
description: Okra was an African open-finance / open-banking infrastructure company based in Lagos, Nigeria. Its REST API connected applications to Nigerian bank accounts to retrieve authentication details, balances, transactions, identity, and income data, and to initiate bank-to-bank payments, with a Link widget and webhooks. Okra wound down operations in May 2025; this catalog documents the API as it was publicly published.
finops:
- name: Okra Ng Finops
  service_category: Financial Services
  slug: okra-ng-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/okra-ng.png
layout: provider
modified: '2026-06-21'
name: Okra
nav: Providers
network: true
overview: 'Okra publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Auth API, Balance API, and 5 more. Tagged areas include Open Banking, Open Finance, Fintech, Africa, and Nigeria.


  Okra''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Okra Ng Plans Pricing
  plan_count: 3
  slug: okra-ng-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 3
  name: Okra Ng Rate Limits
  slug: okra-ng-rate-limits
score:
  band: thin
  composite: 34.5
  delta: -4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Okra Ng Authentication
  slug: okra-ng-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Okra Ng Domain Security
  slug: okra-ng-domain-security
  summary_line: no transport/DNS hardening detected
slug: okra-ng
tags:
- Open Banking
- Open Finance
- Fintech
- Africa
- Nigeria
- Financial Data
website: https://okra.ng/
---
