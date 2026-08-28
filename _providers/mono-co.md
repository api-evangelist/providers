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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Mono Co Agentic Access
  operation_count: 16
  slug: mono-co-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 6
apis:
- description: Account details and balance for a linked account.
  name: Mono Account Information API
  slug: mono-co-account-information-api
- description: Initiate Connect account linking and exchange a code for an account id.
  name: Mono Account Linking API
  slug: mono-co-account-linking-api
- description: Customers, mandates, balance inquiry, and recurring debits.
  name: Mono Direct Debit API
  slug: mono-co-direct-debit-api
- description: One-time bank-to-bank payments.
  name: Mono DirectPay API
  slug: mono-co-directpay-api
- description: Identity verification and income signals for a linked account.
  name: Mono Identity and Income API
  slug: mono-co-identity-and-income-api
- description: Transactions and bank statements for a linked account.
  name: Mono Transactions and Statements API
  slug: mono-co-transactions-and-statements-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mono Account Information API
  slug: open-mono-co-account-information-api
- collection_type: open
  name: Mono Account Information Account Linking API
  slug: open-mono-co-account-linking-api
- collection_type: open
  name: Mono Account Information Direct Debit API
  slug: open-mono-co-direct-debit-api
- collection_type: open
  name: Mono Account Information DirectPay API
  slug: open-mono-co-directpay-api
- collection_type: open
  name: Mono Account Information Identity and Income API
  slug: open-mono-co-identity-and-income-api
- collection_type: open
  name: Mono Account Information Transactions and Statements API
  slug: open-mono-co-transactions-and-statements-api
- collection_type: open
  name: Mono API
  slug: open-mono-co
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mono-co-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mono-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mono-co-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withmono
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mono-hq
- group: company
  title: ''
  type: Website
  url: https://mono.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mono.co
- group: commercial
  title: ''
  type: Plans
  url: plans/mono-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mono-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mono-co-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://mono.co/blog
created: '2026-06-21'
description: Mono is an African open-banking platform that lets businesses access bank and financial data and collect recurring payments through a single API. The Mono REST API at api.withmono.com covers account linking (Connect), transactions, statements, identity, income, and balance, plus DirectPay one-time payments and Direct Debit mandates, secured with a mono-sec-key header.
finops:
- name: Mono Co Finops
  service_category: Financial Services
  slug: mono-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mono-co.png
layout: provider
modified: '2026-06-21'
name: Mono
nav: Providers
network: true
overview: 'Mono publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account Information API, Account Linking API, Direct Debit API, and 3 more. Tagged areas include Open Banking, Financial Data, Payments, Direct Debit, and Africa.


  Mono''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Mono Co Plans Pricing
  plan_count: 4
  slug: mono-co-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Mono Co Rate Limits
  slug: mono-co-rate-limits
score:
  band: thin
  composite: 38.6
  delta: 2.3
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mono-co/refs/heads/main/screenshots/mono-co-2026-08-07T184212.png
security:
- kind: authentication
  name: Mono Co Authentication
  slug: mono-co-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mono Co Domain Security
  slug: mono-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mono-co
tags:
- Open Banking
- Financial Data
- Payments
- Direct Debit
- Africa
website: https://mono.co
---
